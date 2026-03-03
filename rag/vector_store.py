import os
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams
from dotenv import load_dotenv

load_dotenv()

COLLECTION_NAME = "codebase"
VECTOR_SIZE = 384  # matches all-MiniLM-L6-v2 embedding model


def get_qdrant_client() -> QdrantClient:
    """
    Returns Qdrant client.
    Uses local file storage by default (no Docker needed for dev).
    Switch to cloud URL in production.
    """
    qdrant_url = os.getenv("QDRANT_URL")

    if qdrant_url:
        # Production: Qdrant Cloud
        return QdrantClient(
            url=qdrant_url,
            api_key=os.getenv("QDRANT_API_KEY")
        )
    else:
        # Development: local file storage
        return QdrantClient(path="./data/qdrant")


def create_collection(client: QdrantClient, session_id: str) -> str:
    """
    Create a per-session collection so different repos don't mix.
    Collection name: codebase_{session_id}
    """
    collection_name = f"{COLLECTION_NAME}_{session_id}"

    # Delete if exists (fresh analysis)
    existing = [c.name for c in client.get_collections().collections]
    if collection_name in existing:
        client.delete_collection(collection_name)
        print(f"  🗑️  Deleted existing collection: {collection_name}")

    client.create_collection(
        collection_name=collection_name,
        vectors_config=VectorParams(
            size=VECTOR_SIZE,
            distance=Distance.COSINE
        )
    )
    print(f"  ✅ Created collection: {collection_name}")
    return collection_name


def get_collection_name(session_id: str) -> str:
    return f"{COLLECTION_NAME}_{session_id}"