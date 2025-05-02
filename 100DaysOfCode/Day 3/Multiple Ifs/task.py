print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        bill = 5
        print(f"Children tickets are ${bill}.")
    elif age <= 18:
        bill = 7
        print(f"Yound adult tickets are ${bill}.")
    else:
        bill = 12
        print(f"Adult tickets are ${bill}.")

    # Add photo fee
    wants_photo = input("Do you want a photo taken? yes/no: ")
    if wants_photo == "yes":
        bill += 3

    print(f"Your final bill is ${bill}.")

else:
    print("Sorry you have to grow taller before you can ride.")

