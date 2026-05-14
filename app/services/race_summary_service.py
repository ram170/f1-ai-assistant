import ollama


def generate_race_summary(
    driver: str,
    team: str,
    position: int,
    race_name: str,
    year: int
):
    prompt = f"""
Convert the following Formula 1 race result into a natural and concise race summary.

Driver: {driver}
Team: {team}
Position: {position}
Race: {race_name}
Year: {year}

Rules:
- Keep it factual
- Do not invent race events
- Keep it concise
- Make it sound natural
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

    return response["message"]["content"]