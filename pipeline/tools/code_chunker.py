from langchain.text_splitter import RecursiveCharacterTextSplitter, Language


# Map our language strings to LangChain Language enum
LANGUAGE_MAP = {
    "python":     Language.PYTHON,
    "javascript": Language.JS,
    "typescript": Language.JS,
    "java":       Language.JAVA,
    "go":         Language.GO,
    "rust":       Language.RUST,
    "cpp":        Language.CPP,
    "c":          Language.CPP,
}


def chunk_file(file_path: str, content: str, language: str) -> list[dict]:
    """
    Split a single file into chunks using language-aware splitting.
    Falls back to character splitting for unknown languages.

    Returns list of chunk dicts with metadata.
    """
    lang_enum = LANGUAGE_MAP.get(language)

    if lang_enum:
        splitter = RecursiveCharacterTextSplitter.from_language(
            language=lang_enum,
            chunk_size=1000,
            chunk_overlap=100
        )
    else:
        # Markdown, YAML, SQL, etc.
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=100,
            separators=["\n\n", "\n", " ", ""]
        )

    chunks = splitter.split_text(content)

    return [
        {
            "file_path": file_path,
            "language": language,
            "chunk_index": i,
            "content": chunk,
            # Metadata for vector DB filtering
            "metadata": {
                "file_path": file_path,
                "language": language,
                "chunk_index": i,
                "total_chunks": len(chunks)
            }
        }
        for i, chunk in enumerate(chunks)
    ]


def chunk_all_files(files: list[dict]) -> list[dict]:
    """
    Chunk all files from the repo.
    Input: list of {"path", "content", "language"}
    Output: flat list of all chunks across all files
    """
    all_chunks = []

    for file in files:
        chunks = chunk_file(
            file_path=file["path"],
            content=file["content"],
            language=file["language"]
        )
        all_chunks.extend(chunks)
        print(f"  🔪 {file['path']} → {len(chunks)} chunks")

    print(f"\n📦 Total chunks: {len(all_chunks)}")
    return all_chunks