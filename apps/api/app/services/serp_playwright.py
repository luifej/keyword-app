# Placeholder: replace with real Playwright scrapers for Autosuggest/PAA/Related
def fetch_autosuggest_paa(seed: str, country: str = "US", lang: str = "en"):
    if not seed:
        return []
    return [
        {"keyword": f"{seed} ideas", "source": "autosuggest"},
        {"keyword": f"{seed} tips", "source": "autosuggest"},
        {"keyword": f"{seed} questions", "source": "paa"},
    ]
