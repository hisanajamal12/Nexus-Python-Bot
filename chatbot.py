import sys

def main_chatbot():
    print("🤖 Nexus Bot: Hello! I am Nexus, your intelligent assistant.")
    print("🤖 Nexus Bot: Type 'exit' or 'bye' at any time to close our chat.\n")
    
    while True:
        # Taking input from the user and converting to lowercase for easy matching
        user_input = input("You: ").strip().lower()
        
        # Check for empty input
        if not user_input:
            print("🤖 Nexus Bot: I didn't catch that. Could you say something?")
            continue
            
        # Rule-based conditions (if-elif-else logic)
        if user_input in ["hello", "hi", "hey", "hello there"]:
            print("🤖 Nexus Bot: Hey there! How can I help you today?")
            
        elif user_input in ["how are you", "how's it going", "how are you doing"]:
            print("🤖 Nexus Bot: I'm just a bundle of code, but I'm running perfectly! How about you?")
            
        elif user_input in ["what is your name", "who are you"]:
            print("🤖 Nexus Bot: I am Nexus-Python-Bot, a custom rule-based open-source assistant!")
            
        elif user_input in ["fine", "good", "great", "i am fine"]:
            print("🤖 Nexus Bot: That's awesome to hear! Let's keep the good vibes going.")
            
        elif user_input in ["bye", "goodbye", "exit", "quit"]:
            print("🤖 Nexus Bot: Goodbye! Have a wonderful day ahead. See ya!")
            break
            
        else:
            print("🤖 Nexus Bot: Interesting! I'm still learning, so I don't quite understand that yet. Try saying 'hello' or 'how are you'.")

if __name__ == "__main__":
    main_chatbot()
