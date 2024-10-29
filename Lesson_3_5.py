def get_multiplied_digits(number):
    str_number = str(number)
    if len(str_number) > 1:
        first = int(str_number[0])
        remaining_ = get_multiplied_digits(int(str_number[1:]))
        if first == 0 or remaining_ == 0:
            return 0
        else:
            return first * remaining_
    else:
        return int(str_number) if int(str_number) != 0 else 1


result = get_multiplied_digits(50234310)
print(result)
