
class Vehicle:                           # Parent class
    def __init__(self, model, wheel, engine, mileage):
        self.model = model
        self.no_of_wheels = wheel
        self.engine_power = engine
        self.mileage = mileage

    def model_name(self):
        return f"This is {self.model},"

    def check_wheels(self):     
        if self.no_of_wheels == 2:
            say = "a bike."
        elif self.no_of_wheels == 4:
            say = "a car."
        else:
            say = "a commercial vehicle."
        return say

    def specifications(self):
        return f"Specs are: engine -> {self.engine_power} HP, mileage -> {self.mileage} KMPL."


class Bike(Vehicle):
    # def __init__(self, model, wheel : int, engine : int, mileage : int):
    def about_bike(self):  
        about = f"{self.model_name()} {self.check_wheels()} {self.specifications()}"
        return about

class Car(Vehicle):
    def about_car(self):  
        about = f"{self.model_name()} {self.check_wheels()} {self.specifications()}"
        return about

class Commercial(Vehicle):
    def about_commercial(self):
        is_truck = input("Is it a truck: (T)rue / (F)alse : ")
        if is_truck.lower() == 't':
            say = "\nWelcome to your lorry ! here is more about it...\n"
            return F"{say}{self.model_name()} {self.check_wheels()} {self.specifications()} "
        else:
            say = "Sorry! Currently we accept 'truck' only."
            return f"{say} "


hero_hf = Bike("HF Delux", 2, 97, 70)
swift = Car("Swift_Desire", 4, 400, 23)
volvo = Commercial("Volvo TMS5", 8, 1080, 12)
# print(hero_hf.about_bike())
# print(volvo.about_commercial())
welcome_message = "\n$$$ Welcome to 'FindWheel' $$$"

try:
    while True:
        print(welcome_message)
        to_use = int(input("""Please have a look and choose : 
        1 -> Bike
        2 -> Car
        3 -> Commercial Vehicle
        0 -> exit \nI want > """))

        if to_use == 1:
            print(hero_hf.about_bike())
        elif to_use == 2:
            print(swift.about_car())
        elif to_use == 3:
            print(volvo.about_commercial())
        elif to_use == 0:
            print("Thanks for visiting us! Please do come again🤗 ")
            break
        else:
            print("\nInvalid wish! Please type 1, 2, 3 or 0 ")

except ValueError:
    print("\nWARNING...\nYou typed it wrong!! Please choose 1, 2, 3 or 0 next time.")
    