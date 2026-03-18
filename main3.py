import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama
import streamlit as st

load_dotenv()

file_path = 'sachin.txt'
information_sachin = ""
try:
    with open(file_path, 'r', encoding='utf-8') as file:
        information_sachin = file.read()
except FileNotFoundError:
    print("The file was not found.")
except Exception as e:
    print(f"An error occurred: {e}")
#print(information_sachin)

summary_template_sachin = f"""
        given the information {information_sachin} about a person I want you to create:
        1. A short summary
        2. two interesting facts about them
"""
USER = "user"
ASSISTANT = "assistant"
st.chat_message(USER).write(summary_template_sachin)

prompt_template_sachin = PromptTemplate(input_variables=["information_sachin"], template=summary_template_sachin)

llm_sachin = ChatOllama(model="gemma3:270m", temperature=0)

chain_sachin = prompt_template_sachin | llm_sachin

response_sachin = chain_sachin.invoke({"information_sachin": information_sachin})

#print(response_sachin)
#print(response_sachin.content)
with open("summary_output_sachin.txt", "w") as file:
    file.write(response_sachin.content)
st.chat_message(ASSISTANT).write(response_sachin.content)

# To run: streamlit run main3.py

# https://bijukunjummen.medium.com/chat-application-using-streamlit-and-text-bison-05024f939827
