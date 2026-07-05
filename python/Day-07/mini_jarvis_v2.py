print("welcome to mini jarvis v2")

name = input("Enter your name: ")
age = int(input("Enter your age: "))
dream=input("Enter your dream:")

print()

if age >= 18:
    print("Hello", name + "!")
    print("You are an adult.")
else:
    print("Hello", name + "!")
    print("You are a student.")
    
print("Your dream is:", dream)

print()
print("Remember:", name + ", every great engineer starts as a beginner.")
print("Keep learning, keep building!")