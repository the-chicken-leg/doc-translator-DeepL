from getpass import getpass
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
from pathlib import Path

import deepl

from get_languages import get_languages

def main():
    # validate API key and get usage stats
    usage, api_key = None, None
    while not usage:
        while not api_key:
            api_key = getpass(prompt="Enter API key: ")
        try:
            deepl_client = deepl.DeepLClient(api_key)
            usage = deepl_client.get_usage()
        except deepl.AuthorizationException as err:
            print(f"Error: {err}")
            api_key = None

    if usage.any_limit_reached:
        print('\nTranslation limit reached.')
    if usage.character.valid:
        print(f"\nCharacter usage: {usage.character.count} of {usage.character.limit}. 1 Document >= 50,000 characters.")
    if usage.document.valid:
        print(f"\nDocument usage: {usage.document.count} of {usage.document.limit}")  

    # get supported languages
    supported_languages, abbreviations = get_languages(api_key)

    print(f"\nSupported target languages are:\n\n{supported_languages}")

    # user enters target language and formality level
    target_lang = None
    while not target_lang:
        target_lang = input("\nEnter target language abbreviation: ")
        if target_lang not in abbreviations:
            target_lang = None

    formality = None
    while not formality:
        formality = input("\nEnter formality level (default, prefer_more, prefer_less): ")
        if formality not in ("default", "prefer_more", "prefer_less"):
            formality = None

    # select source and destination filepaths
    input_path = None
    while not input_path:
        input("\nPress Enter key to select a file to translate.")
        input_path = askopenfilename(
            defaultextension="pdf",
            filetypes=[("PDF files", "*.pdf"), ("All Files", "*.*")],
        )
    input_path = Path(input_path)
    print(f"Selected file:          {input_path}")

    output_path = None
    while not output_path:
        input("\nPress Enter key to select save location.")
        output_path = asksaveasfilename(
            defaultextension="pdf",
            filetypes=[("PDF files", "*.pdf"), ("All Files", "*.*")],
        )
    output_path = Path(output_path)
    print(f"Selected save location: {output_path}")

    # translate
    print("\nTranslating. This might take a few minutes...")
    try:
        deepl_client.translate_document_from_filepath(
            input_path,
            output_path,
            target_lang=target_lang,
            formality=formality,
        )
        print("Translation finished.")
    except deepl.DocumentTranslationException as err:
        # If an error occurs during document translation after the document was
        # already uploaded, a DocumentTranslationException is raised. The
        # document_handle property contains the document handle that may be used to
        # later retrieve the document from the server, or contact DeepL support.
        print(f"Error after uploading: {err}")
    except deepl.DeepLException as err:
        # Errors during upload raise a DeepLException
        print(f"Error: {err}")       

if __name__ == "__main__":
    main()
