# doc-translator-DeepL

This Python script uses the DeepL API to translate a document.

## Usage

Run the main.py file (detailed instructions below) and follow the prompts to translate a document.

![powershell](screenshots/powershell.png)

## Run on Windows with uv

1. Install uv: https://docs.astral.sh/uv/getting-started/installation/#__tabbed_1_2

2. Verify uv installed correctly:

```powershell
uv --version
```

3. Download script file

```powershell
curl -L -O https://github.com/the-chicken-leg/doc-translator-DeepL/blob/main/doc-translator-DeepL.py?raw=true
```

5. Run using uv. On the first run, uv will download the appropriate python version, create a venv, and install dependencies, which might take some time. Subsequent runs will be faster:

```powershell
uv run .\doc-translator-DeepL.py
```
