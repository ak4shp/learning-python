from functools import reduce
from input_utils import get_measurements

mensuration_select_message = """\nSelect Shape...\n
\t\t1 -> Circle
\t\t2 -> Triangle
\t\t3 -> Rectangle
\t\t4 -> Cone
\t\t5 -> Cylinder
\t\t6 -> Sphare
\t\t0 -> Back to 'Home Menu'"""

selection_message = """!! Choose applicable !!
(P)erimeter
(A)rea
(V)olume
Note : Press any other key to go back to 'Shape Menu'  ->>> """


class ShapeList:
    GO_BACK = 0
    CIRCLE = 1
    TRIANGLE = 2
    RECTANGLE = 3
    CONE = 4
    CYLINDER = 5
    SPHARE = 6


class Mensuration:
    def circle(measurements):
        area = 3.14 * measurements[0] ** 2
        perimeter = 2 * 3.14 * measurements[0]
        result = [area, perimeter]
        return result

    def triangle(measurements):
        area = 0.2 * measurements[0] * measurements[1]
        perimeter = reduce(lambda total, num: total + num, measurements)
        result = [area, perimeter]
        return result

    def rectangle(measurements):
        area = measurements[0] * measurements[1]
        perimeter = reduce(lambda total, num: total + num, measurements)
        result = [area, perimeter]
        return result

    def cone(measurements):
        volume = (1 / 3) * 3.14 * measurements[0] ** 2 * measurements[1]
        curve_area = 3.14 * measurements[0] * measurements[1]
        total_area = curve_area + 3.14 * measurements[0] ** 2
        result = [volume, curve_area, total_area]
        return result

    def cylinder(measurements):
        volume = 3.14 * measurements[0] ** 2 * measurements[1]
        curve_area = 2 * 3.14 * measurements[0] * measurements[1]
        total_area = curve_area + 2 * 3.14 * measurements[0] ** 2
        result = [volume, curve_area, total_area]
        return result

    def sphare(measurements):
        volume = 3.14 * measurements[0] ** 3
        total_area = 4 * 3.14 * measurements[0] ** 2
        result = [volume, total_area]
        return result


def mensuration_calculation():
    while True:
        print(mensuration_select_message)
        operation = int(input("\t  ->> "))

        if operation == ShapeList.GO_BACK:
            break

        elif operation == ShapeList.CIRCLE:
            dimensions = get_measurements()
            result = Mensuration.circle(dimensions)
            while True:
                selection = input(selection_message)
                if selection.lower() == "a":
                    print(f"Area = {result[0]}\n")
                elif selection.lower() == "p":
                    print(f"Perimeter = {result[1]}\n")
                else:
                    print("\nNOT APPLICABLE !!!\n")
                    break

        elif operation == ShapeList.TRIANGLE:
            dimensions = get_measurements()
            result = Mensuration.triangle(dimensions)
            while True:
                selection = input(selection_message)
                if selection.lower() == "a":
                    print(f"Area = {result[0]}\n")
                elif selection.lower() == "p":
                    print(f"Perimeter = {result[1]}\n")
                else:
                    print("\nNOT APPLICABLE !!!\n")
                    break

        elif operation == ShapeList.RECTANGLE:
            dimensions = get_measurements()
            result = Mensuration.rectangle(dimensions)
            while True:
                selection = input(selection_message)
                if selection.lower() == "a":
                    print(f"Area = {result[0]}\n")
                elif selection.lower() == "p":
                    print(f"Perimeter = {result[1]}\n")
                else:
                    print("\nNOT APPLICABLE !!!\n")
                    break

        elif operation == ShapeList.CONE:
            dimensions = get_measurements()
            result = Mensuration.cone(dimensions)
            while True:
                selection = input(selection_message)
                if selection.lower() == "v":
                    print(f"Volume = {result[0]}\n")
                elif selection.lower() == "a":
                    print(f"Curve surface area = {result[1]}\nTotal surface area = {result[2]}\n")
                else:
                    print("NOT APPLICABLE !!!\n")
                    break

        elif operation == ShapeList.CYLINDER:
            dimensions = get_measurements()
            result = Mensuration.cylinder(dimensions)
            while True:
                selection = input(selection_message)
                if selection.lower() == "v":
                    print(f"Volume = {result[0]}\n")
                elif selection.lower() == "a":
                    print(f"Curve surface area = {result[1]}\nTotal surface area = {result[2]}\n")
                else:
                    print("NOT APPLICABLE !!!\n")
                    break
        
        elif operation == ShapeList.SPHARE:
            dimensions = get_measurements()
            result = Mensuration.sphare(dimensions)
            while True:
                selection = input(selection_message)
                if selection.lower() == "v":
                    print(f"Volume = {result[0]}\n")
                elif selection.lower() == "a":
                    print(f"Total surface area = {result[1]}\n")
                else:
                    print("NOT APPLICABLE !!!\n")
                    break

# def show_result()