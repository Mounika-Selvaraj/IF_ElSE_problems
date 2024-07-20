def calculate(num1, num2, operator):
    try:
        num1 = float(num1)
        num2 = float(num2)

        if operator == '+':
            return num1 + num2
        elif operator == '-':
            return num1 - num2
        elif operator == '*':
            return num1 * num2
        elif operator == '/':
            if num2 == 0:
                return "Error: Division by zero is not allowed."
            return num1 / num2
        else:
            return "Invalid operator."
    except ValueError:
        return "Invalid input. Please enter valid numbers."

def main():
    num1 = input("Enter the first number: ")
    operator = input("Enter an operator (+, -, *, /): ")
    num2 = input("Enter the second number: ")

    result = calculate(num1, num2, operator)
    print(f"Result: {result}")
main()
