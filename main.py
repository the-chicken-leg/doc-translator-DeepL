import os
from dotenv import load_dotenv
import deepl

def main():
    load_dotenv()
    api_key = os.environ.get("DEEPL_API_KEY")
    if api_key is None:
        raise RuntimeError("The API key was not found. Please check your .env file.")

    deepl_client = deepl.DeepLClient(api_key)

    result = deepl_client.translate_text("Mein Arbeitgeber ist Scheiße!", target_lang="EN-US")
    print(result.text)

if __name__ == "__main__":
    main()
