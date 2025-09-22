class Person:
    def __init__(self, name, age, occupation):
        self._name = name 
        self._age = age
        self._occupation = occupation

    def get_name(self):
        return self._name
    
    def set_name(self, new_name):
        self._name = new_name
    
    def get_age(self):
        return self._age
    
    def set_age(self, new_age):
        self._age = new_age

    def get_occupation(self):
        return self._occupation
    
    def set_occupation(self, new_occupation):
        self._occupation = new_occupation

my_person = Person("Citra Curie", 16, "student")
print(my_person.get_name())
my_person.set_name("Rowan Faraday")
print(my_person.get_name())
print(my_person.get_age())
my_person.set_age(18)
print(my_person.get_age())
print(my_person.get_occupation())
my_person.set_occupation("plumber")
print(my_person.get_occupation())