# Function to perform the operation
def calculate(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error! Division by zero."
    else:
        return "Invalid operation."

# Get user input
user_input = input("Enter math question (e.g., 10 + 5): ")

# Split the input into parts
parts = user_input.split()

# Convert numbers and perform the operation
num1 = int(parts[0])
operation = parts[1]
num2 = int(parts[2])

# Perform the operation
result = calculate(num1, num2, operation)

# Print the result, removing decimal point if the result is a whole number
if isinstance(result, float) and result.is_integer():
    result = int(result)  # Convert to integer if the result is a whole number

print(f"{num1} {operation} {num2} = {result}")
