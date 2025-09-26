class Car:
    def __init__(self, make, model, year, engine):
        self.make = make
        self.model = model
        self.year = year
        self.engine = engine


    def describe(self):
        print(f'{self.year} {self.make} {self.model}')

class Engine:
    def __init__(self, configuration, displacement, horsepower, torque):
        self.configuration = configuration
        self.displacement = displacement
        self.horsepower = horsepower
        self.torque = torque

    def ignite(self):
        print('Vroom, vroom')

    def start(self):
        self.engine.ignite()

my_engine = Engine("V8", 5.8, 326, 344)
my_car = Car("De Tomaso", "Pantera", 1979, my_engine)
my_car.start()