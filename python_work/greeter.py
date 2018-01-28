prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print("\nHello, " + name + "!")

def greet_user(username):
    """Show simple hello"""
    print("Hello, " + username.title() + "!")

greet_user("jesse")

