def get_student():
    name = input(" Enter your name: ")
    age =int(input(" Enter your age: "))
    college = input(" Enter your college:")
    branch = input(" Enter your branch:")
    return name, age, college, branch

name, age, college, branch = get_student()

print("\n==== Student profile ====")
print(f"Name : {name}")
print(f"Age : {age}")
print(f"College : {college}")
print(f"Branch : {branch}")

print("Enter your marks in 3 subjects:")
marks1 = int(input("Subject 1: "))
marks2 = int(input("Subject 2: "))
marks3 = int(input("Subject 3: "))
def calculate_total_marks(m1, m2, m3):
    return m1 + m2 + m3
total_marks = calculate_total_marks(marks1, marks2, marks3)
print(f"Total marks: {total_marks}")
def calculate_average_marks(total, num_subjects):
    return total / num_subjects
print(f"Average marks: {calculate_average_marks(total_marks, 3)}")
