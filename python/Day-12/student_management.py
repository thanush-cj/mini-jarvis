def student_profile():
    name = input("Enter your name: ")
    age = input("Enter your age: ")

    print("\n=====Student Profile=====")
    print(f"Name : {name}")
    print(f"Age : {age}")

def even_odd():
    number = int(input("Enter your number: ") )
    
    if number % 2 == 0:
        print(f"Number {number} is Even")
        
    else:
        print(f"Number {number} is Odd")
        
def multiplication_table():
    number = int(input("Enter your mutiplication table number:"))
    for i in range(1,11):
        print(f"{number} x {i} = {number*i}")
        
def calculation():
    num1 = int(input("Enter your first number:"))
    num2 = int(input("Enter your second number:"))
    
    print("1. Addition")
    print("2. Subtraction") 
    print("3. Multiplication")
    print("4. Division")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        print(f"Addition of {num1} and {num2} is: {num1 + num2}")
    elif choice == '2':
        print(f"Subtraction of {num1} and {num2} is: {num1 - num2}")    
    elif choice == '3':
        print(f"Multiplication of {num1} and {num2} is: {num1 * num2}")
    elif choice == '4':
        if num2 != 0:
            print(f"Division of {num1} and {num2} is: {num1 / num2}")
        else:
            print("Error: Division by zero is not allowed.")
while True:
    print("\n=====Student Management System=====")
    print("1. Student Profile")
    print("2. Even or Odd")
    print("3. Multiplication Table")
    print("4. Calculation")
    print("5. Exit")
    
    choice = input("Enter your choice (1-5): ")
    
    if choice == '1':
        student_profile()
        
    elif choice == '2':
        even_odd()
        
    elif choice == '3':
        multiplication_table()
        
    elif choice == '4':
        calculation()
        
    elif choice == '5':
        print("Exiting the program. Goodbye!")
        break
        
    else:
        print("Invalid choice! Please try again.")