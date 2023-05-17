print("Welcome to the calculator!")

ans = "yes"

while ans == "yes":
    num1 = int(input("Enter a number: "))
    op = input("Enter any one of these operator - '+', '-', '*', '/': " )
    num2 = int(input("Enter another number: "))

    if op == '+':
        print('The answer is:', num1 + num2)

    elif op == '-':
        print('The answer is:', num1 - num2)

    elif op == '*':
        print('The answer is:', num1 * num2)

    elif op == '/':
        print('The answer is:', num1 / num2)

    ans = input("Would you like to run the program again? ").lower()
