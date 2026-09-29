import os
import requests
import socket
from dotenv import load_dotenv

load_dotenv()

# Force IPv6 DNS Resolution
def allowed_gai_family():
    return socket.AF_INET6

requests.packages.urllib3.util.connection.allowed_gai_family = allowed_gai_family

class GeminiDocumentGenerator:
    def __init__(self):
        self.api_key = os.getenv("GEMINI_API_KEY")
        # Fixed v1beta endpoint and model name
        self.url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash-lite:generateContent?key={self.api_key}"

    def generate_document(self, document_type, parties, dates, terms):
        prompt = (
            f"Generate a comprehensive legal document titled '{document_type}'\n"
            f"Involved parties: {parties}\n"
            f"Effective Date: {dates}\n"
            f"Terms and conditions: {terms}\n"
            f"Ensure formal legal structure with multiple sections and legal clauses."
        )

        headers = {"Content-Type": "application/json"}
        payload = {
            "contents": [
                {
                    "parts": [{"text": prompt}]
                }
            ]
        }

        try:
            response = requests.post(self.url, json=payload, headers=headers, timeout=30)
            response_data = response.json()

            if "candidates" in response_data:
                return response_data["candidates"][0]["content"]["parts"][0]["text"]
            else:
                return f"API Error Details: {response_data}"
        except Exception as e:
            return f"Connection Exception: {str(e)}"