from google import genai
from dotenv import load_dotenv
import os

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
    
    #conversattion context
    conversation_context = system_prompt + "\n"
    conversation_context += "\n".join(history)
    
    try:
        #call gemini model

        response=client.models.generate_content(
            model="gemini-2.5-flash",
            contents=conversation_context
        )
        
        bot_response=response.text
        print(f"\n Gemini : {bot_response}")
        
        # store bot response
        history.append(f'Assistant: {bot_response}')
    except Exception as e:
        print(f"service is unavailable, please try again later{e}")


