import json
from pathlib import Path
from pprint import pprint

# the below code imports languages from ./supported_languages.json
# ./supported_languages.json pulled from here: https://developers.deepl.com/api-reference/languages
# cool improvement would be to pull supported languages automatically at program startup

with open(Path("./supported_languages.json"), mode="r", encoding="utf-8") as f:
    languages = json.load(f)
LANGUAGE_DATA = {
    language["language"]: {
        "name": language["name"],
        "supports_formality": language["supports_formality"]
    } 
    for language in languages
}

LANGUAGES = [language for language in LANGUAGE_DATA]

SPELLED_OUT = ", ".join([f"{long['name']} ({short})" for short, long in LANGUAGE_DATA.items()])

FORMALITIES = ["less", "more", "prefer_less", "prefer_more"]

if __name__ == "__main__":
    pprint(languages)
    print()
    pprint(LANGUAGE_DATA)
    print()
    pprint(LANGUAGES)
    print()
    print(SPELLED_OUT)
    print()
    pprint(FORMALITIES)
