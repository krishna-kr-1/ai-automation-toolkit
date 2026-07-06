import requests
from dotenv import load_dotenv
import os

class MemoryChat:
    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv("google_api_key")
        self.url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent"

    def _get_response(self, content):
        payload = {
            "contents" : [
                {
                    "parts" : [
                        {
                            "text" : content
                        }
                    ]
                }
            ]
        }
        return self._send_payload(payload)

    def _send_payload(self, payload):
        try:
            params = {"key" : self.api_key}
            response = requests.post(self.url, json = payload, params = params)
            response.raise_for_status()
            return response.json()["candidates"][0]["content"]["parts"][0]["text"]
        except requests.exceptions.RequestException as e:
            print("failed to call api")
            print(e)
            return None

    def call_process(self):
        send_input = ""
        while(True):
            input_text = input("Enter the prompt : ")
            if input_text == "exit":
                print("Thank You for Service")
                return 
            send_input = input_text + " " + send_input
            response = self._get_response(send_input)
            print(response)
            send_input = send_input + response
            
