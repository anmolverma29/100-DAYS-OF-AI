from google import genai
from dotenv import load_dotenv
import os
import time

#Load envirnment variable
load_dotenv()
API_KEY=os.getenv("GEMINI_API_KEY")
client=genai.Client(api_key=API_KEY)

#defining Agent
