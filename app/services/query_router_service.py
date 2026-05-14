import ollama


ANALYTICS_KEYWORDS = [
    "most",
    "least",
    "average",
    "compare",
    "comparison",
    "faster",
    "slower",
    "fastest",
    "slowest",
    "how many",
    "wins",
    "statistics",
    "stats",
    "dominant"
]


def determine_query_type(query: str):
    query_lower = query.lower()

    # Step 1 — Deterministic routing
    for keyword in ANALYTICS_KEYWORDS:
        if keyword in query_lower:
            return "analytics"

    # Step 2 — LLM fallback
    return llm_route_query(query)


def llm_route_query(query: str):
    prompt = f"""
Classify the following Formula 1 query.

Return ONLY one word:
- retrieval
- analytics

Definitions:

retrieval:
- asking for specific race information
- asking about a driver/team/race
- retrieving facts or events

analytics:
- counting
- comparisons
- rankings
- trends
- statistics
- aggregation

Query:
{query}
"""

    response = ollama.chat(
        model="llama3.2",
        options={
            "temperature": 0
        },
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    content = response["message"]["content"].strip().lower()

    if content not in ["retrieval", "analytics"]:
        return "retrieval"

    return content