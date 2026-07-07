from langchain_classic.memory import ConversationBufferWindowMemory
from langchain_classic.chains import ConversationChain
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv

load_dotenv()

memory = ConversationBufferWindowMemory(k = 3)

llm = ChatGoogleGenerativeAI(model = "gemini-2.5-flash", google_api_key = os.getenv("google_api_key"))

chain = ConversationChain(llm = llm, memory=memory, verbose=True)

while True:
    user = input("User :")
    if (user == "quit"):
        break
    response = chain.invoke({"input" : user})
    print(response["response"])
    
