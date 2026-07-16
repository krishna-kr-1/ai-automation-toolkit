from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_classic.chains import RetrievalQA
import os
from dotenv import load_dotenv
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

load_dotenv()

llm = ChatGoogleGenerativeAI(model = "gemini-2.5-flash", google_api_key = os.getenv("google_api_key"))
textsplitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
embedding = GoogleGenerativeAIEmbeddings(model = "gemini-embedding-001", google_api_key = os.getenv("google_api_key"))

filename = input("Enter PDF full path : ")
print(filename)

pdf = PyPDFLoader(filename)

pages = pdf.load()

chunks = textsplitter.split_documents(pages)

index_path = os.path.splitext(os.path.basename(filename))[0]

if os.path.exists(index_path):
    vector_store = FAISS.load_local(index_path, embedding, 
                  allow_dangerous_deserialization=True)
else:
    vector_store = FAISS.from_documents(chunks, embedding)
    vector_store.save_local(index_path)

retriever = vector_store.as_retriever()
qa_chain = RetrievalQA.from_chain_type(llm= llm, retriever = retriever)
while True:
    question = input("Enter Question/ quit : ")
    if question == "quit":
        break
    print(qa_chain.invoke(question))

