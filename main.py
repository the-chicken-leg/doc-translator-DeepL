import os
from dotenv import load_dotenv
from pathlib import Path
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename

import deepl

def main():
    load_dotenv()
    api_key = os.environ.get("DEEPL_API_KEY")
    if api_key is None:
        raise RuntimeError("The API key was not found. Please check your .env file.")
    deepl_client = deepl.DeepLClient(api_key)

    # result = deepl_client.translate_text("Mein Arbeitgeber ist Scheiße!", target_lang="EN-US")
    # print(result.text)

    # Translate a formal document from English to German
    input_path = Path(askopenfilename(
        defaultextension="pdf",
        filetypes=[("PDF files", "*.pdf"), ("All Files", "*.*")],
    ))
    if not input_path:
        return
    output_path = Path(asksaveasfilename(
        defaultextension="pdf",
        filetypes=[("PDF files", "*.pdf"), ("All Files", "*.*")],
    ))
    if not output_path:
        return
    
    try:
        # Using translate_document_from_filepath() with file paths 
        deepl_client.translate_document_from_filepath(
            input_path,
            output_path,
            target_lang="EN-US",
            formality="more"
        )

        # Alternatively you can use translate_document() with file IO objects
        # with open(input_path, "rb") as in_file, open(output_path, "wb") as out_file:
        #     deepl_client.translate_document(
        #         in_file,
        #         out_file,
        #         target_lang="DE",
        #         formality="more"
        #     )

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

if __name__ == "__main__":
    main()
