print("Welcome to Python Pizza Deliveries!")
bill = 0

# Select size
size = input("What size pizza do you want? S, M or L: ")
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif:
    bill += 25
else:
    print("Wrong input!")


# Select pepperoni
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

# Add extra cheese
extra_cheese = input("Do you want extra cheese? Y or N: ")
if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}.")
