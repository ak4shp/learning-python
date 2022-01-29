'''#1 way to import module -> using dot(.)'''

# import source_class
# hero_hf = source_class.Bike("HF Delux", 2, 97, 70)
# swift = source_class.Car("Swift_Desire", 4, 400, 23)
# volvo = source_class.Commercial("Volvo TMS5", 8, 1080, 12)
# welcome_message = "\n$$$ Welcome to 'FindWheel' $$$"


'''#2 way to import module -> importing individual classes.'''

from source_class import Bike, Car, Commercial
hero_hf = Bike("HF Delux", 2, 97, 70)
swift = Car("Swift_Desire", 4, 400, 23)
volvo = Commercial("Volvo TMS5", 8, 1080, 12)
welcome_message = "\n$$$ Welcome to 'FindWheel' $$$"