number_str = input("Enter integer value: ")

# without string
number = int(number_str)
if number <= 0:
    print("Value must be positive")
else:
    is_descending = True
    previous_digit = 0

    while number != 0:
        current_digit = number % 10

        if current_digit < previous_digit:
            is_descending = False
            break

        previous_digit = current_digit
        number //= 10

    print((
        "Digits are in descending order" if is_descending
        else "Digits are not in descending order"
    ))

# with string
# assuming input only contains numbers, skipping isdigit check
if number_str.startswith("-"):
    print("Value must be positive")
else:
    # using the fact '9' > '8' > '7' > ... > '0'
    is_descending = True
    for i in range(len(number_str) - 1):
        if number_str[i] < number_str[i + 1]:
            is_descending = False
            break

    print((
        "Digits are in descending order" if is_descending
        else "Digits are not in descending order"
    ))
