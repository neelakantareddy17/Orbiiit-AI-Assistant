from agent import build_agent

def start_chat():
    agent = build_agent()
    print("🤖 HiesenBot (LangChain Mode) ready!")

    while True:
        q = input("\nYou: ")
        if q.lower() == "exit":
            break
        
        print("\nHiesenBot:", agent.run(q))

if __name__ == "__main__":
    start_chat()
