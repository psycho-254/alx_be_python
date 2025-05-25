# Personal finance calculator

# steps

# step 1
# prompt the user for their monthly income
monthly_income = int(input("Enter your monthly income: "))

# prompt the user for their monthly expenses
monthly_expenses = int(input("Enter your total monthly expenses: "))

# step 2
# calculate monthly savings
monthly_savings = monthly_income - monthly_expenses

# project annual savings at an interest rate of 5%

projected_savings = int(monthly_savings * 12 + (monthly_savings * 12 * 0.05))

print(f"Projected savings after one year, with interest, is: {projected_savings}.")