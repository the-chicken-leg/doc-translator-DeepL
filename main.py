from getpass import getpass
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
from pathlib import Path

import deepl

def main():
    usage = None
    while not usage:
        api_key = getpass(prompt="Enter API key: ")
        try:
            deepl_client = deepl.DeepLClient(api_key)
            usage = deepl_client.get_usage()
        except deepl.AuthorizationException as error:
            print(error)

    if usage.any_limit_reached:
        print('\nTranslation limit reached.')
    if usage.character.valid:
        print(f"\nCharacter usage: {usage.character.count} of {usage.character.limit}. 1 Document = 50,000 characters.")
    if usage.document.valid:
        print(f"\nDocument usage: {usage.document.count} of {usage.document.limit}")        

    input("\nPress Enter key to select a file to translate to English.")
    input_path = askopenfilename(
        defaultextension="pdf",
        filetypes=[("PDF files", "*.pdf"), ("All Files", "*.*")],
    )
    if not input_path:
        return
    else:
        input_path = Path(input_path)
        print(f"Selected file: {input_path}")

    input("\nPress Enter key to select save location.")
    output_path = asksaveasfilename(
        defaultextension="pdf",
        filetypes=[("PDF files", "*.pdf"), ("All Files", "*.*")],
    )
    if not output_path:
        return
    else:
        output_path = Path(output_path)
        print(f"Selected save location: {output_path}")
    
    print("\nTranslating. This might take a few minutes...")
    try:
        deepl_client.translate_document_from_filepath(
            input_path,
            output_path,
            target_lang="EN-US",
            # formality="more"
        )
    except deepl.DocumentTranslationException as error:
        # If an error occurs during document translation after the document was
        # already uploaded, a DocumentTranslationException is raised. The
        # document_handle property contains the document handle that may be used to
        # later retrieve the document from the server, or contact DeepL support.
        doc_id = error.document_handle.id
        doc_key = error.document_handle.key
        print(f"Error after uploading ${error}, id: ${doc_id} key: ${doc_key}")
    except deepl.DeepLException as error:
        # Errors during upload raise a DeepLException
        print(error)
    input("Translation finished. Press Enter key to exit")
    print("Cleaning up...")

if __name__ == "__main__":
    main()
