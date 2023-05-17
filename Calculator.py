class Calc:
    def add(self):
        print(x + y)

    def subtract(self):
        print(x + y)

calc = Calc()

try:
    x = int(input("Enter a number: "))
    op = input("Enter an operation: ")
    y = int(input("Enter another number: "))
    if op == "+":
        calc.add()

    elif op == "-":
        calc.subtract()

except Exception as e:
    print("Only numbers are accepted")
