from google import genai
from dotenv import load_dotenv
import os
import time

#Load envirnment variable
load_dotenv()
API_KEY=os.getenv("GEMINI_API_KEY")
client=genai.Client(api_key=API_KEY)

#defining Agent
class RoadMapAgent:
    def __init__(self, goal):
        #here goal=user input
        self.goal=goal

    #step-1: Reasoning
    def reasoning(self):
        print("[Agent] Understanding Goal...")
        prompt=f""" 
        user goal: {self.goal}
        identify all required skills.
        Return only the skills
        """
        response=client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
        )
        return response.text

    #step- 2 Planning
    def planning(self,skills):
        print("[Agent] creating plan...")
        prompt=f"""
        goal: {self.goal}
        Skills: {skills}
        Arrange these skills in a step by step learning order
        """
        response=client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
        )
        return response.text
    #step- 3: Execution
    def Execution(self,plan):
            print("[Agent] Executing plan...")
            prompt=f"""
            goal: {self.goal}
            plan: {plan}
            Planning is done, now create a roadmap for the user to achieve the goal.
            """
            response=client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
            )
            return response.text
    #Run the agent
    def run(self):
         skills=self.reasoning()
         time.sleep(1)
         plan=self.planning(skills)
         time.sleep(1)

         roadmap=self.Execution(plan)

         print("\n" + "="*50)
         print("Final Roadmap")
         print("=" * 50)
         print(roadmap)
print("="*50)
print("welcome to the RoadMap Agent!")
print("="*50)
goal=input("Enter your goal:")
agent=RoadMapAgent(goal)
agent.run()
    



        

