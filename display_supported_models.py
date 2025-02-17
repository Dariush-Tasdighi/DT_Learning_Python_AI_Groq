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

# # print("-" * 50)
# # print(models)

# print("-" * 50)
# list = models.list()
# print("Type of list:", type(list))

# # print("-" * 50)
# # print(list)

# print("-" * 50)
# data = list.data
# print("Type of list:", type(data))

# # print("-" * 50)
# # print(data)

# # print("-" * 50)
# # for model in data:
# #     print(model)

# # print("-" * 50)
# # for model in data:
# #     print(model.id)

# # new_data = []
# # for model in data:
# #     new_data.append(model.id)

# new_data = [model.id for model in data]
# new_data.sort()

# print("-" * 50)
# for model in new_data:
#     print(model)
# print("-" * 50)
# **************************************************


# **************************************************
# Get Groq Models List
# **************************************************
import os
from groq import Groq
from dotenv import load_dotenv

os.system(command="cls")

load_dotenv()
client = Groq()

data = client.models.list().data

new_data = [model.id for model in data]
new_data.sort()

print("-" * 50)
for model in new_data:
    print(model)
print("-" * 50)
# **************************************************
