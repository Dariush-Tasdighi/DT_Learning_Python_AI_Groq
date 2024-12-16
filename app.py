# **************************************************
model_name = "llama-3.1-8b-instant"
# model_name = "llama-3.3-70b-versatile"
# **************************************************

# **************************************************
import os
from groq import Groq
from pprint import pprint
from dotenv import load_dotenv

os.system(command="cls")

# ********************
# *** Solution (1) ***
# ********************
# api_key = "abcde12345..."  # Bad Practice
# client = Groq(api_key=api_key)
# ********************

# ********************
# *** Solution (2) ***
# ********************
# نکته مهم
# باید دستور ذیل نوشته شود
# هر چند که بر خلاف دستورات آتی
# مستقیما از آن استفاده نمی‌شود
# ********************
# load_dotenv()

# api_key = os.getenv(key="GROQ_API_KEY")
# # print(api_key)
# api_key = os.environ.get(key="GROQ_API_KEY")
# # print(api_key)

# client = Groq(api_key=api_key)
# ********************

# ********************
# *** Solution (3) ***
# ********************
load_dotenv()
client = Groq()
# ********************

chat_completion = client.chat.completions.create(
    model=model_name,
    messages=[
        {
            "role": "user",
            "content": "Tell me a joke.",
        }
    ],
)

print("-" * 50)
print("type of chat_completion:", type(chat_completion))
print("-" * 50)
print(chat_completion)
print("-" * 50)
pprint(chat_completion)
print("-" * 50)
# **************************************************

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
# import os
# from groq import Groq
# from dotenv import load_dotenv

# os.system(command="cls")

# load_dotenv()
# client = Groq()

# chat_completion = client.chat.completions.create(
#     model=model_name,
#     messages=[
#         {
#             "role": "user",
#             "content": "Tell me a joke.",
#             # "content": "What is result of 2 + 2?",
#         }
#     ],
# )

# response = chat_completion.choices[0].message.content
# print("-" * 50)
# print(response)
# print("-" * 50)
# **************************************************

# **************************************************
# Chatbot
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
#     prompt = input("User: ")

#     if prompt.lower() in ["quit", "exit"]:
#         break

#     message_user = {"role": "user", "content": prompt}

#     messages = [message_user]

#     chat_completion = client.chat.completions.create(
#         model=model_name, messages=messages
#     )

#     response = chat_completion.choices[0].message.content

#     result = f"\nAI: {response}"
#     print(result)
# **************************************************

# **************************************************
# Chatbot with System Role
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
#     prompt = input("User: ")

#     if prompt.lower() in ["quit", "exit"]:
#         break

#     message_user = {"role": "user", "content": prompt}
#     message_system = {"role": "system", "content": "you are a helpful assistant."}

#     # نکته مهم: ترتیب نوشتن پیغام‌ها و نقش‌ها اهمیت دارد
#     messages = [message_system, message_user]

#     chat_completion = client.chat.completions.create(
#         model=model_name, messages=messages
#     )

#     response = chat_completion.choices[0].message.content

#     result = f"\nAI: {response}"
#     print(result)
# **************************************************

# **************************************************
# Chatbot with History & Temperature!
# **************************************************
# import os
# from groq import Groq
# from dotenv import load_dotenv

# os.system(command="cls")

# print("Welcome to Dariush Tasdighi Chatbot!\n")

# # temperature -> 0 => Consistency -> 100
# # temperature -> 1 => Creativity  -> 100
# temperature = 0.5

# messages = []
# message_system = {"role": "system", "content": "you are a helpful assistant."}
# messages.append(message_system)

# load_dotenv()
# client = Groq()

# while True:
#     print("-" * 50)
#     prompt = input("User: ")

#     if prompt.lower() in ["quit", "exit"]:
#         break

#     message_user = {"role": "user", "content": prompt}
#     messages.append(message_user)

#     chat_completion = client.chat.completions.create(
#         model=model_name, messages=messages, temperature=temperature
#     )

#     response = chat_completion.choices[0].message.content

#     message_assistant = {"role": "assistant", "content": response}
#     messages.append(message_assistant)

#     result = f"\nAI: {response}"
#     print(result)
# **************************************************

# **************************************************
# Agent: Translator Assistant Chatbot without! History & without! Temperature!
# **************************************************
# import os
# from groq import Groq
# from dotenv import load_dotenv

# os.system(command="cls")

# print("Welcome to Dariush Tasdighi Chatbot!\n")

# temperature = 0.0 # Note

# message_system = {"role": "system", "content": """You are a translator assistant from english language to persian (Farsi) language.
# If user write just one english word, you must just translate this word to persian language.
# after of this translation, you must not translate anything and your answers must be just in english language.
# You must write the pronounciation of user english word.
# You must write the type of user english word, for example: noun, verb and so on.
# You must write 5 synonyms for user english word.
# you must write 2 antonyms for user english word.
# you must write 2 short sentences that has the user english word."""}

# while True:
#     print("-" * 50)
#     prompt = input("User: ")

#     if prompt.lower() in ["quit", "exit"]:
#         break

#     load_dotenv()
#     client = Groq()

#     messages = []
#     messages.append(message_system)

#     message_user = {"role": "user", "content": prompt}
#     messages.append(message_user)

#     chat_completion = client.chat.completions.create(
#         model=model_name, messages=messages, temperature=temperature
#     )

#     response = chat_completion.choices[0].message.content

#     result = f"\nAI: {response}"
#     print(result)
# **************************************************

# **************************************************
# Get Groq Models List
# **************************************************
# import os
# from groq import Groq
# from dotenv import load_dotenv

# os.system(command="cls")

# load_dotenv()
# client = Groq()

# print("-" * 50)
# models = client.models
# print("Type of models:", type(models))

# print("-" * 50)
# list = models.list()
# print("Type of list:", type(list))

# print("-" * 50)
# data = list.data
# print("Type of list:", type(data))

# # print("-" * 50)
# # print(models)

# # print("-" * 50)
# # print(list)

# # print("-" * 50)
# # print(data)

# # print("-" * 50)
# # for model in data:
# #     print(model)

# print("-" * 50)
# # new_data = []
# # for model in data:
# #     new_data.append(model.id)

# new_data = [model.id for model in data]

# new_data.sort()
# for model in new_data:
#     print(model)

# print("-" * 50)
# **************************************************
