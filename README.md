# AI Automation Toolkit

Python utilities for AI and automation workflows.

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

## Tech Stack
Python, Requests, Google Gemini API

## Usage

### DocumentProcessor
```python
from document_processor import DocumentProcessor

processor = DocumentProcessor("YOUR_GEMINI_API_KEY")

# Analyze a resume
processor.process("resume.txt", "analyze this resume and give feedback", "output.txt")

# Summarize a report
processor.process("report.txt", "summarize the key points", "summary.txt")
```

### GeminiClient
```python
from gemini_client import GeminiClient, RPAAdvisor, ResumeAnalyzer

# Basic usage
client = GeminiClient("YOUR_GEMINI_API_KEY")
print(client.ask_prompt("What is RPA?"))

# RPA Expert
advisor = RPAAdvisor("YOUR_GEMINI_API_KEY")
print(advisor.compare_tools("Automation Anywhere", "UiPath"))

# Resume Analysis
analyzer = ResumeAnalyzer("YOUR_GEMINI_API_KEY")
print(analyzer.check_resume("resume.txt"))
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

## Requirements
```
pip install requests
```

## Author
Krishna Kumar — RPA Developer transitioning to AI Automation Engineer
