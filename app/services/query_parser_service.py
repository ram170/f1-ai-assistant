import ollama
import json


def parse_query(query: str):
    prompt = f"""
Extract structured information from this Formula 1 query.

Strictly return ONLY a valid JSON and nothing else.
group_by should strictly have a value based on relevance of the query and it should be a string.
year value should be an integer if mentioned in the query, else it should be null.

IMPORTANT ENTITY RULE:
    - NEVER modify full driver names.
    - NEVER modify full constructor/team names.
    - NEVER invent or merge names.
    - ONLY expand names if they are CLEAR abbreviations.
    - If uncertain, preserve the original text exactly.

SAFE AUTOCOMPLETE
    ONLY expand extremely obvious abbreviations:
    - Ham -> Lewis Hamilton
    - Max -> Max Verstappen
    - Merc -> Mercedes


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
- wins (strictly means position 1 finishes)
- podiums (strictly means position 1, 2, or 3 finishes)
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
        Task:
        Rewrite the user's Formula 1 query ONLY for normalization purposes.

        DO NOT answer the question.

        IMPORTANT ENTITY RULE:
        - NEVER modify full driver names.
        - NEVER modify full constructor/team names.
        - NEVER invent or merge names.
        - ONLY expand names if they are CLEAR abbreviations.
        - If uncertain, preserve the original text exactly.

        Allowed transformations only:

        1. POSITION NORMALIZATION
          - Replace any mention of rank or position (p10, 10th, tenth, 10) with the format: "integer (string)" (e.g., 10 (tenth)).

        2. YEAR NORMALIZATION
        Convert spoken years:
        - twenty twenty -> 2020

        3. SAFE AUTOCOMPLETE
        ONLY expand extremely obvious abbreviations:
        - Ham -> Lewis Hamilton
        - Max -> Max Verstappen
        - Merc -> Mercedes

        DO NOT modify already complete names.

        4. OUTPUT
        Return ONLY the rewritten query text.

        Examples:

        Input:
        Who was p1 in 2021

        Output:
        Who was 1 (first) in 2021

        Input:
        Who came tenth in italian grand prix in twenty twenty

        Output:
        Who came 10 (tenth) in Italian Grand Prix in 2020

        Input:
        What was the position of Charles Leclerc in Hungarian Grand Prix in 2020

        Output:
        What was the position of Charles Leclerc in Hungarian Grand Prix in 2020

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
    print("LLM response for retrieval query parsing:", response["message"]["content"])
    return response["message"]["content"]