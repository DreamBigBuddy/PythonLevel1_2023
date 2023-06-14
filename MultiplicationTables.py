# Multiplication Tables

num = int(input("Enter a number: "))
limit = int(input("What number to stop at: "))

for i in range(1, limit+1):
    print(i, "*", num, "=", i*num)
