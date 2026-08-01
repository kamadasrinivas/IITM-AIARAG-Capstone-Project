# IITM-AIARAG-Capstone-Project
RAG System

## Setup

Create and activate your virtual environment, then install dependencies:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

`requirements.txt` already includes:

```text
openai
python-dotenv
```

## Run the script

Use the active virtual environment when running the script:

```powershell
.\.venv\Scripts\Activate.ps1
python .\IITM-AIARAG-Capstone-Project\hello_llm.py "what is rag agent"
```

If `python` is not recognized, use the full Python executable path from the venv:

```powershell
C:\SRINI\WORKSPACE\IITM\.venv\Scripts\python.exe .\IITM-AIARAG-Capstone-Project\hello_llm.py "what is rag agent"
```
