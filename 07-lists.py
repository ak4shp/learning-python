'''EXCERCISE 1 : LARGEST NUMBER IN A LIST'''


# numbers = [2, 32, 324, 4, 5, 1345, 14]


# numbers.sort()  # way 1
# print(numbers[-1])

# print(max(numbers))  # way 2

# max_num = numbers[0]  # way 3
# for num in numbers:
#     if num > max_num:
#         max_num = num
# print(max_num)


'''2D LISTS or MATRIX'''

# matrix = [[11, 23, 3], [3, 45, 87], [43, 45, 0]]

# print(matrix[1] [2])  # prints 3rd element [2] of second list [1] inside list matrix

'''LIST METHODS'''

# numbers = [2, 32, 324, 4, 4, 5, 1345, 14]

# numbers[3] = 10  # change 4 [3] to 10
# numbers.append(65)
# numbers.insert(5, 10)
# numbers.sort()
# numbers.reverse()
# copied = numbers.copy()
# numbers.extend(copied[0:])  # 0: copies all the element of coopied 
# numbers.remove(4)  # value as input
# numbers.pop(2)  # index as input
# print(numbers.count(4))
# print(numbers.index(5))  # input -> value, return -> index
# print(300 in numbers)
# print(numbers)

'''EXCERCISE 2 : REMOVE DUPLICATE FROM THE LIST'''

# given_list = [2, 54, 65, 45, 2, 54, 24, 100]
# max = []
# for num in given_list:
#     if num not in max:
#         max.append(num)
# max.sort()
# given_list.sort()
# print(given_list)
# print(max)


'''TUPLES'''
# prices = (200, 340, 120, 134, 200, 120, 200)
# print(prices.count(200))
# print(prices.index(340))
