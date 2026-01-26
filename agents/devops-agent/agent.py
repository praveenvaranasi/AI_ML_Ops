from dotenv import load_dotenv
import os
import streamlit as sl

load_dotenv()

print(os.getenv("greet"))

sl.title("Devops Agent")
sl.header("Let me help you with your devops tasks")
sl.chat_input("Ask me anything")
