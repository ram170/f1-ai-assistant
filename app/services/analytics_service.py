from collections import Counter
from app.services.chroma_service import get_collection
from app.services.query_parser_service import parse_query


collection = get_collection()

def form_dynamic_where_clause(filters: dict):
        where_conditions = []

        if filters.get("year"):
            where_conditions.append({"year": filters["year"]})

        if filters.get("team") and filters.get("team") != "null":
            where_conditions.append({"team": filters["team"]})

        if filters.get("driver"):
            where_conditions.append({"driver": filters["driver"]})

        if filters.get("position"):
            where_conditions.append({"position": filters["position"]})

        if filters.get("metric") == "wins":
            where_conditions.append({"position": 1})

        elif filters.get("metric") == "podiums":
            where_conditions.append({
                "$or": [
                    {"position": 1},
                    {"position": 2},
                    {"position": 3}
                ]
            })

        return where_conditions

def run_analytics(query: str):
    filters = parse_query(query)
    print("Running analytics with filters:", filters)
    year = filters.get("year")
    aggregation = filters.get("aggregation")
    metric = filters.get("metric")
    group_by = filters.get("group_by") or "driver"

    where_conditions = []

    where_conditions = form_dynamic_where_clause(filters)

    where_clause = None

    if len(where_conditions) == 1:
        where_clause = where_conditions[0]

    elif len(where_conditions) > 1:
        where_clause = {
            "$and": where_conditions
        }

    print("Constructed where clause for analytics query:", where_clause)

    results = collection.get(
        where=where_clause
    )
    print("Analytics query results:", results, group_by)

    metadatas = results["metadatas"]

    grouped_values = [
        metadata[group_by]
        for metadata in metadatas
    ]

    counts = Counter(grouped_values)
    print("Counts for analytics:", counts)

    if not counts:
        return {
            "answer": "No data found for the given query."
        }

    if aggregation == "most":
        result = counts.most_common(1)[0]

    elif aggregation == "least":
        result = counts.most_common()[-1]

    else:
        return {
            "answer": "Unsupported aggregation."
        }

    return {
        "question": query,
        "query_type": "analytics",
        "answer": f"{result[0]} has the {aggregation} {metric} with a count of {result[1]}",
        "sources": [],
        "metadata": {
            "entity": result[0],
            "count": result[1],
            "metric": metric,
            "aggregation": aggregation,
            "year": year
        }
    }