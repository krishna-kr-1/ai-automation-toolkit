from langchain_classic.memory import ConversationBufferMemory
from langchain_classic.chains import ConversationChain
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os


load_dotenv()
api_key = os.getenv("google_api_key")
memory = ConversationBufferMemory()
llm = ChatGoogleGenerativeAI(model = "gemini-2.5-flash", google_api_key = api_key)

chain = ConversationChain(llm = llm, memory=memory, verbose=True)

while True:
    user_input = input("You :")
    if user_input == "quit":
        break
    response = chain.invoke({"input":user_input})
    print("AI : ", response["response"])

print(memory.buffer)
