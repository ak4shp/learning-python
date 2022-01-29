current_weight = float(input("Weight: "))
unit = input("(L)bs or (K)g: ")

if unit.lower() == 'l':
    weight = current_weight * 0.45
    print(f"You are {weight} kilos")
elif unit.lower() == 'k':
    weight = current_weight / 0.45
    print(f"You are {weight} pounds")
