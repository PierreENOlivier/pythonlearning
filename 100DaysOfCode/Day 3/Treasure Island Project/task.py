print(r'''
 _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|
                                                                 
                                                                 
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

choice = input("""
You are at a crossroad. Where do you want to go?
(l)eft or (r)ight\n
""").lower()



if choice == "l":
    choice = input(
        f"You arrive at a lake. You see an island in the distance.\n" +
        f"What do you do? (s)wim or (w)ait for a boat.\n"
    ).lower()

    if choice == "s":
        print(
            f"You got attacked by a shark and bled to death! Game Over!")
    elif choice == "w":
        choice = input(
            f"You waited for the boat. You arrived on the island.\n" +
            f"There is a house with 3 doors. Which one do you pick?\n" +
            f"(r)ed door, (y)ellow door, (b)lue door.\n"
        ).lower()

        if choice == "r":
            print(
                f"You enter through the red door.\n" +
                f"The house suddenly catches fire! You are trapped!!!" +
                f"You died... Game Over!"
            )
        elif choice == "b":
            print(
                f"You enter through the blue door.\n" +
                f"It is freezing in there!" +
                f"You catch a glimpse of a white walker before he stabs you with a valyrian steel blade!\n" +
                f"You died... Game Over!"
            )
        elif choice == "y":
            print(
                f"You enter through the yellow door.\n" +
                f"It is so shiny in there!" +
                f"You squint your eyes to catch a glimpse of a mountain of gold!!!\n" +
                f"Congratulation adventurer! You've made!"
            )
        else:
            print("Wrong input!")



    else:
        print("Wrong input!")


elif choice == "r" or choice == "R":
    print(f"You fell into a hole and died! Game Over!")
else:
    print("Wrong input!")