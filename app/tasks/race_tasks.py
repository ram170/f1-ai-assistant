from app.celery_app import celery
from app.ingestion.race_ingestor import ingest_season


@celery.task
def ingest_season_task(year: int):
    ingest_season(year)

    return f"{year} ingestion completed"