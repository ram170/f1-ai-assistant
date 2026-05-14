import ollama


def generate_response(query: str, documents: list[str]):
    context = "\n".join(documents)

    prompt = f"""
You are an F1 AI assistant.

Answer the user's question using the provided race data.

Question:
{query}

Race Data:
{context}

Provide a concise and human-readable response without any filler text. Just respond with the answer or say "I don't know" if the answer cannot be found in the provided data.
"""

    response = ollama.chat(
        model="llama3.2",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]