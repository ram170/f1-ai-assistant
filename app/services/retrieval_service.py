from app.services.query_parser_service import parse_query_for_retrieval
from app.services.embedding_service import generate_embedding
from app.services.chroma_service import get_collection
from app.services.llm_service import generate_response

collection = get_collection()

def retrieval_pipeline(query: str):
    print("Running retrieval pipeline for query:", query)
    modified_query = parse_query_for_retrieval(query)
    
    query_embedding = generate_embedding(modified_query)

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=10
    )

    print("Raw search results for retrieval:", results)

    documents = results["documents"][0]
    distances = results["distances"][0]

    filtered_documents = []

    for doc, distance in zip(documents, distances):
        if distance <= 1:
            filtered_documents.append(doc)

    if not filtered_documents:
        return {
            "question": query,
            "answer": "No relevant race data found."
        }

    response = generate_response(
        query=query,
        documents=filtered_documents
    )

    return {
        "question": query,
        "query_type": "retrieval",
        "answer": response,
        "sources": filtered_documents,
        "metadata": {
            "documents_found": len(filtered_documents)
        }
    }