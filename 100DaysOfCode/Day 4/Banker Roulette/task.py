import random
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel", "Pierre"]
number_of_friends = friends.__len__()

random_index = random.randint(0, number_of_friends - 1)
banker = friends[random_index]
print(f"{banker} is going to pay the bill! Yeah!")

# Random choice
random_friends = random.choice(friends)
print(f"My choice is {random_friends}! Pay the bill, bit**!")