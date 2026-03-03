import os
import base64
from github import Github, GithubException
from dotenv import load_dotenv

load_dotenv()

# ── Files we WANT to analyze ─────────────────────────────────────
ALLOWED_EXTENSIONS = {
    ".py", ".js", ".ts", ".jsx", ".tsx",
    ".java", ".go", ".rs", ".cpp", ".c",
    ".sql", ".yaml", ".yml", ".toml",
    ".md", ".env.example", ".dockerfile"
}

# ── Paths we SKIP entirely ───────────────────────────────────────
SKIP_PATHS = {
    "node_modules", ".git", "__pycache__", ".venv",
    "venv", "dist", "build", ".next", "coverage",
    "migrations", ".pytest_cache", "*.lock",
    "package-lock.json", "yarn.lock", "uv.lock"
}

# ── Max file size to avoid token explosion (50KB) ───────────────
MAX_FILE_SIZE_BYTES = 50_000

# ── Max total files to keep context manageable ──────────────────
MAX_FILES = 60


def should_skip(file_path: str) -> bool:
    """Return True if this file should be ignored."""
    parts = file_path.lower().split("/")
    for part in parts:
        if part in SKIP_PATHS:
            return True
    return False


def get_file_language(file_path: str) -> str:
    """Detect language from extension."""
    ext_map = {
        ".py": "python", ".js": "javascript", ".ts": "typescript",
        ".jsx": "javascript", ".tsx": "typescript", ".java": "java",
        ".go": "go", ".rs": "rust", ".cpp": "cpp", ".c": "c",
        ".sql": "sql", ".yaml": "yaml", ".yml": "yaml",
        ".md": "markdown", ".toml": "toml"
    }
    ext = os.path.splitext(file_path)[1].lower()
    return ext_map.get(ext, "text")


def prioritize_files(files: list[dict]) -> list[dict]:
    """
    Sort files by importance:
    README > entry points > config > source > tests
    """
    def priority(f):
        path = f["path"].lower()
        if "readme" in path:                    return 0
        if path in ("main.py", "app.py",
                    "index.js", "server.js"):   return 1
        if any(x in path for x in
               ["config", "schema", "model",
                "database", "docker"]):          return 2
        if any(x in path for x in
               ["test", "spec"]):               return 4
        return 3

    return sorted(files, key=priority)


def fetch_github_repo(github_url: str) -> dict:
    """
    Main function: fetch and filter all useful files from a GitHub repo.

    Returns:
        {
            "repo_name": str,
            "repo_language": str,
            "files": [{"path": str, "content": str, "language": str}],
            "total_files_fetched": int,
            "skipped_files": int
        }
    """
    token = os.getenv("GITHUB_TOKEN")  # Optional but recommended (higher rate limit)
    g = Github(token) if token else Github()

    # ── Parse URL → owner/repo ───────────────────────────────────
    # Handle: https://github.com/owner/repo or github.com/owner/repo
    clean = github_url.replace("https://", "").replace("http://", "")
    parts = clean.strip("/").split("/")
    if len(parts) < 3:
        raise ValueError(f"Invalid GitHub URL: {github_url}")
    owner, repo_name = parts[1], parts[2]

    try:
        repo = g.get_repo(f"{owner}/{repo_name}")
    except GithubException as e:
        raise ValueError(f"Could not access repo: {e.data.get('message', str(e))}")

    # ── Walk entire repo file tree ───────────────────────────────
    print(f"📂 Fetching repo: {repo.full_name}")
    contents = repo.get_git_tree(sha="HEAD", recursive=True)

    accepted_files = []
    skipped = 0

    for item in contents.tree:
        if item.type != "blob":
            continue

        file_path = item.path
        ext = os.path.splitext(file_path)[1].lower()

        # Filter checks
        if should_skip(file_path):
            skipped += 1
            continue
        if ext not in ALLOWED_EXTENSIONS:
            skipped += 1
            continue
        if item.size > MAX_FILE_SIZE_BYTES:
            print(f"  ⚠️  Skipping large file: {file_path} ({item.size} bytes)")
            skipped += 1
            continue

        accepted_files.append(file_path)

    # Fetch file contents (prioritized, up to MAX_FILES)
    accepted_files_sorted = accepted_files[:MAX_FILES]
    files_data = []

    for path in accepted_files_sorted:
        try:
            file_content = repo.get_contents(path)
            if isinstance(file_content, list):
                continue
            content = base64.b64decode(file_content.content).decode("utf-8", errors="ignore")
            files_data.append({
                "path": path,
                "content": content,
                "language": get_file_language(path)
            })
            print(f"  ✅ {path}")
        except Exception as e:
            print(f"  ❌ Failed to fetch {path}: {e}")
            skipped += 1

    # Prioritize by importance
    files_data = prioritize_files(files_data)

    print(f"\n Fetched: {len(files_data)} files | Skipped: {skipped}")

    return {
        "repo_name": repo.full_name,
        "repo_language": repo.language or "Unknown",
        "files": files_data,
        "total_files_fetched": len(files_data),
        "skipped_files": skipped
    }
"""
if __name__ == "__main__":
    repo_url = input("Enter GitHub repo URL: ")
    data = fetch_github_repo(repo_url)

    print("\n--- SUMMARY ---")
    print("Repo Name:", data["repo_name"])
    print("Primary Language:", data["repo_language"])
    print("Total Files Fetched:", data["total_files_fetched"])
    print("Skipped Files:", data["skipped_files"])

"""    
