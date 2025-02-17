# **************************************************
# Simple and Basic Sample (From Groq Documentation)
# **************************************************
from groq import Groq

api_key = "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"

client = Groq(api_key=api_key)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Tell me a joke.",
            # "content": "Explain the importance of fast language models",
        }
    ],
    model="llama-3.3-70b-versatile",
)

print(chat_completion.choices[0].message.content)
# **************************************************


# **************************************************
# Best Practice For Using API Key
# **************************************************
# import os
# from groq import Groq
# from dotenv import load_dotenv

# # os.system("cls")
# os.system(command="cls")

# # ********************
# # *** Solution (1) ***
# # ********************
# api_key = "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"  # Bad Practice
# client = Groq(api_key=api_key)
# # ********************

# # ********************
# # *** Solution (2) ***
# # ********************
# # نکته مهم
# # باید دستور ذیل نوشته شود
# # هر چند که بر خلاف دستورات آتی
# # مستقیما از آن استفاده نمی‌شود
# # ********************
# load_dotenv()
# # OR
# # load_dotenv(dotenv_path=".envTemp")

# api_key = os.getenv(key="GROQ_API_KEY")
# print(api_key)

# api_key = os.environ.get(key="GROQ_API_KEY")
# print(api_key)

# client = Groq(api_key=api_key)
# # ********************

# # ********************
# # *** Solution (3) ***
# # ********************
# load_dotenv()
# client = Groq()
# **************************************************


# **************************************************
# استراتژی انتخاب مدل
# **************************************************
MODEL_NAME: str = "llama-3.1-8b-instant"
# MODEL_NAME: str = "llama-3.3-70b-versatile"
# **************************************************


# **************************************************
# import os
# from groq import Groq
# from pprint import pprint
# from dotenv import load_dotenv

# os.system(command="cls")

# load_dotenv()
# client = Groq()

# # وقتی نام پارامتر را می‌نویسیم، ترتیب نوشتن
# # پارامترها مهم نیست و من معمولا به ترتیب قد می‌نویسیم
# chat_completion = client.chat.completions.create(
#     model=MODEL_NAME,
#     messages=[
#         {
#             "role": "user",
#             "content": "Tell me a joke.",
#         }
#     ],
# )

# print("-" * 50)
# print("type of chat_completion:", type(chat_completion))
# print("-" * 50)
# print(chat_completion)
# print("-" * 50)
# print(chat_completion.choices[0].message.content)
# print("-" * 50)
# pprint(chat_completion.choices[0].message.content)
# print("-" * 50)
# **************************************************


# **************************************************
# ChatCompletion Object
# **************************************************
# ChatCompletion(
# 	id='chatcmpl-e56f6098-fc74-43cb-81a4-e8cf6589eee7',
# 	choices=[
# 		Choice(
# 			finish_reason='stop',
# 			index=0,
# 			logprobs=None,
# 			message=ChatCompletionMessage(
# 				content='A man walked into a library...',
# 				role='assistant',
# 				function_call=None,
# 				tool_calls=None
# 			)
# 		)
# 	],
# 	created=1733050351,
# 	model='llama-3.1-8b-instant',
# 	object='chat.completion',
# 	system_fingerprint='fp_9cb648b966',
# 	usage=CompletionUsage(
# 		completion_tokens=55,
# 		prompt_tokens=40,
# 		total_tokens=95,
# 		completion_time=0.073333333,
# 		prompt_time=0.00427855,
# 		queue_time=0.011420940000000001,
# 		total_time=0.077611883
# 	),
# 	x_groq={'id': 'req_01je0xkg1qfch89pe8y3nrre3p'}
# )
# **************************************************


# **************************************************
# یادآوری: هوش مصنوعی قابلیت حل مساله دارد
# **************************************************
# import os
# from groq import Groq
# from dotenv import load_dotenv

# os.system(command="cls")

# load_dotenv()
# client = Groq()

# chat_completion = client.chat.completions.create(
#     model=MODEL_NAME,
#     messages=[
#         {
#             "role": "user",
#             # "content": "Tell me a joke.",
#             "content": "What is result of 2 + 2?",
#             # "content": "محمد دو تا برادر دارد به نام های علی و اکبر، و اکبر هم یک خواهر دارد به نام سارا، و همه آن‌ها با هم با پدر و مادرشان زندگی می‌کنند. به من بگو در این خانواده چند نفر زندگی می‌کنند.",
#         }
#     ],
# )

# assistant_answer = chat_completion.choices[0].message.content
# print("-" * 50)
# print(assistant_answer)
# print("-" * 50)
# **************************************************


# **************************************************
# Get Response with Stream
# **************************************************
# import os
# from groq import Groq
# from dotenv import load_dotenv

# os.system(command="cls")

# load_dotenv()
# client = Groq()

# chat_completion_stream = client.chat.completions.create(
#     stream=True,
#     model=MODEL_NAME,
#     messages=[
#         {
#             "role": "user",
#             "content": "Explain the importance of fast language models",
#         }
#     ],
# )

# for chunk in chat_completion_stream:
#     print(chunk.choices[0].delta.content, end="")
# **************************************************


# **************************************************
# Get Response Time
# **************************************************
# import os
# import time
# from groq import Groq
# from dotenv import load_dotenv

# os.system(command="cls")

# load_dotenv()
# client = Groq()

# start_time: float = time.time()

# chat_completion = client.chat.completions.create(
#     stream=False,
#     model=MODEL_NAME,
#     messages=[
#         {
#             "role": "user",
#             "content": "Explain the importance of fast language models",
#         }
#     ],
# )

