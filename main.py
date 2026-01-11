import os
from dotenv import load_dotenv

def main():
    load_dotenv()
    api_key = os.environ.get("DEEPL_API_KEY")
    if api_key is None:
        raise RuntimeError("The API key was not found. Please check your .env file.")
    print(api_key)

if __name__ == "__main__":
    main()
