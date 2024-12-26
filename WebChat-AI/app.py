import streamlit as st
from ui import initialize_chat_history, display_chat_history, handle_user_query

st.set_page_config(page_title="Chat with WebSites", page_icon=":speech_balloon")
st.title("Chat with WebSites")

# Sidebar for additional context input and connect button
with st.sidebar:
    additional_context = st.text_input("URl you want to scrape")
    if st.button("Add"):
        st.session_state.additional_context = additional_context
        st.sidebar.write(f"Connected with context: {additional_context}")

# Initialize chat history
initialize_chat_history(st.session_state)

# Display chat history
display_chat_history(st.session_state, st)

# User input
user_query = st.chat_input("Type a message...")

# Handle user query
if 'additional_context' in st.session_state:
    handle_user_query(st.session_state, st, user_query, st.session_state.additional_context)
else:
    st.write("Please provide URL of the website you want to know and press on Add button.")