number = int(input("Give me an integer: "))
remainder_div = number % 2

if remainder_div == 0:
    print(f'{number} is Even')
else:
    print(f'{number} is Odd')
