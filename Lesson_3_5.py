def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number)
    if len(str_number) > 1:
        first = int(str_number[0])
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return int(str_number)


result = get_multiplied_digits(505012123)
print(result)
