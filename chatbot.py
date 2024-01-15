import sys

def greeting():
    print("Hello! I'm a chatbot. What can i call you? ")

def respond(question):
    questions_answers = {
        "who are you": "I'm a chatbot.",
        "what do you do": "I'm here to help answer basic questions and make conversation.",
        "how are you": "I'm a computer program, so I don't have feelings, but I'm ready to assist you!",
        "where are you from": "I'm from the world of programming.",
        "when were you created": "I was created just now for this conversation.",
    }

    answer = questions_answers.get(question.lower())
    if answer:
        return answer
    else:
        return "I'm sorry, I don't know the answer to that question."
    
def say_bye():
    print("It was nice talking to you! Have a great day!")

def register_prev(user_input, context):
    context["previous_interactions"] = context.get("previous_interactions", [])
    context["previous_interactions"].append(user_input)

def recall_context(context):
    if context.get("previous_interactions"):
        print("Previously, you said:")
        for interaction in context["previous_interactions"]:
            print(f"- {interaction}")

def ask_questions(chatbot_name):
    questions = [
        f"Do you like programming?, {chatbot_name}?",
        "Do you like Python for its simplicity and readability?",
        "Have you ever talked to a chatbot before?",
        "Have you ever created a chatbot before?",
    ]

    for question in questions:
        user_input = input(question + " (yes/no): ")
        if user_input.lower() in ["yes", "y"]:
            print("That's great! I'm here to help you learn more.")
        elif user_input.lower() in ["no", "n"]:
            print("No worries, I'm here to help you get started.")
        else:
            print("I'm sorry, I didn't understand your answer. Let's move on.")



def handle_input(user_input, context):
    if user_input.lower() == "bye":
        say_bye()
        sys.exit()
    elif user_input.lower() == "previous convo":
        recall_context(context)
    else:
        response = respond(user_input)
        print(response)
        register_prev(user_input, context)


context = {}
greeting()

name = input()
ask_questions(name)

while True:
    user_input = input("Ask me something or type 'previous convo' to see previous interactions, type 'bye' to leave: ")
    handle_input(user_input, context)
