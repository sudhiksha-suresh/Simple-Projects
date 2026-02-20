def chatbot():
    """
    A simple rule-based chatbot that responds to basic greetings and questions
    """
    print("🤖 ChatBot: Hello! I'm a simple chatbot. Type 'bye' to exit.")
    
    while True:
        # Get user input
        user_input = input("👤 You: ").lower().strip()
        
        # Check for exit condition
        if any(bye_word in user_input for bye_word in ["bye", "goodbye", "exit", "quit"]):
            print("🤖 ChatBot: Goodbye! Have a nice day!")
            break
        
        # Check for greetings
        elif any(greet_word in user_input for greet_word in ["hello", "hi", "hey", "hola"]):
            print("🤖 ChatBot: Hi there! Nice to meet you!")
        
        # Check for how are you questions
        elif "how are you" in user_input or "how do you do" in user_input:
            print("🤖 ChatBot: I'm just a program, but thanks for asking! I'm functioning well.")
        
        # Check for name questions
        elif "your name" in user_input or "who are you" in user_input:
            print("🤖 ChatBot: I'm ChatBot, your friendly AI assistant!")
        
        # Check for help requests
        elif "help" in user_input:
            print("🤖 ChatBot: I can respond to greetings like 'hello' and 'hi', ask me 'how are you', or say 'bye' to exit.")
        
        # Default response for unknown inputs
        else:
            print("🤖 ChatBot: Sorry, I don't understand that. I'm a simple bot that responds to greetings!")

def main():
    """
    Main function to run the chatbot
    """
    print("=" * 50)
    print("        SIMPLE RULE-BASED CHATBOT")
    print("=" * 50)
    
    # Start the chatbot
    chatbot()

if __name__ == "__main__":
    main()
