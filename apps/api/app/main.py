from fastapi import FastAPI
from app.routers import keywords

app = FastAPI(title="Keyword API")
app.include_router(keywords.router, prefix="/keywords", tags=["keywords"])

@app.get("/health")
def health():
    return {"ok": True}
