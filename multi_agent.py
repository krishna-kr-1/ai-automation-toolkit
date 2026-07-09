from langchain_classic.agents import initialize_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_classic.agents.agent_types import AgentType
from langchain_core.tools import Tool
import os
load_dotenv()
llm = ChatGoogleGenerativeAI(model = "gemini-2.5-flash", google_api_key = os.getenv("google_api_key"))
def calculator(input):
    a, b, sign = input.strip().split(",")
    a = a.strip()
    b = b.strip()
    sign = sign.strip()
    a = int(a)
    b = int(b)
    print(sign)
    if sign == "+" : 
        return a + b
    elif sign == "-" :
        return a-b
    elif sign == "*" : 
        return a * b
    elif sign == "/" : 
        return a/b
    else:
        return None
def word_counter(input):
    return (len(input.split()))
    
def text_reverser(input):
    return (input[::-1])
    
tools = [
     Tool(
        name = "calculator",
        description = "This is a tool which is used to calculate numerical value by passing 1st parameter is number, 2nd parameter is number, 3rd parameter is a symbol in string format like + , -, *, /",
        func = calculator
    ),
     Tool(
        name = "Reverse_word",
        description = "This is a tool which is used to reverse a word, which take input as a string",
        func = text_reverser
    ),
     Tool(
        name = "Word_Counter",
        description = "This is a tool which is used to count the number of words present in a sentence which takes input as a string",
        func = word_counter
    ),
    
]
agent = initialize_agent (tools = tools, llm = llm, agent = AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose = True)
user_input = input("Enter the Prompt for the agent : ")
agent.invoke({"input" : user_input})
