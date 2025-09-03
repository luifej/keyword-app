# Keyword Research App (MVP)

Lightweight Semrush/Ahrefs-style app: generate keyword ideas, fetch metrics, cluster & score, export lists.

## Stack
- Frontend: Next.js + Tailwind (UI)
- Backend: FastAPI (Python) + Celery (async)
- DB: PostgreSQL
- Queue/Cache: Redis
- Infra: Docker Compose (local), Playwright (scraping)

## Quickstart
1) Copy `.env.example` to `.env` and fill credentials.
2) From the `infra/` folder, run:
   ```bash
   docker compose up --build
   ```
3) Web at http://localhost:3000, API at http://localhost:8000

## Dev notes
- The scraping and Google Ads calls are stubbed. Replace stubs in `apps/api/app/services/`.
- Add real clustering logic in `cluster.py`.
- DB models are minimal; extend as needed.
