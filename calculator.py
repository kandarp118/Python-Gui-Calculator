def calculator():
    print("--- Simple Python Calculator ---")

    try:
        num1 = float(input("Enter the first number: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    print("\nSelect operation:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")

    operation = input("Enter choice (1/2/3/4): ")

    try:
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    result = None

    if operation == '1' or operation == '+':
        result = num1 + num2
        print(f"\n{num1} + {num2} = {result}")

    elif operation == '2' or operation == '-':
        result = num1 - num2
        print(f"\n{num1} - {num2} = {result}")

    elif operation == '3' or operation == '*':
        result = num1 * num2
        print(f"\n{num1} * {num2} = {result}")

    elif operation == '4' or operation == '/':
        if num2 != 0:
            result = num1 / num2
            print(f"\n{num1} / {num2} = {result}")
        else:
            print("\nError: Cannot divide by zero!")

    else:
        print("\nInvalid operation choice. Please select 1, 2, 3, or 4.")

    print("---------------------------------")

if __name__ == "__main__":
    calculator()