# response_time: float = time.time() - start_time

# assistant_answer = chat_completion.choices[0].message.content

# print("-" * 50)
# print(assistant_answer)
# print("-" * 50)
# print(f"Full response received {response_time:.2f} seconds after request.")
# print("-" * 50)
# **************************************************


# **************************************************
# Simple Text Chatbot without History
# **************************************************
# import os
# from groq import Groq
# from dotenv import load_dotenv

# os.system(command="cls")

# print("Welcome to Dariush Tasdighi Chatbot!\n")

# load_dotenv()
# client = Groq()

# while True:
#     print("-" * 50)
#     user_prompt: str = input("User: ")

#     if user_prompt.lower() in ["quit", "exit", "bye"]:
#         break

#     messages = []
#     user_message = {"role": "user", "content": user_prompt}
#     messages.append(user_message)

#     # chat_completion = client.chat.completions.create(
#     #     stream=False, model=MODEL_NAME, messages=messages
#     # )

#     chat_completion = client.chat.completions.create(
#         stream=False,
#         model=MODEL_NAME,
#         messages=messages,
#     )

#     assistant_answer = chat_completion.choices[0].message.content

#     result: str = f"\nAI: {assistant_answer}"
#     print(result)
#     print("-" * 50)
#     print()
# **************************************************


# **************************************************
# Chatbot with System Role without History
# **************************************************
# import os
# from groq import Groq
# from dotenv import load_dotenv

# os.system(command="cls")

# print("Welcome to Dariush Tasdighi Chatbot!\n")

# load_dotenv()
# client = Groq()

# while True:
#     print("-" * 50)
#     user_prompt: str = input("User: ")

#     if user_prompt.lower() in ["quit", "exit", "bye"]:
#         break

#     messages = []

#     system_prompt: str = "You are a helpful assistant."
#     system_message = {"role": "system", "content": system_prompt}

#     user_message = {"role": "user", "content": user_prompt}

#     # نکته مهم: ترتیب نوشتن پیغام‌ها و نقش‌ها بسیار اهمیت دارد
#     messages.append(system_message)
#     messages.append(user_message)

#     chat_completion = client.chat.completions.create(
#         stream=False,
#         model=MODEL_NAME,
#         messages=messages,
#     )

#     assistant_answer: str | None = chat_completion.choices[0].message.content

#     result: str = f"\nAI: {assistant_answer}"
#     print(result)
#     print("-" * 50)
#     print()
# **************************************************


# **************************************************
# Chatbot with History & Temperature!
# **************************************************
# import os
# from groq import Groq
# from dotenv import load_dotenv

# os.system(command="cls")

# print("Welcome to Dariush Tasdighi Chatbot!\n")

# load_dotenv()
# client = Groq()

# # 0 <= temperature <= 2
# # temperature -> 0 => Consistency -> 100
# # temperature -> 1 => Creativity  -> 100
# TEMPERATURE: float = 0.8

# messages = []

# system_prompt: str = "You are a helpful assistant."
# system_message = {"role": "system", "content": system_prompt}
# messages.append(system_message)

# while True:
#     print("-" * 50)
#     user_prompt: str = input("User: ")

#     if user_prompt.lower() in ["quit", "exit", "bye"]:
#         break

#     user_message = {"role": "user", "content": user_prompt}
#     messages.append(user_message)

#     chat_completion = client.chat.completions.create(
#         stream=False,
#         model=MODEL_NAME,
#         messages=messages,
#         temperature=TEMPERATURE,
#     )

#     assistant_answer: str | None = chat_completion.choices[0].message.content

#     assistant_message = {"role": "assistant", "content": assistant_answer}
#     messages.append(assistant_message)

#     result: str = f"\nAI: {assistant_answer}"
#     print(result)
#     print("-" * 50)
#     print()
# **************************************************


# **************************************************
# Agent: Translator Assistant Chatbot without! History & without! Temperature!
# **************************************************
# import os
# from groq import Groq
# from dotenv import load_dotenv

# os.system(command="cls")

# print("Welcome to Dariush Tasdighi Dictionary Chatbot!\n")

# load_dotenv()
# client = Groq()

# TEMPERATURE: float = 0.0  # Note

# # system_prompt: str = """You are a useful assistant."""

# system_prompt: str = """You are a translator assistant from english language to persian (Farsi) language.
# If user write just one english word, you must just translate this word to persian (Farsi) language.
# after of this translation, you must not translate anything and your answers must be just in english language.
# You must write the pronounciation of user english word.
# You must write the type of user english word, for example: noun, verb and so on.
# You must write 5 synonyms for user english word.
# you must write 2 antonyms for user english word.
# you must write 2 short sentences that has the user english word."""

# while True:
#     print("-" * 50)
#     user_prompt: str = input("User: ")

#     if user_prompt.lower() in ["quit", "exit", "bye"]:
#         break

#     messages = []

#     system_message = {"role": "system", "content": system_prompt}
#     messages.append(system_message)

#     user_message = {"role": "user", "content": user_prompt}
#     messages.append(user_message)

#     chat_completion = client.chat.completions.create(
#         stream=False,
#         model=MODEL_NAME,
#         messages=messages,
#         temperature=TEMPERATURE,
#     )

#     assistant_answer: str | None = chat_completion.choices[0].message.content

#     result: str = f"\nAI: {assistant_answer}"
#     print(result)
#     print("-" * 50)
#     print()
# **************************************************
