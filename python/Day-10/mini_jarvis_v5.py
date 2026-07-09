def welcome():
    return "Welcome to Mini Jarvis!"

def ask_name():
    name = input("What is your name? ")
    return name

message = welcome()
print(message)

user = ask_name()

print(f"Hello, {user}!")
print("Have a great day!")