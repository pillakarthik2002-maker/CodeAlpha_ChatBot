import random
import datetime

def chatbot():
    print("🤖 Welcome to Smart Chatbot!")
    name = input("Bot: What's your name? ")
    print(f"Bot: Nice to meet you, {name}!\n")

    responses = {
        "hello": ["Hi!", "Hello there!", "Hey!"],
        "how are you": ["I'm fine, thanks!", "Doing great!", "All good!"],
        "what is your name": ["I'm a Python Chatbot.", "You can call me SmartBot!"],
        "bye": ["Goodbye!", "See you soon!", "Have a great day!"]
    }

    while True:
        user_input = input(f"{name}: ").lower()

        # Greeting responses
        if user_input in responses:
            reply = random.choice(responses[user_input])
            print("Bot:", reply)

            if user_input == "bye":
                break

        # Time feature
        elif user_input == "time":
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            print("Bot: Current time is", current_time)

        # Date feature
        elif user_input == "date":
            current_date = datetime.datetime.now().strftime("%Y-%m-%d")
            print("Bot: Today's date is", current_date)

        # Simple Calculator
        elif "calculate" in user_input:
            try:
                expression = user_input.replace("calculate", "")
                result = eval(expression)
                print("Bot: The result is", result)
            except:
                print("Bot: Please enter a valid calculation.")

        # Asking about user
        elif "my name" in user_input:
            print(f"Bot: Your name is {name}!")

        # Default response
        else:
            print("Bot: Sorry, I don't understand that.")

chatbot()
