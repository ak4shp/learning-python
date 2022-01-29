def check_even_filter_callback(num):
    if num % 2 == 0:
        return True
    return False


# LAMBDA
"""
    lambda parameter1, parameter2... : single_statement_which_implicitely_returns
ex: 
    lambda num: num + 2

"""


# main
numbers = list(range(1, 11))  # [1, 2, 3, 4, ..., 10]

even_numbers_map = filter(lambda x: x % 2 == 0, numbers) 

print(list(even_numbers_map))