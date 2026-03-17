from langchain_core.messages import HumanMessage
from langchain_community.chat_models import ChatOllama
from langchain.tools import tool
from langchain.agents import create_agent
from dotenv import load_dotenv

load_dotenv()

def main():
    model = ChatOllama(temperature=0,
                       model="phi3")
    
    agent = create_agent(model=model,tools=[])
    
    print("Welcome I am your Local AI assistant. Type 'quit' to exit")
    
    while True:
        user_input = input("\nYou: ").strip()
        
        if user_input.lower() == 'quit':
            break
            
        result = agent.invoke({
            "messages": [
                {"role":"user","content":user_input}
            ]
        })
        
        print("\nAssistant: ", result["messages"][-1].content)

if __name__ == "__main__":
    main()