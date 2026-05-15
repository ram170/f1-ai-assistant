from fastapi import APIRouter
from app.data.sample_races import sample_races
from app.services.chroma_service import get_collection
from app.tasks.race_tasks import ingest_season_task
from app.services.search_service import (
    add_race_documents,
    semantic_search,
    metadata_search,
    ask_question
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

@router.get("/metadata-search")
def search_by_metadata(team: str, year: int):
    results = metadata_search(team, year)

    return results

@router.get("/debug/all")
def get_all_documents():
    collection = get_collection()

    results = collection.get()

    formatted = []

    for i in range(len(results["ids"])):
        formatted.append({
            "id": results["ids"][i],
            "document": results["documents"][i],
            "metadata": results["metadatas"][i]
        })

    return formatted

from app.ingestion.race_ingestor import ingest_season

@router.post("/ingest-season/{year}")
def ingest_year(year: int):
    task = ingest_season_task.delay(year)

    return {
        "message": f"{year} season ingestion queued",
        "task_id": task.id
    }

@router.get("/ask")
def ask(query: str):
    return ask_question(query)