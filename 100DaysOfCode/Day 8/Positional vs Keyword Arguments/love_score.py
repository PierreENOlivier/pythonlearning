def calculate_love_score(name1, name2):
    combined_name = name1 + name2
    combined_name = combined_name.upper()
    # TRUE compatibility
    true_comp = 0

    for letter in "TRUE":
        true_comp += combined_name.count(letter)

    # LOVE compatibility
    love_comp = 0
    for letter in "LOVE":
        love_comp += combined_name.count(letter)


    love_score = int(f"{true_comp}{love_comp}")
    print(f"{name1} and {name2} are {love_score}% compatible.")

    return love_score

their_love_score = calculate_love_score("Kanye West", "Kim Kardashian")
print(their_love_score)


