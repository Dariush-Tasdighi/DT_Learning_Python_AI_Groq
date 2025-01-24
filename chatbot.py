# **************************************************
# import os
# from groq import Groq
# from dotenv import load_dotenv

# os.system(command="cls")

# print("Welcome to Dariush Tasdighi Chatbot!\n")

# load_dotenv()
# client = Groq()

# TEMPERATURE: float = 0.8
# MODEL_NAME: str = "llama-3.3-70b-versatile"

# messages = []

# SYSTEM_PROMPT: str = "You are a helpful assistant."
# system_message = {"role": "system", "content": SYSTEM_PROMPT}
# messages.append(system_message)

# while True:
#     print("-" * 50)
#     user_prompt: str = input("User: ")

#     if user_prompt.lower() in ["quit", "exit", "bye"]:
#         break

#     user_message = {"role": "user", "content": user_prompt}
#     messages.append(user_message)

#     chat_completion = client.chat.completions.create(
#         model=MODEL_NAME, messages=messages, temperature=TEMPERATURE
#     )

#     assistant_answer = chat_completion.choices[0].message.content

#     assistant_message = {"role": "assistant", "content": assistant_answer}
#     messages.append(assistant_message)

#     result = f"\nAI: {assistant_answer}"
#     print(result)
# **************************************************


# **************************************************
import os
import time
from groq import Groq
from dotenv import load_dotenv


def chat_completion(
    messages, model_name: str = "llama-3.1-8b-instant", temperature: float = 0.8
) -> str:
    """
    Chat Completion Function
    """

    load_dotenv()
    client = Groq()

    chat_completion = client.chat.completions.create(
        model=model_name, messages=messages, temperature=temperature
    )

    assistant_answer: str | None = chat_completion.choices[0].message.content

    if not assistant_answer:
        assistant_answer = "I'm sorry, I don't have an answer to that."

    return assistant_answer


def main():
    """
    Main Function
    """

    os.system(command="cls")

    print("Welcome to Dariush Tasdighi Chatbot!\n")

    TEMPERATURE: float = 0.8
    MODEL_NAME: str = "llama-3.3-70b-versatile"

    messages = []

    SYSTEM_PROMPT: str = "You are a helpful assistant."
    system_message = {"role": "system", "content": SYSTEM_PROMPT}
    messages.append(system_message)

    print("-" * 50)

    while True:
        user_prompt: str = input("User: ")

        if user_prompt.lower() in ["quit", "exit", "bye"]:
            break

        user_message = {"role": "user", "content": user_prompt}
        messages.append(user_message)

        start_time: float = time.time()

        assistant_answer: str = chat_completion(
            messages=messages, model_name=MODEL_NAME, temperature=TEMPERATURE
        )

        response_time: float = time.time() - start_time

        assistant_message = {"role": "assistant", "content": assistant_answer}
        messages.append(assistant_message)

        result = f"\nAI: {assistant_answer}"
        print(result)
        print("-" * 50)
        print(f"Full response received {response_time:.2f} seconds after request.")
        print("-" * 50)


if __name__ == "__main__":
    main()
# **************************************************
