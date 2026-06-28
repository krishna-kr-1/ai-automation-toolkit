import requests

class DocumentProcessor:
    def __init__(self, api_key):
        self.api_key = api_key
        self.url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent"

    def gemeni_client(self, file_content, task):
        context = f"Hi, You are a AI Document Processor, That take the Input File and perform the specific {task} and return the Response in 3 to 4 Bullet points."
        params = {"key" : self.api_key}
        payload = {
            "system_instruction": {
                "parts": [{"text": context}]
                    },
            "contents": [
                    {
                    "parts": [{"text": file_content}]
                    }
                ]
            }
        try:
            response = requests.post(self.url, json = payload, params = params)
            response.raise_for_status()
            data = response.json()["candidates"][0]["content"]["parts"][0]["text"]
            return data
        except requests.exceptions.RequestException as e:
            print(e)
        return None

    def load_file(self, filename):
        try:
            with open(filename, "r") as f:
                content = f.readlines()
                content = "".join(content)
                return content
        except FileNotFoundError as e:
            print("Failed to load file")
            print(e)
            return None

    def generate_output_file(self, file_path,output_from_gemeni):
        try:
            with open(file_path, "w") as f:
                f.write(output_from_gemeni)
        except FileNotFoundError as e:
            print(e)
        
    def process(self, input_file, task, output_file):
        input_file_content = self.load_file(input_file)
        output_from_gemeni = self.gemeni_client(input_file_content, task)
        self.generate_output_file(output_file,output_from_gemeni)
