from fastapi import APIRouter
from app.data.sample_races import sample_races
from app.services.search_service import (
    add_race_documents,
    semantic_search
)

router = APIRouter()

@router.post("/ingest")
def ingest_data():
    add_race_documents(sample_races)

    return {
        "message": "Race data ingested successfully"
    }

@router.get("/search")
def search(query: str):
    results = semantic_search(query)

    return results