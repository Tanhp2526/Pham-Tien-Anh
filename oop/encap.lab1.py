import csv

class CoffeeJournal:
    def __init__(self, file):
        self._file = file
        self._roaster =    ""
        self._country =    ""
        self._region =     ""
        self._stars =    ""
        self._new_coffee = []
        self._old_coffee = self.load_coffee()


    def load_coffee(self):
        coffee = []
        with open(self._file) as f:
            reader = csv.reader(f, delimiter=',')
            for row in reader:
                coffee.append(row)
        return coffee
    

test_object = CoffeeJournal("thumuc.csv")
test_object.load_coffee()
print(test_object._old_coffee)
