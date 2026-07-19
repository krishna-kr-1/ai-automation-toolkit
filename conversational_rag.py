from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_classic.chains import ConversationalRetrievalChain
from langchain_classic.memory import ConversationBufferWindowMemory
import os
from dotenv import load_dotenv
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

load_dotenv()
memory = ConversationBufferWindowMemory(k = 5, memory_key = "chat_history", output_key = "answer", return_messages = True)
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

qa_chain = ConversationalRetrievalChain.from_llm(
    llm=llm,
    retriever=retriever,
    memory=memory,
    verbose=True,
    condense_question_llm=llm,
    rephrase_question=False  # ← add this
)
while True:
    question = input("Enter Question/ quit : ")
    if question == "quit":
        break
    print(qa_chain.invoke(question))
