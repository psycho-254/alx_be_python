# Objective: Learn to use Match Case statements for handling multiple operations in a simple calculator program.

# Task Description:

# This calculator will prompt the user to enter two numbers and select an operation 
# (addition, subtraction, multiplication, or division). 
# The script will then perform the selected operation using a Match Case statement and display the result.

# Instructions:

# Prompt for User Input:

# Ask the user to input two numbers (one at a time) using: Enter the first number: and Enter the second number:
# Make sure you use num1 and num2 for first and second numbers

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Ask for the type of operation they’d like to perform: Choose the operation (+, -, *, /):.

operation = input("Choose the operation (+, -, *, /): ")

# Perform the Calculation Using Match Case:

match operation:
    case "+":
        print(f"The result is {num1 + num2}.")
    case "-":
        print(f"The result is {num1 - num2}.")
    case "*":
        print(f"The result is {num1 * num2}.")
    case "/":
        if num2 == 0:
            print("Cannot divide by zero.")
        else:
            print(f"The result is {num1 / num2}.")
    case _ :
        print("Invalid operation.")


# Implement a Match Case statement that executes the chosen operation based on the user’s input.
# For addition (+), subtract (-), multiply (*), and divide (/).
# Ensure to handle the division by zero case gracefully, displaying a message if the user tries to divide by zero.
# Output the Result:

# Display the result of the operation in a user-friendly message, e.g., The result is [result].