from mensuration import Mensuration
from numerical import numeric_calculation

welcome = """\nWelcome to 'MATH_UTILS'. Please select Operation Category...\n
\t1 -> Basic Operations
\t2 -> Mensuration 
\t0 -> Exit"""

class Options:
    GO_BACK = 0
    NUMERICAL = 1
    MENSURATION = 2
    
    
def home_menu():
    while True:
        print(welcome)
        option = int(input("--> "))

        if option == Options.GO_BACK:
            break
        elif option == Options.NUMERICAL:
            numeric_calculation()
        elif option == Options.MENSURATION:
            m = Mensuration()
            m.perform_operation()

if __name__ == "__main__":
    home_menu()
