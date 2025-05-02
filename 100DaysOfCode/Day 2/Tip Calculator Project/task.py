print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15? "))
people = int(input("How many people to split the bill? "))

tip_value = bill * tip / 100
total_bill = bill + tip_value
bill_share = total_bill / people
bill_share_rounded = round(bill_share, 2)

print(f"Each person should pay: ${bill_share_rounded:.2f}")