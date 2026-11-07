from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

machine_is_on = True
while machine_is_on:
    items = menu.get_items()

    choice = input(f"What would you like? ({items}): ")
    if choice == "off":
        machine_is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        selected_item = menu.find_drink(choice) # Returns an object with attributes name, cost, ingredients
        if selected_item is None:
            continue


        while not coffee_maker.is_resource_sufficient(selected_item):
            coffee_maker.refill_machine()

        print(f"That will be ${selected_item.cost} for a {selected_item.name}.")
        if money_machine.make_payment(selected_item.cost): # process payment and return status
            coffee_maker.make_coffee(selected_item)


