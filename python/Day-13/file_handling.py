name = input("Enter your name: ")
age = input("Enter your age: ")
college = input("Enter your college: ")
with open("student.txt", "w") as file:
    file.write(name)
    
    file.write(age)

    file.write(college)
print("Saved!")

with open("student.txt", "r") as file:
 data=file.read()
print("\n=====Student profile=====")
print(data)
file.close