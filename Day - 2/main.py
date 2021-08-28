# Tip Calculator Program

print("Welcome to the tip calculator!")

total_bill = float(input("What was the total bill? $"))
percentage_tip = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
person_to_pay = int(input("How many people to split the bill? "))

amount_to_pay = (total_bill / person_to_pay) * (1 + (percentage_tip / 100))

print(f"Each person should pay: ${amount_to_pay:.2f}")
