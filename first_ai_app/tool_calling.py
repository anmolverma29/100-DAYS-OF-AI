#here we learn about the fundamentals of tool calling in gemini api. we will create a simple chatbot which can call some tools based on user query and if no tool is found, it will use the gemini model to generate response.

from google import genai
from dotenv import load_dotenv
import os
import time
from datetime import datetime
import random

#Load envirnment variable
#gemini api key from .env file
load_dotenv()

API_KEY=os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("API key not found")

#Create a client instance of gemini
client=genai.Client(api_key=API_KEY)

#store history of conversation
history=[]

#context management
Max_history = 20


system_prompt="You are a helpful assistant and have to follow some rules." \
"" \
"1. be helpfull" \
"2. be concise" \
"3. be polite" \
"4. remember previous conversation context" \

print("="*50)
print("Gemini Chatbot")
print("="*50)

#shows current time if asked by user
def datetime_now():
    return datetime.now().strftime("%I:%M:%S, %p")

#tool which returns a random motivational quote if asked by user
def motivational_quote():
    quotes = [
        "Believe you can and you're halfway there. - Theodore Roosevelt",
        "The only way to do great work is to love what you do. - Steve Jobs",
        "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
        "Don't watch the clock; do what it does. Keep going. - Sam Levenson",
        "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt"
    ]
    return random.choice(quotes)

#calculator tool
def calculator(expression):
    try:
        result=eval(expression)
        return result
    except Exception as e:
        return "Invalid Expression"

#based on user query, route to the appropriate tool or return "gemini" to use the gemini model
def route_tool(query):
    query=query.lower()
    if "time" in query:
        return "time"
    elif "calculator" in query:
        return "calculator"
    elif "quote" in query or "motivation" in query:
        return "quote"
    return "gemini"


#user input loop
while True:
    user_input=input("prompt:")
    if user_input.lower() in ["exit","quit","bye"]:
        break
    tool=route_tool(user_input)
    if tool=="time":
        result=datetime_now()
        print(f"Current time: {result}")
    elif tool =="calculator":
        expression=(user_input.replace("calculate","").strip())
        result=calculator(expression)
        print(f"Result: {result}")
    elif tool =="quote":
        result=motivational_quote()
        print(f"Motivational Quote: {result}")
    else:
        response=client.models.generate_content(
            model="gemini-2.5-flash",
            contents=user_input
            )
        print(f"Gemini Response: {response.text}")


   