from fastapi import FastAPI
from app.routes.search_routes import router

app = FastAPI()

app.include_router(router)

@app.get("/")
def home():
    return {
        "message": "F1 AI Semantic Search API"
    }