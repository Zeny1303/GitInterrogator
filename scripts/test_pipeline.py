import uuid
from pipeline.nodes.ingestion import ingestion_node
from pipeline.state import InterviewState

# Test with any public GitHub repo
initial_state: InterviewState = {
    "github_url": "https://github.com/tiangolo/fastapi",
    "session_id": str(uuid.uuid4()),
    "repo_name": "",
    "repo_language": "",
    "total_files_fetched": 0,
    "filtered_files": [],
    "chunks_stored": 0,
    "technical_report": None,
    "question_bank": {},
    "current_stage": "INTRO",
    "interview_transcript": [],
    "time_elapsed_seconds": 0,
    "evaluation": None,
    "error": None,
    "current_node": "start"
}

result = ingestion_node(initial_state)

print("\n📊 RESULT SUMMARY:")
print(f"  Repo:          {result['repo_name']}")
print(f"  Language:      {result['repo_language']}")
print(f"  Files fetched: {result['total_files_fetched']}")
print(f"  Chunks stored: {result['chunks_stored']}")
print(f"  Error:         {result['error']}")