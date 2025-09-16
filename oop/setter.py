class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if type(new_name) != str:
            raise TypeError("Name must be expressed as a string")
        self._name = new_name

    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, new_age):
        if new_age < 0:
            raise ValueError("Age must be a positive number.")
        self._age = new_age

c = Person("Anh", 21)
print(c.name)
print(c.age)
c.age = 22
c.name = "Long"
print(c.name)
print(c.age)
        