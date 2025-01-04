from autogen import ConversableAgent
import random
import os

# Print initialization message
print("Welcome to FunBot, your quirky chatbot powered by Autogen! Let's make this chat a blast! 🚀")

# Load API key from environment variable
model = "gpt-3.5-turbo"
api_key = os.getenv("OPENAI_API_KEY")

# Check if the API key is available
if not api_key:
    raise EnvironmentError("API key not found! Please set the OPENAI_API_KEY environment variable.")

llm_config = {
    "model": model,
    "api_key": api_key,
}

# Create the ConversableAgent
agent = ConversableAgent(
    name="FunBot",
    llm_config=llm_config,
    code_execution_config=False,
    human_input_mode="NEVER",
)

# Chat loop
def chat_loop():
    print("\nLet’s get started! Type your message or ask me anything. Type 'exit' to quit.\n")
    while True:
        # Get user input
        user_input = input("You: ")
        
        # Exit condition
        if user_input.lower() in ["exit", "quit"]:
            print("FunBot: Aww, leaving so soon? Take care and come back anytime! 👋")
            break

        # Fun pre-response
        playful_comments = [
            "Oh, this one’s gonna be good! 😄",
            "Let me put on my thinking cap… 🧢",
            "Ooh, I love this question! 🥳",
            "Hold on, let me channel my inner genius… 🧠",
        ]
        print(f"FunBot: {random.choice(playful_comments)}")

        # Autogen message
        print("FunBot: (Powered by Autogen - making smart conversations happen!)")

        # Generate response
        try:
            response = agent.generate_reply(messages=[{"role": "user", "content": user_input}])
            print(f"FunBot: {response}\n")
        except Exception as e:
            print(f"FunBot: Oops! Something went wrong: {e}\n")

# Run the chatbot
if __name__ == "__main__":
    chat_loop()
