# **************************************************
from groq import Groq

api_key = "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"

client = Groq(api_key=api_key)
# **************************************************


# **************************************************
# Solution (1)
# **************************************************
# import os
# from dotenv import load_dotenv

# load_dotenv()

# api_key = os.getenv(key="GROQ_API_KEY")
# print("API Key:", api_key)

# password = os.getenv(key="Password")
# print("Password:", password)
# **************************************************


# **************************************************
# Solution (2)
# **************************************************
# import os
# from dotenv import load_dotenv

# load_dotenv()

# api_key = os.environ.get(key="GROQ_API_KEY")
# print("API Key:", api_key)

# password = os.environ.get(key="Password")
# print("Password:", password)
# **************************************************


# **************************************************
# Solution (3)
# **************************************************
# import os
# from dotenv import load_dotenv

# load_dotenv(dotenv_path=".envTemp")

# api_key = os.environ.get(key="GROQ_API_KEY")
# print("API Key:", api_key)

# password = os.environ.get(key="Password")
# print("Password:", password)
# **************************************************


# **************************************************
# Best Practice
# **************************************************
# import os
# from dotenv import load_dotenv

# os.system(command="cls")

# load_dotenv()

# API_KEY_NAME: str = "GOOGOOLI"
# # API_KEY_NAME: str = "GROQ_API_KEY"

# api_key: str | None = os.getenv(key=API_KEY_NAME)

# if api_key is None:
#     print("API Key not found!")
#     exit()

# print("API Key:", api_key)
# **************************************************
