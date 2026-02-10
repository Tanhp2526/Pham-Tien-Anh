class Contacts:
    def __init__(self):
        self.view = "quit"
        self.contact_list = []
        self.choice = None 
        self.index = None
    
    def display(self):
        while True:
            if self.view == "list":
                self.show_list()
            elif self.view == "infor":
                self.show_infor()
            elif self.view == "add":
                print()
                self.add_contact()
            elif self.view == "quit":
                print("\nClosing the contact list ...\n")
                break
    
    def show_list(self):
        pass
    def show_infor(self):
        pass
    def add_contact(self):
        pass

c = Contacts()
c.display()