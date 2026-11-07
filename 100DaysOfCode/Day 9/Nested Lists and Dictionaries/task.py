travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Stuttgart", "Berlin"],
}

print(travel_log["France"][1])

nested_list = ["A", "B", ["C", "D"]]

print(nested_list[2][1])

travel_log_counter = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visited": 12
    },
    "Germany": {
        "cities_visited": ["Hamburg", "Berlin", "Stuttgart"],
        "total_visited": 5
    },
}

print(travel_log_counter["Germany"]["cities_visited"][2])