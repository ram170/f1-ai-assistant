import fastf1

from app.services.search_service import add_race_documents
from app.services.race_summary_service import generate_race_summary


def build_race_document(row, race_name, year):
    position = int(row["Position"])

    driver = f"{row['FirstName']} {row['LastName']}"

    text = generate_race_summary(
        driver=driver,
        team=row["TeamName"],
        position=position,
        race_name=race_name,
        year=year
    )

    return {
        "id": f"{year}_{race_name}_{position}",
        "text": text,
        "team": row["TeamName"],
        "driver": driver,
        "year": year,
        "track": race_name,
        "position": position
    }


def ingest_season(year: int):
    schedule = fastf1.get_event_schedule(year=year, include_testing=False)

    all_documents = []

    for _, event in schedule.iterrows():
        race_name = event["EventName"]

        try:
            print(f"Ingesting {year} {race_name}")

            session = fastf1.get_session(year, race_name, "R")

            session.load()

            results = session.results

            for _, row in results.iterrows():
                document = build_race_document(
                    row,
                    race_name,
                    year
                )

                all_documents.append(document)

        except Exception as e:
            print(f"Failed for {race_name}: {e}")

    add_race_documents(all_documents)

    print(f"Ingested {len(all_documents)} documents")