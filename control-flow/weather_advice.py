# Task Description:

# This script will ask the user about the current weather conditions and provide clothing recommendations based on the input. 
# This task aims to demonstrate the use of if, elif, and else statements to make decisions in a program.

# Instructions:

# Prompt User for Weather Input:

# Ask the user to input the current weather from a predefined set of conditions: sunny, rainy, or cold.
# Use the prompt: What's the weather like today? (sunny/rainy/cold):.
todays_weather = input("What's the weather like today? (sunny/rainy/cold)? ").lower()


# Provide Clothing Recommendations:
# Based on the user’s input, your program will recommend different types of clothing:

    
if todays_weather == "sunny":  # If the weather is “sunny”, recommend: Wear a t-shirt and sunglasses.
    print("Wear a t-shirt and sunglasses.")
    
elif todays_weather == "rainy": # If the weather is “rainy”, recommend: Don't forget your umbrella and a raincoat.
    print("Don't forget your umbrella and a raincoat.")

elif todays_weather == "cold":# If the weather is “cold”, recommend: Make sure to wear a warm coat and a scarf.
    print("Make sure to wear a warm coat and a scarf.")
                                
else: # Include an else statement that handles unexpected input by printing: Sorry, I don't have recommendations for this weather.
    print("Sorry, I don't have recommendations for this weather.")

    
# Output the Recommendation:

# Print the clothing recommendation based on the weather condition provided by the user.