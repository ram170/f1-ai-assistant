import ollama
import json


def parse_query(query: str):
    prompt = f"""
Extract structured information from this Formula 1 query.

Strictly return ONLY a valid JSON and nothing else.
group_by should strictly have a value based on relevance of the query and it should be a string.
autocomplete the driver and team name if the query contains partial value.
year value should be an integer if mentioned in the query, else it should be null.

Supported fields:
- query_type
- metric
- aggregation
- group_by
- driver
- team
- year
- position

Definitions:

aggregation:
- most
- least
- average

group_by:
- driver
- team

metric examples:
- wins
- podiums
- races

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

    content = response["message"]["content"]
    print("LLM response for query parsing:", content)

    try:
        return json.loads(content)
    except Exception:
        print("Failed to parse JSON from LLM response.")
        return {}
    
def parse_query_for_retrieval(query: str):
    prompt = f"""
        Task: Rewrite the user's Formula 1 query based on specific formatting rules. 
        DO NOT answer the question. Only modify the text of the query.

        RULES:
        1. POSITION: Replace any mention of rank or position (p10, 10th, tenth, 10) with the format: "integer (string)" (e.g., 10 (tenth)).
        2. YEAR: Ensure the year is a 4-digit integer.
        3. AUTOCOMPLETE: Expand partial driver/team names (e.g., "Ham" to "Lewis Hamilton", "Merc" to "Mercedes").
        4. OUTPUT: Return ONLY the rewritten query. No conversational filler.

        EXAMPLES:
        - Input: "Who was p1 in 2021" 
        - Output: Who was 1 (first) in 2021
        
        - Input: "Who came tenth in italian grand prix in twenty twenty"
        - Output: Who came 10 (tenth) in Italian Grand Prix in 2020

        Query: {query}
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
    print("LLM response for retrieval query parsing:", response["message"]["content"])
    return response["message"]["content"]