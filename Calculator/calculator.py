def get_number(message):
    while True:
        try:
            number = float(input(message))
        except ValueError:
            print("Please enter a valid number.")
            continue
        return number

def get_operation():
    while True:
        operation = input("Choose an operation (+, -, *, /): ")
        if operation == "+" or operation == "-" or operation == "*" or operation == "/":
            return operation
        else:
            print("Please enter a valid operation.")

def calculate(first_number, operation, second_number):
    result = None

    if operation == "+":
        result = first_number + second_number
    elif operation == "-":
        result = first_number - second_number
    elif operation == "*":
        result = first_number * second_number
    elif operation == "/":
        if second_number == 0:
            print("Cannot divide by zero.")
        else:
            result = first_number / second_number
    return result

def ask_again():
    while True:
        answer = input("Would you like to make another calculation? (yes/no): ").lower().strip()

        if answer == "yes" or answer == "no":
            return answer
        else:
            print("Please enter yes or no.")

def show_history(history):
    if len(history) == 0:
        print("No calculation in history.")
    else:
        print("Calculation History:")
        for number, calculation in enumerate(history, start=1):
            print(f"{number}. {calculation}")

history = []

while True:
    first_number = get_number("Enter the first number: ")
    operation = get_operation()
    second_number = get_number("Enter the second number: ")

    result = calculate(first_number, operation, second_number)

    if result is not None:
        print(result)
        history.append(f"{first_number} {operation} {second_number} = {result}")
        

    answer = ask_again()
    if answer == "no":
        show_history(history)
        print("Thanks for using the calculator!")
        break

    

