# ===============================
#         NOVA AI CHATBOT
# ===============================

# Welcome Page
def welcome():
    print("=" * 50)
    print("          🤖 WELCOME TO NOVA AI 🤖")
    print("=" * 50)
    print("      Your Smart Virtual Assistant")
    print("=" * 50)


# Sign Up Function
def signup():
    print("\n========== SIGN UP ==========")

    user = input("Create a username: ").lower()
    password = input("Create a password: ")

    accounts.append((user, password))

    print("\n✅ Account created successfully!")
    print("Please log in.\n")


# Chat Function
def chat():

    print("\n=========================================")
    print("🤖 NOVA AI is now online!")
    print("Type 'help' to see all commands.")
    print("Type 'bye' to exit the chatbot.")
    print("=========================================\n")

    while True:

        chatbox = input("You: ").lower()

        if chatbox == "hello":
            print("NOVA AI: Hello! 👋 It's nice to meet you.")

        elif chatbox == "hi":
            print("NOVA AI: Hi! 😊 How can I help you today?")

        elif chatbox == "good morning":
            print("NOVA AI: 🌞 Good morning! Have an amazing day!")

        elif chatbox == "good afternoon":
            print("NOVA AI: ☀️ Good afternoon! Hope you're doing well.")

        elif chatbox == "good evening":
            print("NOVA AI: 🌙 Good evening! What can I do for you?")

        elif chatbox == "who are you":
            print("NOVA AI: I'm NOVA AI, your personal virtual assistant.")

        elif chatbox == "what is your name":
            print("NOVA AI: My name is NOVA AI.")

        elif chatbox == "what can you do":
            print("NOVA AI: I can chat with you, answer simple questions, tell jokes and motivate you!")

        elif chatbox == "tell me about yourself":
            print("NOVA AI: I'm a chatbot created using Python to assist users.")

        elif chatbox == "who created you":
            print("NOVA AI: I was created by Tsion using Python.")

        elif chatbox == "how are you":
            print("NOVA AI: I'm doing fantastic! Thanks for asking. 😄")

        elif chatbox == "i am fine":
            print("NOVA AI: That's wonderful to hear! 😊")

        elif chatbox == "thank you":
            print("NOVA AI: You're always welcome! ❤️")

        elif chatbox == "motivate me":
            print("NOVA AI: 🌟 Believe in yourself.")
            print("Every expert was once a beginner.")

        elif chatbox == "favorite programming language":
            print("NOVA AI: Definitely Python! 🐍")

        elif chatbox == "joke":
            print("NOVA AI: 😂 Why do programmers prefer dark mode?")
            print("Because light attracts bugs!")

        elif chatbox == "time":
            print("NOVA AI: Sorry, I can't tell the current time yet.")

        elif chatbox == "date":
            print("NOVA AI: Sorry, I can't tell today's date yet.")

        elif chatbox == "help":
            print("\n========== AVAILABLE COMMANDS ==========")
            print("hello")
            print("hi")
            print("good morning")
            print("good afternoon")
            print("good evening")
            print("who are you")
            print("what is your name")
            print("what can you do")
            print("tell me about yourself")
            print("who created you")
            print("how are you")
            print("i am fine")
            print("thank you")
            print("motivate me")
            print("favorite programming language")
            print("joke")
            print("time")
            print("date")
            print("bye")
            print("========================================")

        elif chatbox == "bye":
            print("NOVA AI: 👋 Goodbye!")
            print("Thank you for chatting with me.")
            print("Have a wonderful day!")
            break

        else:
            print("NOVA AI: 🤔 Sorry, I don't understand that.")
            print("Type 'help' to see the available commands.")


# ===============================
# Main Program
# ===============================

welcome()

while True:

    try:
        choice = int(input("""
========== MENU ==========

1. 📝 Sign Up
2. 🔑 Login
3. 🚪 Exit

Enter your choice: """))

        if choice == 1:
            signup()

            if login():
                chat()
            break

        elif choice == 2:

            if login():
                chat()
            break

        elif choice == 3:
            print("\n👋 Thank you for using NOVA AI.")
            print("Goodbye!")
            break

        else:
            print("❌ Please enter 1, 2 or 3.")

    except ValueError:
        print("❌ Please enter numbers only.")