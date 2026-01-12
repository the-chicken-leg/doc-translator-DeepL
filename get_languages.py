import json
from pathlib import Path
from pprint import pprint

# the below code imports languages from ./supported_languages.json
# with open(Path("./supported_languages.json"), mode="r", encoding="utf-8") as f:
#     languages = json.load(f)
# LANGUAGES_DATA = {
#     language["language"]: {
#         "name": language["name"],
#         "supports_formality": language["supports_formality"]
#     } 
#     for language in languages
# }

LANGUAGE_DATA = {
    'AR': {'name': 'Arabic', 'supports_formality': False},
    'BG': {'name': 'Bulgarian', 'supports_formality': False},
    'CS': {'name': 'Czech', 'supports_formality': False},
    'DA': {'name': 'Danish', 'supports_formality': False},
    'DE': {'name': 'German', 'supports_formality': True},
    'EL': {'name': 'Greek', 'supports_formality': False},
    'EN-GB': {'name': 'English (British)', 'supports_formality': False},
    'EN-US': {'name': 'English (American)', 'supports_formality': False},
    'ES': {'name': 'Spanish', 'supports_formality': True},
    'ES-419': {'name': 'Spanish', 'supports_formality': True},
    'ET': {'name': 'Estonian', 'supports_formality': False},
    'FI': {'name': 'Finnish', 'supports_formality': False},
    'FR': {'name': 'French', 'supports_formality': True},
    'HE': {'name': 'Hebrew', 'supports_formality': False},
    'HU': {'name': 'Hungarian', 'supports_formality': False},
    'ID': {'name': 'Indonesian', 'supports_formality': False},
    'IT': {'name': 'Italian', 'supports_formality': True},
    'JA': {'name': 'Japanese', 'supports_formality': True},
    'KO': {'name': 'Korean', 'supports_formality': False},
    'LT': {'name': 'Lithuanian', 'supports_formality': False},
    'LV': {'name': 'Latvian', 'supports_formality': False},
    'NB': {'name': 'Norwegian (Bokmål)', 'supports_formality': False},
    'NL': {'name': 'Dutch', 'supports_formality': True},
    'PL': {'name': 'Polish', 'supports_formality': True},
    'PT-BR': {'name': 'Portuguese (Brazilian)', 'supports_formality': True},
    'PT-PT': {'name': 'Portuguese (European)', 'supports_formality': True},
    'RO': {'name': 'Romanian', 'supports_formality': False},
    'RU': {'name': 'Russian', 'supports_formality': True},
    'SK': {'name': 'Slovak', 'supports_formality': False},
    'SL': {'name': 'Slovenian', 'supports_formality': False},
    'SV': {'name': 'Swedish', 'supports_formality': False},
    'TH': {'name': 'Thai', 'supports_formality': False},
    'TR': {'name': 'Turkish', 'supports_formality': False},
    'UK': {'name': 'Ukrainian', 'supports_formality': False},
    'VI': {'name': 'Vietnamese', 'supports_formality': False},
    'ZH': {'name': 'Chinese (simplified)', 'supports_formality': False},
    'ZH-HANS': {'name': 'Chinese (simplified)', 'supports_formality': False},
    'ZH-HANT': {'name': 'Chinese (traditional)', 'supports_formality': False}
}

LANGUAGES = [language for language in LANGUAGE_DATA]

SPELLED_OUT = ", ".join([f"{long['name']} ({short})" for short, long in LANGUAGE_DATA.items()])

FORMALITIES = ["less", "more", "prefer_less", "prefer_more"]

if __name__ == "__main__":
    pprint(LANGUAGE_DATA)
    print()
    pprint(LANGUAGES)
    print()
    print(SPELLED_OUT)
    print()
    pprint(FORMALITIES)
    