class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def __str__(self):
        return f'{self.name} is a {self.breed}'
    
dogs = []
dogs.append(Dog("Rockey", "Ngao Tay Tang"))
dogs.append(Dog("Nick", "bet de"))
print(dogs)