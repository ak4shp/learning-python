class Person:
    # Constructor ->
    def __init__(self, name, age : int, skill, gender) -> None:  
        self.first_name = name
        self.my_age = age
        self.quality = skill
        self.my_gender = gender.title()

    # Methods ->
    def about_me(self):
        return f"I'm {self.first_name} {self.my_age} years old. My skill is {self.quality} and I am a {self.my_gender}."

    def age(self):
        return f"{self.first_name} is {self.my_age} years old."

    def skill(self):
        return f"{self.first_name} has {self.quality} as skill(s)."

    def gender(self):
        return f"{self.first_name} is a {self.my_gender}."

# Objects of class person
roney = Person("Roney", 21, "Bussiness Administration, F1 Racing", "male") 
mira = Person("Mira", 22, "Fashion designing", "FEMALE")
roy = Person("Roy", 34, "Paramounting", "MaLe")

# Calling class methods for the object
print(roy.age())
