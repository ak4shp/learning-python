'''EXCERCISSE 1: EMOJI CONVERTER'''

# def greet_me(name, message):
#     words = message.split(" ")  # Converts input message into list
#     emojis = {                  # Dictionary
#         ":)" : "😃",
#         ":(" : "🙁",
#         ":o" : "😮",
#         ":|" : "😑"}
#     output = ""                 # Can be appended
#     for word in words:
#         output += emojis.get(word, word) + " "   # Appending using get() method
#     return f"Dear {name}. Your message is : " + output


# welcome = '''!!! Welcome to the emoji converter !!!  You can choose following symbols ->                 
#     ":)" 
#     ":(" 
#     ":o" 
#     ":|"
#     '''
# print(welcome)
# first_name = input("Enter your first name: ")
# value = input(f"hey {first_name} what do you want to say: ")
# print(greet_me(first_name, value))


'''EXCERCISE 2: WEIGHT CONVERTER'''

# def weight_converter(weight, unit):
#     if unit.lower() == 'l':                  # convert unit to lower case
#         weight = current_weight * 0.45       # lbs to kg
#         print(f"You are {weight} kilos")
#     elif unit.lower() == 'k':
#         weight = current_weight / 0.45       # kg to lbs
#         print(f"You are {weight} pounds")    # Print here


# current_weight = float(input("Weight: "))
# unit = input("(L)bs or (K)g: ")
# weight_converter(current_weight, unit)       # Can not print just call as kilos and pounds differs depending on input.