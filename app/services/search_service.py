from app.services.embedding_service import generate_embedding
from app.services.chroma_service import get_collection

collection = get_collection()

def add_race_documents(races):
    for race in races:
        embedding = generate_embedding(race["text"])

        collection.add(
            ids=[race["id"]],
            documents=[race["text"]],
            embeddings=[embedding],
            metadatas=[
                {
                    "team": race["team"],
                    "driver": race["driver"],
                    "year": race["year"],
                    "track": race["track"],
                    "position": race["position"]
                }
            ]
        )

def semantic_search(query: str):
    query_embedding = generate_embedding(query)

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=3
    )

    return results

def metadata_search(team: str, year: int):
    results = collection.get(
        where={
            "$and": [
                {"team": team},
                {"year": year}
            ]
        }
    )

    return results

# TODO: Finish the route

def hybrid_search(
    query: str,
    driver: str,
    year: int,
    position: int
):
    query_embedding = generate_embedding(query)

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=5,
        where={
            "$and": [
                {"driver": driver},
                {"year": year},
                {"position": position}
            ]
        }
    )

    return results