def format_name(
        f_name: str,
        l_name: str,
):
    """
    Format a name and return a formatted name.
    :param f_name: str
    :param l_name: str
    :return: str

    """
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()

    return f"{formatted_f_name} {formatted_l_name}"



res = format_name("Pierre", "Garthur")
print(res)