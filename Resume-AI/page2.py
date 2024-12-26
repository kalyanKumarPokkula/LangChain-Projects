import streamlit as st
import PyPDF2
from langchain_core.messages import AIMessage, HumanMessage
from llm import get_response_from_llm
from llama_parse import LlamaParse
import tempfile

def initialize_chat_history(session_state):
    if "chat_history" not in session_state:
        session_state.chat_history = [
            AIMessage(content="Hello!"),
        ]

def display_chat_history(session_state, st):
    for message in session_state.chat_history:
        if isinstance(message, AIMessage):
            with st.chat_message("AI"):
                st.markdown(message.content)
        elif isinstance(message, HumanMessage):
            with st.chat_message("Human"):
                st.markdown(message.content)

def handle_user_query(session_state, st, user_query, pdf_text):
    if user_query is not None and user_query.strip() != "":
        session_state.chat_history.append(HumanMessage(content=user_query))
        
        with st.chat_message("Human"):
            st.markdown(user_query)
        
        # Simulate AI response (In practice, you would call your AI model here)
        response = get_response_from_llm(pdf_text, user_query)
        
        with st.chat_message("AI"):
            st.markdown(response)
            
        session_state.chat_history.append(AIMessage(content=response))

def process_pdf(file):
    print(file)
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in range(len(reader.pages)):
        text += reader.pages[page].extract_text()
    return text

def process_pdf_with_llamaParser(file):
    print(file)
    document = LlamaParse(file)
    return document[0].text

def app():
    st.title("Chat With Your Own Resume")
    st.text("chat with your resume and get more insites, recomemendations and end less ways you can use!")

    uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])
    if st.button("Connect With LLM"):
        if uploaded_file is not None:
            pdf_text = process_pdf(uploaded_file)
            st.session_state.pdf_text = pdf_text
            st.sidebar.write("PDF Uploaded and Processed")
        else:
            st.sidebar.write("Please upload a PDF file")

    # Initialize chat history
    initialize_chat_history(st.session_state)

    # Display chat history
    display_chat_history(st.session_state, st)

    # User input
    user_query = st.chat_input("Type a message...")

    # Handle user query
    if 'pdf_text' in st.session_state:
        handle_user_query(st.session_state, st, user_query, st.session_state.pdf_text)
    else:
        st.write("Please upload a PDF file and click Connect.")
