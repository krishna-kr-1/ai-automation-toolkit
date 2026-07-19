# AI Automation Toolkit

Python utilities for AI and automation workflows.

## Setup

1. Clone the repo
2. Install dependencies: pip install requests langchain langchain-core langchain-google-genai python-dotenv langchain-classic
3. Create a `.env` file in the root folder: GOOGLE_API_KEY=your_gemini_api_key_here
4. Never commit your `.env` file — it's already in `.gitignore`

## Projects

### EmployeeManager
- Full CRUD operations on CSV files
- Filter by status, department, salary range
- File persistence

### GeminiClient / RPAAdvisor / ResumeAnalyzer
- Raw API integration with Google Gemini
- Context-aware responses via system instructions
- RPA tool comparison and resume analysis

### DocumentProcessor
- Reads any text document
- Sends to Gemini AI with a custom task
- Saves AI response to output file
- Use cases: resume analysis, report summarization, document extraction

### LangChain Pipeline
- LCEL chain using PromptTemplate and StrOutputParser
- Two step pipeline: summarize → rewrite in professional tone
- Uses python-dotenv for secure API key management

### Memory Chat (LangChain)
- ConversationBufferMemory with ConversationChain
- Full conversation history injected into every prompt
- Exit on 'quit', prints memory buffer at end

### LangChain Document Rewriter
- Two-chain LCEL pipeline (summary → tone rewrite)
- PromptTemplate, StrOutputParser, ChatGoogleGenerativeAI
- Verified working with Gemini 2.5 Flash

### Manual Memory Chat
- Raw requests implementation with manual context tracking
- Shows what LangChain memory abstracts under the hood

### Window Memory Chat (LangChain)
- ConversationBufferWindowMemory with k=3
- Remembers only last 3 exchanges — production-safe token management
- Drops oldest exchanges automatically as conversation grows
- Same interface as Memory Chat but token-efficient

### Basic Agent (LangChain)
- initialize_agent
- Create agent with Gemini to use Tools
- ReAct pattern (Think → Act → Observe loop)
- Single calculator tool with comma-separated input parsing
- Demonstrates LLM-driven tool selection via ZERO_SHOT_REACT_DESCRIPTION

### Multi Agent (LangChain)
- initialize_agent with 3 tools — calculator, word counter, text reverser
- LLM-driven dynamic tool selection via ZERO_SHOT_REACT_DESCRIPTION
- Demonstrates agent picking correct tool based on tool descriptions

### Memory Agent (LangChain)
- Multi-tool agent with ConversationBufferWindowMemory(k=5)
- Remembers last 5 conversation exchanges
- chat_history injected into agent context automatically

### Basic RAG
- RecursiveCharacterTextSplitter for document chunking
- GoogleGenerativeAIEmbeddings (gemini-embedding-001) for vector conversion
- FAISS vector store for similarity search
- RetrievalQA chain connecting retriever to LLM
- Query loop for interactive Q&A

### PDF RAG (LangChain)
- PyPDFLoader for extracting text from PDF documents
- RecursiveCharacterTextSplitter for chunking PDF content
- GoogleGenerativeAIEmbeddings (gemini-embedding-001) for vector conversion
- FAISS vector store with index persistence — built once, reused forever
- Auto-generates index path from PDF filename using os.path
- RetrievalQA chain for accurate, document-grounded answers
- Production-ready — avoids redundant embedding API calls on repeat runs

### Conversational RAG (LangChain)
- ConversationalRetrievalChain combining RAG + memory
- ConversationBufferWindowMemory(k=5) for conversation history
- Follow-up questions handled via chat_history context
- FAISS vector store with index persistence
- Known limitation: gemini-embedding-001 500 error on follow-up embedding calls — fix planned with LangGraph migration

## Tech Stack
Python, Requests, Google Gemini API, LangChain, python-dotenv

## Usage

### DocumentProcessor
```python
from document_processor import DocumentProcessor
from dotenv import load_dotenv
import os

load_dotenv()
processor = DocumentProcessor(os.getenv("GOOGLE_API_KEY"))
processor.process("resume.txt", "analyze this resume and give feedback", "output.txt")
```

### GeminiClient
```python
from gemini_client import GeminiClient, RPAAdvisor, ResumeAnalyzer
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

client = GeminiClient(api_key)
print(client.ask_prompt("What is RPA?"))

advisor = RPAAdvisor(api_key)
print(advisor.compare_tools("Automation Anywhere", "UiPath"))
```

### EmployeeManager
```python
from employee_manager import EmployeeManager

mgr = EmployeeManager("employees.csv")
mgr.get_active()
mgr.get_by_department("Automation")
mgr.get_by_salary_range(300000, 450000)
mgr.add_employee("11,Ravi Kumar,IT,430000,active")
mgr.save()
```

### LangChain Pipeline
```python
from dotenv import load_dotenv
import os

load_dotenv()
# See langchain_pipeline.py for full usage
```

## Requirements
pip install requests langchain langchain-classic langchain-core langchain-google-genai langchain-community python-dotenv

## Author
Krishna Kumar — RPA Developer transitioning to AI Automation Engineer
Stack: Python, LangChain, Google Gemini, Automation Anywhere A360, VBA Macro
