# Useful Visual Studio Code Extensions

* Python
* Pylint
* Pylance
* Black Formatter
* Python Debugger

<br>

- Jupyter
- Codeium
- vscode-pdf
- Live Server
- Rainbow CSV
- Marp for VS Code -> Learn Markdown: [https://pandao.github.io/editor.md/en.html]

# Using Groq API

- https://groq.com
- https://pypi.org/project/groq

## References

- https://console.groq.com
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
- **For Jupyter:**
    - pip install -U ipywidgets

- pip install -U groq
- pip install -U python-dotenv

<br>

- pip list
- deactivate

## Create .env File (For Saving Passwords / API Keys / Access Tokens)

- Create a file:
    - .env
        - GROQ_API_KEY="..."

## Fix PyLint Warnings

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
