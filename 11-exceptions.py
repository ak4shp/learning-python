'''Error Handling (Exception) -> Weight converter from code "03-weight.py"'''

# try:
#     current_weight = float(input("Weight: "))
#     unit = input("(L)bs or (K)g: ")

#     if unit.lower() == 'l':                 # convert unit to lower case
#         weight = current_weight * 0.45      # lbs to kg
#         print(f"You are {weight} kilos")
#     elif unit.lower() == 'k':
#         weight = current_weight / 0.45      # kg to lbs
#         print(f"You are {weight} pounds")
#     else:
#         print("Please choose between 'l' and 'k'")
#         unit = input("(L)bs or (K)g: ")     # Trying again for right weight type

#         if unit.lower() == 'l':
#             weight = current_weight * 0.45  
#             print(f"You are {weight} kilos")
#         elif unit.lower() == 'k':
#             weight = current_weight / 0.45   
#             print(f"You are {weight} pounds")

# except ValueError:                          # If invalid value given
#     print("Invalid value!! Please enter a numerical value only.")


