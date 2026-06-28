import requests

class GemeniClient:
    def __init__(self, api_key):
        self.api_key = api_key
        self.url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent"

    def ask_prompt(self, prompt):
        payload = {
            "contents" : [
                {
                    "parts" : [
                        {"text" : prompt}
                    ]
                }
            ]
        }

        return self.send_pyload(payload)

    def ask_with_context(self, system_context, prompt):
        payload = {
            "system_instruction": {
                "parts": [{"text": system_context}]
            },
            "contents": [
                {
                    "parts": [{"text": prompt}]
                }
            ]
        }
        return self.send_pyload(payload)

    def send_pyload(self,  payload):
        params = {"key" : self.api_key}
        try:
            response = requests.post(self.url, json = payload ,params = params)
            response.raise_for_status()
            data = response.json()
            return data["candidates"][0]["content"]["parts"][0]["text"]
        except requests.exceptions.RequestException as e:
            print("Failed to call API")
            print(e)
            return None

class RPAAdvisor(GemeniClient):
    def __init__(self, api_key):
        super().__init__(api_key)
        self.context = "You are an RPA expert. Give concise answers in maximum 3-4 bullet points. Be direct and practical."

    def advior(self, question):
        return self.ask_with_context( self.context, question)

    def compare_tools(self, tool1, tool2):
        prompt =  f"Compare {tool1} and {tool2} as RPA tools. Key differences, pros and cons."
        return self.ask_with_context(self.context, prompt)


class ResumeAnalyzer(GemeniClient):

    def __init__(self, api_key):
        super().__init__(api_key)
        self.context = "You are a professional Resume Analyzer, analyze my resume and give me the feedback and improvement points in in 3-4 bullet and any other opinion in 3 to 4 bullter"
        

    def load_resume(self, filename):
        try:
            with open(filename, "r") as f:
                data = f.readlines()
                return ("".join(data))
        except FileNotFoundError:
            print("failed to find file")
        
    def check_resume(self, filename):
        resume = self.load_resume(filename)
        prompt = f"Here is my resume and check this out {resume}"
        return (self.ask_with_context(self.context, prompt))