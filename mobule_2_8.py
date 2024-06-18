def get_multiplied_digits(*number):
    first = int(number[0])
    if not number:
        return 0
    if len(number) == 1:
        return first
    else:
        return first * get_multiplied_digits(int(str_number[1:]))

str_number = '40203'
print(get_multiplied_digits(str_number))




