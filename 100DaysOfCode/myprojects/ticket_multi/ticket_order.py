"""
Ticketing machines for selecting tickets and compiling the full bill
"""
# TODO
number_of_tickets = int(input("How many tickets do you need? "))

selected = 0
while selected < number_of_tickets:
    adult_tickets_number = int(input("How many adults"))