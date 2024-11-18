# Useful Visual Studio Extensions

* Python
* Pylint
* Pylance
* Black Formatter
* Python Debugger

<br>

- Codeium
- Jupyter
- vscode-pdf
- Live Server
- Rainbow CSV
- Marp for VS Code [https://pandao.github.io/editor.md/en.html]

# Using Groq API

- http://groq.com
- https://pypi.org/project/groq

## References

- https://console.groq.com/keys
- https://console.groq.com/login
- https://console.groq.com/settings
- https://console.groq.com/docs/models
- https://console.groq.com/docs/quickstart

## Setup Environment

- python -m venv .venv
- .\\.venv\Scripts\activate
- pip list
- python -m pip install -U pip
- pip install -U ipywidgets

<br>

- pip install -U groq
- pip install -U python-dotenv

<br>

- pip list
- deactivate

## Create .env File

- Create a file:
    - .env
        - GROQ_API_KEY="..."

## Fix PyLint Warning:

- Open the command palette: Press F1 [OR] CTRL + SHIFT + P
- Choose "Preference: Open Settins (JSON)"

```
{
    "security.workspace.trust.untrustedFiles": "open",
    "pylint.args": [
        "ignored-modules=cv2,streamlit,groq",
        "--extension-pkg-whitelist=cv2,pygame,numpy,streamlit,groq"
    ]
}
```
