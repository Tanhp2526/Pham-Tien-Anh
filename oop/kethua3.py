class Dinosaur:
    def __init__(self, size, weight):
        self.size = size
        self.weight = weight

class Carnivore:
    def __init__(self, diet):
        self.diet = diet

class Tyrannosaurus(Dinosaur, Carnivore):
    pass

tiny = Tyrannosaurus(12, 100)
print(tiny.__dict__)