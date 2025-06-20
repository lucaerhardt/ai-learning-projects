# Ask the user for input

a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
op = input("Enter the operation (+, -, *, /): ")

# Define a calculator function

def calculate(num1, num2, operation):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero!"
    else:
        return "Invalid operation!"

# Call the function and print the result

result = calculate(a, b, op)
print(f"Result: {result}")
