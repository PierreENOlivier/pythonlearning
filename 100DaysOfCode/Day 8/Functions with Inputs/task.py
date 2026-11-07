def greet():
    print("Hello Jack")
    print("How do you do, Jack?")
    print("Isn't the weather crap?")

greet()

print("\n")

username = input("What is your name? ")

def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do, {name}?")
    print("Isn't the weather crap?")

greet_with_name(username)
