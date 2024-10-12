import streamlit as st
import google.generativeai as genai

st.title("🐧 My Chatbot App")
st.subheader("Conversation")

#get Gemini api key
gemini_api_key = st.text_input("Gemini API Key: ", placeholder="Type your API Key here...", type="password")
# genai.configure(api_key=gemini_api_key)
# model = genai.GenerativeModel("gemini-pro")
# response = model.generate_content(user_input)
# bot_response = response.text


# Initialize session state for storing chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [] # Initialize with an empty list

# Display all chat messages
for message in st.session_state.chat_history:
    with st.chat_message("user"):
        st.markdown(message)

# Capture user input and append to chat history
if prompt := st.chat_input("Type your message here ..."):
    st.session_state.chat_history.append(prompt)
    st.chat_message("user").markdown(prompt)