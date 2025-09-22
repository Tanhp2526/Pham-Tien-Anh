class Alpha:
    def show(self):
        print("I am from class Alpha")

    def hello(self):
        print("Hellp from Alpha")

class Bravo(Alpha):
    def show(self):
        print("I am from class Bravo")
    
    def hello(self):
        print("Hello from Bravo")

c = Bravo()
c.show()