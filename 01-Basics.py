# var1 = 12  # initialization
# print(var1)
# str2 = ""

# if str2 == "":
#     print("01")

# else:
#     print("hi")


# $$$ 02 while loop with break $$$
# while True:
#     name = input("\n Enter username ")
#     password = input(" Enter password ")
#     if name == 'Akash' and password == '2020':
#         print('Yay !! You are "Authentic"')
#         break
#     else:
#         print('''No baby! You "can't go" !''')


# $$$ 03 Say hello to strings $$$

# dance = 'She was dancing well yesterday, but today...' 
# print('dancing' in dance)

# dance.upper()
# dance.lower()
# dance.title()
# dance.find()  # gives index of that char or str
# dance.replace()  # you know what it does
# len(dance)  # gives length i.e. number of characters including white space
# '....' in dance  # gives boolean value


# $$$ 04 operator precedance


# $$$ 05 Math function

# import math
# print(math.lcm(2, 4, 12, 15))
# n = int(input("enter n "))
# r = int(input("enter r "))
# combination = math.comb(n, r)
# name = float("nan")
# print(math.isnan(name))
# print(math.floor(value))
# print(type(math.ceil(value)))
# print(type(value))
# temp = value.__ceil__()
# print(temp, type(temp))


# $$$ 06 If statement $$$

day = input('''How is the day : hot = 1
                cold = 2
                othrwise \n''')

if day == '1':
    print("drink a lot of water !")
elif day == '2':
    print('wear warm clothes !')
else:
    print('Are you confused??')

