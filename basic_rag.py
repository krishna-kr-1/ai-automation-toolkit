from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_community.vectorstores import FAISS
from langchain_classic.chains import RetrievalQA
from langchain_text_splitters import RecursiveCharacterTextSplitter
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatGoogleGenerativeAI(model = "gemini-2.5-flash", google_api_key = os.getenv("google_api_key"))
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)

def get_text(filename):
    with open(filename, "r") as f:
        return "".join(f.readlines())

large_document = get_text(r"C:\Users\krish\AI Automation Engineer\sample.txt")
chunks = text_splitter.split_text(large_document)

embeddings = GoogleGenerativeAIEmbeddings(model = "gemini-embedding-001", google_api_key = os.getenv("google_api_key"))
vector_store = FAISS.from_texts(chunks, embeddings)

retriever = vector_store.as_retriever()
qa_chain = RetrievalQA.from_chain_type(llm = llm, retriever = retriever)

while True:
    question = input("Ask a question (or quit) : ")
    if question == "quit":
        break
    print(qa_chain.invoke(question))
