# def print_params(a = 1, b = 'строка', c = True):
#     print(a, b, c)
#
# print_params(b = 25)
# print_params(c = [1, 2, 3])

values_list = [24, 'kolobok', False]
values_dict = {'a': 42, 'b': 'новая строка', 'c': None}

def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params(*values_list)
print_params(**values_dict)

values_list_2 = ['тест', 3.5]
print_params(*values_list_2, 42)