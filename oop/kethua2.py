class Person():
    def __init__(self, name, age, occupation):
        self.name = name
        self.age = age
        self.occupation = occupation

    def say_hello(self):
        print("Xin chao ban:", self.name)

class SuperHero(Person):
    def say_hello(self):
        return super().say_hello()

Sieunhan = SuperHero("Anh", "20", "Sinh Vien")
Sieunhan.say_hello()
print(isinstance(Person, SuperHero))
print(isinstance(SuperHero, Person))