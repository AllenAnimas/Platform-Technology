
def get_bot_response(user_message):
    responses = {
        "hello":"Hello! How can I help you?",
        "tell me about":"Sure! What place would you like to know about?",
        "bye": "Goodbye! Have a great day!",
    }
    return responses.get(user_message, "I'm not sure how to respond to that.")
def main():
    print("welcome im your chatbot, type 'bye' to exit.")
    while True:
        user_input =input("You: ") .strip().lower()
        if user_input == "bye":
            print("Chatbot: Goodbye! Have a great day!")
            break
        response = get_bot_response (user_input)
        print("Chatbot:", response)
        if __name__ == "_main_":
            main()