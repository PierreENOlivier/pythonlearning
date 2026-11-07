from art import logo

def add(n1, n2):
    return n1 + n2

def substract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide
}

res = operations["*"](4, 8)
print(res)

def calculator():

    print(logo)

    n1 = float(input("Enter first number: "))

    run_calculation = True
    while run_calculation:

        for symbol in operations:
            print(symbol)

        operator = input("Enter operator: ")

        n2 = float(input("Enter next number: "))

        res = operations[operator](n1, n2)

        print(f"{n1} {operator} {n2} = {res}")

        choice = input(
            f"(c)ontinue with {res}, " +
            f"or start (n)ew calculation," +
            f"or (q)uit" +
            "\n"
        )

        if choice == "c":
            n1 = res
        elif choice == "n":
            run_calculation = False
            calculator()
        else:
            return res


total = calculator()
print(f"Total: {total}")