# Objective: Familiarize yourself with Python’s datetime module by writing a script that performs specified operations with dates and times.

# Task Instructions:
# Your task is to create a Python script named explore_datetime.py. 
# This script will demonstrate your ability to use the datetime module for handling dates and times in Python.

# Part 1: Display the Current Date and Time

# Research how to use the datetime module to obtain the current date and time.
# Create a function with a name display_current_datetime and
# save the current date inside a current_date variable
# Format and print the current date and time in a readable format, such as “YYYY-MM-DD HH:MM:SS”.

from datetime import datetime

def display_current_datetime():
    now = datetime.now()
    formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
    print(formatted_date)

display_current_datetime()


# Part 2: Calculate a Future Date

# Prompt the user to enter a number of days (as an integer).
# Create a function with a name calculate_future_date and
# saves the future date inside a future_date variable
# Calculate what the date will be after adding the specified number of days to the current date.
# Print the future date in a format like “YYYY-MM-DD”.

from datetime import datetime, timedelta
days = int(input("Enter the number of days to add to the current date: "))

def calculate_future_date():
    today = datetime.now()
    future_date = today + timedelta(days)
    formatted_date = future_date.strftime("%Y-%m-%d")
    print(formatted_date)
    
calculate_future_date()








# Example Output (Hypothetical):
# Current date and time: 2024-03-25 15:30:45
# Enter the number of days to add to the current date: 10
# Future date: 2024-04-04