'''Calculate total of a list'''

# item_rate = [11, 56, 239, 353, 8, 8, 10, 23, 15, 75]
# addition = 0
# for item in item_rate:
#     addition = addition + item
#     item += 1

# print(addition)


'''NESTED LOOPS'''
# 01- Print F

# numbers = [5, 2, 5, 2, 2]  # operand for 'for' loop
# for num in numbers:
#     print("X"*num)   # Cheap way !!!!!

numbers = [5, 2, 5, 2, 2]  # operand for 'for' loop
numbers1 = [5, 2, 5, 2, 5]
numbers2 = [5, 2, 5, 2, 5]
numbers3 = [2, 2, 2, 2, 5]

operands = [numbers, numbers1, numbers2, numbers3]
for nums in operands:
    for num in nums:
        output = ""
        for show in range(num):
            output += "@"
        # output += "\n"
        print(output)
    print()
    