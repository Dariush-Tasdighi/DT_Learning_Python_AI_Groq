# **************************************************
# import re

# text = "Hello, world! This is a test. Let's split this string.Do you have fun?"

# pattern = r"[ ,.!?]+"

# parts = re.split(pattern=pattern, string=text)

# for part in parts:
#     print(part)
# **************************************************

# **************************************************
# pathfile: str = "./files/sample.txt"

# file = open(file=pathfile, mode="rt", encoding="utf-8")
# file_content: str = file.read()
# file.close()

# print(file_content)
# **************************************************

# **************************************************
# pathfile: str = "./files/sample.txt"

# with open(file=pathfile, mode="rt", encoding="utf-8") as file:
#     file_content: str = file.read()
#     file.close()

# print(file_content)
# **************************************************

# **************************************************
# import os


# def read_text_file(pathfile: str) -> str:
#     with open(file=pathfile, mode="rt", encoding="utf-8") as file:
#         result: str = file.read()
#         file.close()

#     return result


# os.system(command="cls")

# pathfile: str = "./files/sample.txt"

# file_content: str = read_text_file(pathfile=pathfile)
# print(file_content)
# **************************************************

# **************************************************
# import os
# import re


# def read_text_file(pathfile: str) -> str:
#     with open(file=pathfile, mode="rt", encoding="utf-8") as file:
#         result: str = file.read()
#         file.close()

#     return result


# def normalize_text(text: str) -> str:
#     result: str = text

#     while "  " in result:
#         result = result.replace("  ", " ")

#     result = result.replace("\n", "")
#     result = result.replace("\r", "")

#     return result


# def get_sentences(text: str) -> list[str]:
#     pattern = r"[.!?]+"

#     parts = re.split(pattern=pattern, string=text)

#     sentences: list[str] = []

#     for part in parts:
#         if not part:
#             continue

#         part = part.strip()

#         if not part:
#             continue

#         sentences.append(part)

#     return sentences


# os.system(command="cls")

# pathfile: str = "./files/sample.txt"

# file_content: str = read_text_file(pathfile=pathfile)
# file_content = normalize_text(text=file_content)
# sentences: list[str] = get_sentences(text=file_content)

# print("-" * 50)
# for sentence in sentences:
#     message = f"[{sentence}]"
#     print(message)
#     print("-" * 50)
# **************************************************

# **************************************************
# import os

# # import translator_functions
# import translator_functions as functions

# os.system(command="cls")

# pathfile: str = "./files/sample.txt"

# file_content: str = functions.read_text_file(pathfile=pathfile)
# file_content = functions.normalize_text(text=file_content)
# sentences: list[str] = functions.get_sentences(text=file_content)

# print("-" * 50)
# for sentence in sentences:
#     message = f"[{sentence}]"
#     print(message)
#     print("-" * 50)
# **************************************************

# **************************************************
import os
import translator_functions as functions


def main() -> None:
    os.system(command="cls")

    source_pathfile: str = "./files/sample.txt"
    target_pathfile: str = "./files/translated.txt"

    file_content: str = functions.read_text_file(pathfile=source_pathfile)
    file_content = functions.normalize_text(text=file_content)
    paragraphs: list[str] = functions.get_paragraphs(text=file_content)

    with open(file=target_pathfile, mode="wt", encoding="utf-8") as file:
        for paragraph in paragraphs:
            translated: str = functions.translate(text=paragraph)
            file.write(translated)
            file.write("\n\n")

    print("Translation Completed...")


if __name__ == "__main__":
    main()
# **************************************************
