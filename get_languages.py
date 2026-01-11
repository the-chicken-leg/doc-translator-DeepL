import json
from pathlib import Path
from pprint import pprint

with open(Path("./supported_languages.json"), mode="r", encoding="utf-8") as f:
    languages = json.load(f)
LANGUAGES = {
    language["language"]: {
        "name": language["name"],
        "supports_formality": language["supports_formality"]
    } 
    for language in languages
}

FORMALITIES = ["less", "more", "prefer_less", "prefer_more"]

if __name__ == "__main__":
    pprint(LANGUAGES)
    print()
    pprint(FORMALITIES)