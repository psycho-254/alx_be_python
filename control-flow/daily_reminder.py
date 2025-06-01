# Objective: Create a simplified Python script that uses conditional statements, Match Case, and loops 
# to remind the user about a single, priority task for the day based on time sensitivity.

# Task Description:

# This script will ask the user for a single task, its priority level, and if it is time-sensitive. \
# The program will then provide a customized reminder for that task, 
# demonstrating control flow and loops without relying on data structures to store multiple tasks.

# Instructions:

# 1. Prompt for a Single Task:

    # Ask the user to input a task description and save it into a task variable
    # Prompt for the task’s priority (high, medium, low) and save it into a priority variable
    # In a time_bound variable, Ask if the task is time-bound (yes or no)

# 2. Process the Task Based on Priority and Time Sensitivity:

    # Use a Match Case statement to react differently based on the task’s priority.
    # Within the Match Case or after, use an if statement to modify the reminder if the task is time-bound.

# 3. Provide a Customized Reminder:

    # Print a reminder about the task that includes its priority level and 
    # whether immediate action is required based on time sensitivity.
    # A message should be ‘that requires immediate attention today!’

task = input("Enter your task: ")
priority = input("Priority (highmedium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")



match priority:
    case "high" if priority == "high" and time_bound == "yes":
        print(f"Reminder: {task} is a high priority task that requires immediate attention today!")
    case "medium" if priority == "medium" and time_bound == "yes":
        print(f"Reminder: {task} is a medium priority task. Delegate it.")
    case "low" if priority == "high" and time_bound == "no":
        print(f"Note: {task} is a low priority task. You can do it later.")
    case _:
        print("Invalid input, try again")
    
    
