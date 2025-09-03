from .celery_app import celery_app
from app.services.serp_playwright import fetch_autosuggest_paa
from app.services.google_ads import fetch_volumes
# from app.services.cluster import cluster_keywords  # future use

@celery_app.task
def discover_ideas(payload: dict):
    seed = payload.get("seed", "")
    country = payload.get("country", "US")
    lang = payload.get("lang", "en")

    ideas = fetch_autosuggest_paa(seed, country, lang)  # list[{keyword, source}]
    metrics_map = fetch_volumes([i["keyword"] for i in ideas])  # {kw: {volume,cpc,difficulty}}

    merged = []
    for i in ideas:
        m = metrics_map.get(i["keyword"], {})
        merged.append({
            "keyword": i["keyword"],
            "source": i.get("source", "stub"),
            "volume": m.get("volume"),
            "cpc": m.get("cpc"),
            "difficulty": m.get("difficulty"),
        })

    # TODO: persist to DB and cluster
    return {"count": len(merged), "items": merged[:10]}
