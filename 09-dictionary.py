# guest = {
#     "name" : "Lucy Grace",
#     "gift" : "teddybear",
#     "ate_food" : True
# }
# guest["arrived_at"] = "12 : 30 PM"
# print(guest["ate_food"])
# print(guest["arrived_at"])

# print(guest)

'''EXCERCISE : DIGITS TO WORD CONVERTER'''

phone = input("What is your contact number (seperate using space) > ")
letters = phone.split(" ")
digits_to_word = {
    "0" : "zero",
    "1" : "one",
    "2" : "two",
    "3" : "three",
    "4" : "four",
    "5" : "five",
    "6" : "six",
    "7" : "seven",
    "8" : "eight",
    "9" : "nine"
}
output = ""
for ch in letters:
    output += digits_to_word.get(ch, ch) + " "
print(output)    