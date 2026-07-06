from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv

load_dotenv()

llm = ChatGoogleGenerativeAI( model = "gemini-2.5-flash" , google_api_key = os.getenv("google_api_key"))

summary_template = PromptTemplate(
    input_variables = ["document"],
    template = "Summarize the following document in 3 bullet points:\n\n{document}"
)
summary_chain = summary_template | llm | StrOutputParser()

tone_template = PromptTemplate(
    input_variables = ["document"],
    template = "Rewrite the following in a professional tone:\n\n{document}"
)
tone_chain = tone_template | llm | StrOutputParser()

def process(file):
    summary = summary_chain.invoke({"document" : file})
    tone = tone_chain.invoke({"document" : summary})
    print(tone)
    
if __name__ == "__main__":
    sample_doc = """
    hey so basically i was trying to fix this bug right and 
    it took me like 3 hours but i finally got it working. 
    the problem was a missing bracket and also some variable 
    names were wrong. pretty annoying but its done now.
    """
    process(sample_doc)
