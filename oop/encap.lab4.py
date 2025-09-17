import csv

class CoffeeJournal:
    def __init__(self, file):
        self._file = file
        self._roaster = ""
        self._region = ""
        self._country = ""
        self._stars = ""
        self._new_coffee = []
        self._old_coffee = self.load_coffee()

    def load_coffee(self):
        coffee = []
        with open(self._file) as f:
            reader = csv.reader(f, delimiter=',')
            for row in reader:
                coffee.append(row)
        return coffee 
    
    @property
    def roaster(self):
        return self._roaster
    
    @roaster.setter
    def roaster(self, new_roaster):
        self._roaster = new_roaster

    @property
    def country(self):
        return self._country
    
    @country.setter
    def country(self, new_country):
        self._country = new_country
    
    @property
    def region(self):
        return self._region
    
    @region.setter
    def region(self, new_region):
        self._region = new_region
    
    @property
    def stars(self):
        return self._stars
    
    @stars.setter
    def stars(self, new_stars):
        self._stars = new_stars

    def save(self):
        with open(self._file, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(self._new_coffee)

    def show_coffee(self):
        print()

        if len(self._old_coffee) < 2 and len(self._new_coffee) == 0:
            print("Enter a coffee first")

        elif len(self._old_coffee) > 2 and len(self._new_coffee) == 0:
            for row in self._old_coffee:
                if len(row) == 4:
                    print(f"{row[0]:15} {row[1]:15} {row[2]:15} {row[3]:15}")

        else:
            for row in self._old_coffee:
                if len(row) == 4:
                    print(f"{row[0]:15} {row[1]:15} {row[2]:15} {row[3]:15}")
            for row in self._new_coffee:
                if len(row) == 4:
                    print(f"{row[0]:15} {row[1]:15} {row[2]:15} {row[3]:15}")
        print()

    def add(self):
        self._new_coffee.append([self._roaster, self._country, self._region, self._stars])

def main_menu():
    print("Coffess of the World")
    print("\t1. Show Coffee")
    print("\t2. Add Coffee")
    print("\t3. Save and Quit")
    choice = int(input("Enter the number of your selection: "))
    return choice

def perform_action(choice, coffee):
    if choice == 1:
        coffee.show_coffee()
    elif choice == 2:
        enter_coffee(coffee)
    elif choice == 3:
        quit(coffee)

def enter_coffee(coffee):
    print()
    coffee.roaster = input("Enter the name of the roaster: ")
    coffee.country = input("Enter the country of origin: ")
    coffee.region = input("Enter the region: ")
    coffee.stars = input("Enter the number of stars '*' (1-4): ")
    print()
    coffee.add()

def quit(coffee):
    global run_loop
    coffee.save()
    run_loop = False

run_loop = True
file = "thumuc2.csv"
my_coffe = CoffeeJournal(file)

while run_loop:
    choice = main_menu()
    perform_action(choice, my_coffe)
