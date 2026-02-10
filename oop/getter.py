class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age
    @property
    def name(self):
        return self._name
    
    @property
    def age(self):
        return self._age
    
person = Person("Anh", 25)
print(person.name)
print(person.age)