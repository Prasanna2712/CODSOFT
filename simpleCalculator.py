
# Simple Calculator 

def addition(n1, n2):
    return n1 + n2

def subtraction(n1, n2):
    return n1 - n2

def multiplication(n1, n2):
    return n1 * n2

def division(n1, n2):
    if n2 != 0:
        return n1 / n2
    else:
        print("Can't divide by zero...")
        return None

while True:
    n1 = float(input("Enter number 1: "))
    n2 = float(input("Enter number 2: "))

    choice = input("Enter choice that you want ('+', '-', '*', '/'): ")

    if choice == '+':
        print("Result:", addition(n1, n2))
    elif choice == '-':
        print("Result:", subtraction(n1, n2))
    elif choice == '*':
        print("Result:", multiplication(n1, n2))
    elif choice == '/':
        result = division(n1, n2)
        if result is not None:
            print("Result:", result)
    else:
        print("Invalid choice!")

    carry = input("Do you want to calculate again? (yes/no): ")
    if carry.lower() == 'no':
        print("Calculator exiting. Goodbye!")
        break
