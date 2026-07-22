from google import genai
from dotenv import load_dotenv
import os
import time

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

while True:
    user_input=input("prompt:")
    if user_input.lower() in ["exit","quit","bye"]:
        break
    #store user message here
    history.append(f"User: {user_input}")

    if len(history)> Max_history:
        history=history[-Max_history]
    
    #conversattion context
    conversation_context = system_prompt + "\n"
    conversation_context += "\n".join(history)

    start_time=time.time()
    full_response=""
    
    try:
        #call gemini model

        stream=client.models.generate_content_stream(
            model="gemini-2.5-flash",
            contents=conversation_context
        )
        for chunk in stream:
            if chunk.text:
                print(chunk.text,end="",flush=True)
                full_response+=chunk.text
        
        end_time=time.time()
        total_time=end_time-start_time
        print(f"\nTime taken for response: [{total_time} seconds]")
       
        # store bot response
        history.append(f'Assistant: {full_response}')
    except Exception as e:
        print(f"error:{e}")
        continue


