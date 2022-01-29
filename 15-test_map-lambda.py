def make_even_filter_callback(num):
    if num % 2 != 0:
        return num + 1
    return num

def to_string(num):
    return str(num)

def add_10(num):
    return num + 10

# main
numbers = list(range(1, 11))  # [1, 2, 3, 4, ..., 10]

even_numbers_map = map(add_10, numbers) 

print(list(even_numbers_map))