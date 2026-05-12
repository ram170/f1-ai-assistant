import ollama

def generate_embedding(text: str):
    response = ollama.embed(
        model="all-minilm",
        input=text
    )

    return response["embeddings"][0]