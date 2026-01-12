from getpass import getpass
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
from pathlib import Path
import argparse

import deepl

from get_languages import *

def main():
    parser = argparse.ArgumentParser(description="Translate a document with DeepL.")
    parser.add_argument(
        "target_lang",
        choices=LANGUAGES,
        help="available target languages"
    )
    parser.add_argument(
        "-f",
        "--formality",
        choices=FORMALITIES,
        default="more",
    )
    args = parser.parse_args()
    target_lang, formality = args.target_lang, args.formality
    if not LANGUAGE_DATA[target_lang]["supports_formality"]:
        formality = None

    usage = None
    while not usage:
        api_key = getpass(prompt="Enter API key: ")
        try:
            deepl_client = deepl.DeepLClient(api_key)
            usage = deepl_client.get_usage()
        except deepl.AuthorizationException as error:
            print(f"Error: {error}")

    if usage.any_limit_reached:
        print('\nTranslation limit reached.')
    if usage.character.valid:
        print(f"\nCharacter usage: {usage.character.count} of {usage.character.limit}. 1 Document = 50,000 characters.")
    if usage.document.valid:
        print(f"\nDocument usage: {usage.document.count} of {usage.document.limit}")        

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
    
    print("\nTranslating. This might take a few minutes...")
    try:
        deepl_client.translate_document_from_filepath(
            input_path,
            output_path,
            target_lang=target_lang,
            formality=formality,
        )
        input("Translation finished. Press Enter key to exit.")
        print("Cleaning up...")
    except deepl.DocumentTranslationException as error:
        # If an error occurs during document translation after the document was
        # already uploaded, a DocumentTranslationException is raised. The
        # document_handle property contains the document handle that may be used to
        # later retrieve the document from the server, or contact DeepL support.
        input(f"Error after uploading: {error}\nPress Enter key to exit.")
        print("Cleaining up...")
    except deepl.DeepLException as error:
        # Errors during upload raise a DeepLException
        input(f"Error: {error}\nPress Enter key to exit.")
        print("Cleaning up...")        

if __name__ == "__main__":
    main()
