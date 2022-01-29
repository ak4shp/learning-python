def get_operands():
    operands_string_list = input("Enter operands(space separated) >> ").split()
    operands = list(map(int, operands_string_list))
    return operands

def get_measurements():
    sides_string_list = input("Enter specific measurement(s) required for this shape(space seperated) >> ").split()
    measurements = list(map(int, sides_string_list))
    return measurements