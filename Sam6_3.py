input_str = input("Введите строку из цифр: ")

def func(digits):
    my_dict = {}
    for char in digits:
        digit = int(char)
        if digit in my_dict:
            my_dict[digit] += 1
        else:
            my_dict[digit] = 1
    sorted_dict = sorted(my_dict.items(), key = lambda item: (-item[1], item[0]))
    return dict(sorted_dict[:3])

print(func(input_str))
