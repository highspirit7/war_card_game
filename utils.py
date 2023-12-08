def convert_to_ordinal(number):
    # To handle the exceptional cases(11: 11th, 12: 12th, 13: 13th)
    if 10 <= number % 100 <= 20:
        suffix = "th"
    else:
        suffix = {1: "st", 2: "nd", 3: "rd"}.get(number % 10, "th")

    return f"{number}{suffix}"
