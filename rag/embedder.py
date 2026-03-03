from sentence_transformers import SentenceTransformer
from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct
from rag.vector_store import get_qdrant_client, create_collection
import uuid

# Free, fast, runs locally — no API key needed
EMBEDDING_MODEL = "all-MiniLM-L6-v2"

_model = None

def get_embedding_model() -> SentenceTransformer:
    """Lazy load model (only once)."""
    global _model
    if _model is None:
        print("  📥 Loading embedding model...")
        _model = SentenceTransformer(EMBEDDING_MODEL)
    return _model


def embed_chunks(chunks: list[dict], session_id: str) -> int:
    """
    Embed all chunks and store in Qdrant.

    Returns: number of chunks stored
    """
    model = get_embedding_model()
    client = get_qdrant_client()
    collection_name = create_collection(client, session_id)

    # Extract text for embedding
    texts = [chunk["content"] for chunk in chunks]

    print(f"  🔢 Embedding {len(texts)} chunks...")
    vectors = model.encode(texts, show_progress_bar=True).tolist()

    # Build Qdrant points
    points = [
        PointStruct(
            id=str(uuid.uuid4()),
            vector=vector,
            payload=chunk["metadata"] | {"content": chunk["content"]}
        )
        for vector, chunk in zip(vectors, chunks)
    ]

    # Upload in batches of 100
    batch_size = 100
    for i in range(0, len(points), batch_size):
        batch = points[i:i + batch_size]
        client.upsert(collection_name=collection_name, points=batch)
        print(f"  ⬆️  Uploaded batch {i//batch_size + 1}")

    print(f"\n✅ Stored {len(points)} chunks in collection: {collection_name}")
    return len(points)