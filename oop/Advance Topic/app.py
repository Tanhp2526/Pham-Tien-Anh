class App:
    def __init__(self, name, description, category):
        self.name = name
        self.description = description
        self.category = category

    def display(self):
        print(f'{self.name} is a(n) {self.category} app that is {self.description}')
