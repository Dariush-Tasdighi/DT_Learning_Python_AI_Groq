# Using Groq API

- https://groq.com
- https://pypi.org/project/groq
- https://pypi.org/project/python-dotenv

## Notes

- llama 3.3
    - 70b -> Online
- llama 3.2
    - 1b
    - 3b
- llama 3.1
    - 8b -> Offline
    - 70b
    - 405b

## References

- https://console.groq.com
- https://console.groq.com/keys
- https://console.groq.com/login
- https://console.groq.com/settings
- https://console.groq.com/docs/models
- https://console.groq.com/docs/text-chat
- https://console.groq.com/docs/quickstart

## Setup Environment

- python -m venv .venv
- .\\.venv\Scripts\activate
- pip list
- python -m pip install -U pip
- python -m pip install -U groq
- python -m pip install -U streamlit
- python -m pip install -U python-dotenv
- pip list

Write / Edit / Run the Source Code(s)!

- deactivate

## Create .env File (For Saving Passwords / API Keys / Access Tokens / ...)

- In the root of project, create a file, with the name of '.env', and write key name(s) and value:
    - GROQ_API_KEY="..."
