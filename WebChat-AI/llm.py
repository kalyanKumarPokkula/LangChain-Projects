import os
import requests
from dotenv import load_dotenv
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_openai import ChatOpenAI
from langchain_core.runnables import RunnablePassthrough
from langchain import hub
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
# os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
# os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
# os.environ["LANGCHAIN_TRACING_V2"] = "true"


# load the data
def scrape_jina_ai(url):
    response = requests.get(f"https://r.jina.ai/{url}")
    return response.text

# split the data
def spliting_data(data):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=3000, chunk_overlap=1000)
    splits = text_splitter.split_text(data)
    return splits

# storing the data in vector store
def get_retriver_from_vectorStore(data_splits):
    vectorStore = Chroma.from_texts(texts=data_splits, embedding=OpenAIEmbeddings())
    retriver = vectorStore.as_retriever(search_type="similarity", search_kwarge={"k": 12})
    return retriver

# formating the output
def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)


# invoking the llm for the response
def get_response_from_llm(site_url, question):
    result = scrape_jina_ai(site_url)
    text_splits = spliting_data(result)
    prompt = hub.pull("rlm/rag-prompt")
    # creating the llm
    llm = ChatOpenAI()
    
    rag_chain = (
        {"context": get_retriver_from_vectorStore(text_splits) | format_docs, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )

    result = rag_chain.invoke(question)  
    return result