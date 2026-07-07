print("=== Multiplication Table Generator ===")
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))
count = int(input("Generate the table up to: "))
print()
for table in range(start, end + 1):
    print(f"Table of {table}")
    print("--------------------")
    for i in range(1, count + 1):
        print(f"{table} x {i} = {table * i}")

    print()