from dotenv import load_dotenv
import streamlit as st
from langchain_community.llms import GoogleLAMDA
import google.generativeai as ggi
import os

load_dotenv(".env")

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
# ggi.configure(api_key = GOOGLE_API_KEY)

# Initialize LangChain LLM client with your API key
llm = GoogleLAMDA(api_key=GOOGLE_API_KEY)

# Conversation history (list of strings)
chat_history = []


def update_chat_history(user_input, response):
  """Updates conversation history with user input and response"""
  chat_history.append(user_input)
  chat_history.append(response)

def generate_response(user_input):
  """Sends user input to Gemini with context and retrieves response"""
  context = "\n".join(chat_history[-2:])  # Get last two messages for context
  prompt = f"You: {user_input}\nContext: {context}"
  response = llm.text_generation(prompt=prompt)["text"]
  update_chat_history(user_input, response)
  return response

st.title("Gemini Chatbot")

# Text input field for user
user_input = st.text_input("You:")

# Generate response if user input is provided
if user_input:
  response = generate_response(user_input)
  st.write(f"Bot: {response}")

