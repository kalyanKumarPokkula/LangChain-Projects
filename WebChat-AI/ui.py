# import streamlit as st
# from langchain_core.messages import AIMessage, HumanMessage


# st.set_page_config(page_title="Chat with WebSites", page_icon=":speech_ballon")
# st.title("Chat with WebSites")

# if "chat_history" not in st.session_state:
#     st.session_state.chat_history = [
#       AIMessage(content="Hello!"),
#     ]


# for message in st.session_state.chat_history:
#     if isinstance(message, AIMessage):
#         with st.chat_message("AI"):
#             st.markdown(message.content)
#     elif isinstance(message, HumanMessage):
#         with st.chat_message("Human"):
#             st.markdown(message.content)


# user_query = st.chat_input("Type a message...")

# if user_query is not None and user_query.strip() != "":
#     st.session_state.chat_history.append(HumanMessage(content=user_query))
    
#     with st.chat_message("Human"):
#         st.markdown(user_query)
        
#     with st.chat_message("AI"):
#         response = "Hi how can i help you?"
#         st.markdown(response)
        
#     st.session_state.chat_history.append(AIMessage(content=response))

from langchain_core.messages import AIMessage, HumanMessage
from llm import get_response_from_llm

def initialize_chat_history(session_state):
    if "chat_history" not in session_state:
        session_state.chat_history = [
            AIMessage(content="Hello! Please ask me any queries you have i will answer them based the context i have."),
        ]

def display_chat_history(session_state, st):
    for message in session_state.chat_history:
        if isinstance(message, AIMessage):
            with st.chat_message("AI"):
                st.markdown(message.content)
        elif isinstance(message, HumanMessage):
            with st.chat_message("Human"):
                st.markdown(message.content)

def handle_user_query(session_state, st, user_query, additional_context):
    if user_query is not None and user_query.strip() != "":
        session_state.chat_history.append(HumanMessage(content=user_query))
        
        with st.chat_message("Human"):
            st.markdown(user_query)
        
        # Simulate AI response (In practice, you would call your AI model here)
        response = get_response_from_llm(additional_context, user_query)
        
        with st.chat_message("AI"):
            st.markdown(response)
            
        session_state.chat_history.append(AIMessage(content=response))