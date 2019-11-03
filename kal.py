def calculator():
    def multiply(a, b):
        print(f"The result of the multiplication {a} * {b} is {a * b}.")

    def divide(a, b):
        print(f"The result of the division {a} / {b} is {a / b:6.4}.")

    def add_(a, b):
        print(f"The result of the addition {a} + {b} is {a + b}.")

    def subtract(a, b):
        print(f"The result of the subtraction {a} - {b} is {a - b}.")

    operations = {"*": multiply, r"/": divide, "+": add_, "-": subtract}
    while True:
        operator = input("Please enter operation to be performed [+, -, * or /]:\n")
        if operator in "+-*/":
            break
        else:
            print("Please enter valid operator.")
    number_one = int(input("Please enter first number:\n"))
    number_two = int(input("please enter second number:\n"))
    print()
    operations[operator](number_one, number_two)


if __name__ == "__main__":
    calculator()
