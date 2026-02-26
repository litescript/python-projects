from art import logo
print(logo)

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

cont_num = None
done = False

def maths(first=None):
    if first is None:
        first = float(input("Enter the first number: "))
    while True:
        operator = input("Select an operation (+, -, *, /): ").strip()
        if operator in operations:
            break
        print("Invalid operation. Please try again.")
    while True:
        second = float(input("Enter the second number: "))
        if operator != "/" or second != 0:
            break
        print("Cannot divide by zero! Please try again.")
    return operations[operator](first, second)

while not done:
    result = maths(cont_num)
    print(result)
    again = input("Would you like to continue with another number? (y/n): ").strip().casefold()
    if again in ("y", "yes"):
        cont_num = result
    else:
        print("Goodbye!")
        done = True
