from functools import reduce


def get_operands():
    operands_string_list = input("Enter operands(space separated) >> ").split()
    operands = list(map(int, operands_string_list))
    return operands

numeric_select_message = """\nSelect operation...\n
\t\t1 -> Summation
\t\t2 -> Subtraction
\t\t3 -> Multiplication
\t\t4 -> Division
\t\t5 -> Exponential
\t\t6 -> Average
\t\t0 -> Back to Home Menu"""

class Operations:
    GO_BACK = 0
    ADD = 1
    SUBTRACT = 2
    MULTIPLY = 3
    DIVIDE = 4
    EXPONENT = 5
    AVERAGE = 6

class BasicOperation:                # Basic operations.
    # functions
    def addition(operands):
        total = 0
        for element in range(len(operands)):
            total += operands[element]
        return total

    def subtract(operands):
        result = operands[0]
        for element in operands[1:]:
            result -= element
        return result

    def multiply(operands):
        mul = 1
        for element in range(0, len(operands)):
            mul *= operands[element]
        return mul

    def division(operands):
        div = 0
        if len(operands) == 2:
            div = operands[0] / operands[1]
        else:
            div = "Invalid input! please give only 2 values for division"
        return div


class AlternativeBasicOperation:
    def addition(operands):
        total = reduce(lambda total, num: total + num, operands)
        return total

    def subtract(operands):
        total = reduce(lambda total, num: total + num, operands[1:])
        result = operands[0] - total
        return result
    
    def multiply(operands):
        result = reduce(lambda total, num: total * num, operands)
        return result


class AdditionalOperation:
    def exponential(operands, power):
        result = []
        for element in range(0, len(operands)):
            value = operands[element] ** power
            result.append(value)
        return result

    def average(operands):
        total = AlternativeBasicOperation.addition(operands)
        result = total / len(operands)
        return result


def numeric_calculation():
    while True:
        print(numeric_select_message)
        operation = int(input("\t  ->> "))

        if operation == Operations.GO_BACK:
            break

        elif operation == Operations.ADD:
            numbers = get_operands()
            print(BasicOperation.addition(numbers))

        elif operation == Operations.SUBTRACT:
            numbers = get_operands()
            print(BasicOperation.subtract(numbers))

        elif operation == Operations.MULTIPLY:
            numbers = get_operands()
            print(BasicOperation.multiply(numbers))

        elif operation == Operations.DIVIDE:
            numbers = get_operands()
            print(BasicOperation.division(numbers))
        
        elif operation == Operations.EXPONENT:
            numbers = get_operands()
            power = int(input("Enter power: "))
            print(AdditionalOperation.exponential(numbers, power))

        elif operation == Operations.AVERAGE:
            numbers = get_operands()
            print(AdditionalOperation.average(numbers))
        