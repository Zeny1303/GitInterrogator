from pipeline.state import InterviewState
from pipeline.tools.github_loader import fetch_github_repo
from pipeline.tools.code_chunker import chunk_all_files
from rag.embedder import embed_chunks


def ingestion_node(state: InterviewState) -> InterviewState:
    """
    LangGraph Node: Ingestion Agent

    Steps:
    1. Fetch GitHub repo files
    2. Chunk all files
    3. Embed + store in Qdrant

    Updates state with fetched file info and chunk count.
    """
    print("\n" + "="*50)
    print("🚀 INGESTION AGENT STARTING")
    print("="*50)

    try:
        github_url = state["github_url"]
        session_id = state["session_id"]

        # ── Step 1: Fetch repo ───────────────────────────────────
        print(f"\n📡 Fetching repo: {github_url}")
        repo_data = fetch_github_repo(github_url)

        # ── Step 2: Chunk files ──────────────────────────────────
        print("\n🔪 Chunking files...")
        chunks = chunk_all_files(repo_data["files"])

        # ── Step 3: Embed + store ────────────────────────────────
        print("\n🔢 Embedding and storing in Qdrant...")
        chunks_stored = embed_chunks(chunks, session_id)

        print("\n✅ INGESTION COMPLETE")

        return {
            **state,
            "repo_name": repo_data["repo_name"],
            "repo_language": repo_data["repo_language"],
            "total_files_fetched": repo_data["total_files_fetched"],
            "filtered_files": repo_data["files"],
            "chunks_stored": chunks_stored,
            "current_node": "ingestion_complete"
        }

    except Exception as e:
        print(f"\n❌ INGESTION FAILED: {e}")
        return {
            **state,
            "error": str(e),
            "current_node": "ingestion_failed"
        }