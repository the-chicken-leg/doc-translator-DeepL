# doc-translator-DeepL

This Python script uses the DeepL API to translate a document.

## Usage

Run the main.py file (detailed instructions below) and follow the prompts to translate a document.

![powershell](screenshots/powershell.png)

## Run on Windows with uv

1. Install uv using PowerShell (see https://docs.astral.sh/uv/getting-started/installation/ for full instructions):

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

2. Verify uv installed correctly:

```powershell
uv --version
```

3. Navigate to your workspace directory. Below is an example, but you can use whichever directory you want:

```powershell
Set-Location C:\Users\micha\workspace\github.com\the-chicken-leg\
```

4. Clone github repository and navigate to directory:

```powershell
git clone https://github.com/the-chicken-leg/doc-translator-DeepL
```
```powershell
Set-Location .\doc-translator-DeepL\
```

5. Run using uv. On the first run, uv will download the appropriate python version, create a venv, and install dependencies, which might take some time. Subsequent runs will be faster:

```powershell
uv run main.py
```
