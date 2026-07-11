import os
from dotenv import  load_dotenv
from langchain_core.tools import Tool
from langchain_classic.agents import initialize_agent
from langchain_classic.memory import ConversationBufferWindowMemory
from langchain_classic.agents.agent_types import AgentType
from  langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

llm = ChatGoogleGenerativeAI(model = "gemini-2.5-flash", google_api_key = os.getenv("google_api_key"))

memory = ConversationBufferWindowMemory(k = 5, memory_key = "chat_history", return_messages = True)

def calculator(input_string):
    a, b, sign = input_string.strip().split(",")
    a = int(a.strip())
    b = int(b.strip())
    sign = sign.strip()

    if sign == "+":
        return a+b
    elif sign == "-":
        return a-b
    elif sign == "*":
        return a*b
    elif sign == "/":
        return a/b
    else:
        return None

def word_counter(input_string):
    return len(input_string.split())

def rev_sen(input_string):
    return input_string[::-1]

tools = [
    Tool(
        name = "calculator",
        description = "This is a tool which is used to calculate the mathemitical calculation between two numbers for +, -, *, /. This take input as a single string and the input format as a num1, num2, operand",
        func = calculator
    ),
    Tool(
        name = "reverse_a_sentence",
        description = "This is a tool which is used to revese a sentence. This take input as a single string ",
        func = rev_sen
    ),
    Tool(
        name = "word_counter",
        description = "This is a tool which is used to count the number of words in a sentence. This take input as a single string",
        func = word_counter
    ),
]


agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    memory=memory,
    verbose=True,
    handle_parsing_errors=True,
    agent_kwargs={
        "prefix": "You have access to the following tools and also to chat history. Use chat history to answer questions about previous conversations."
    }
)

while True:
    user_input = input("Enter Prompt : ")
    if user_input == "quit":
        break
    agent_output = agent.invoke({"input" : user_input })
    print(agent_output)
