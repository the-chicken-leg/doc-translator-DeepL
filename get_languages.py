import json
import requests

def get_languages(api_key: str) -> tuple[list[str], list[str]]:
    # https://developers.deepl.com/api-reference/languages
    response = requests.get(
        "https://api-free.deepl.com/v2/languages?type=target",
        headers={"Authorization": f"DeepL-Auth-Key {api_key}"},
    )

    languages = sorted(json.loads(response.text), key=lambda d: d["name"])
    supported_languages = [f"{language["name"]} ({language["language"]})" for language in languages]
    abbreviations = [language["language"] for language in languages]

    return supported_languages, abbreviations
