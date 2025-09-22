class Contact:
    def __init__(self):
        self.view = "list"
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
                print("\nClosing the contact the list ...\n")
                break
    
    def show_list(self):
        print()
        if len(self.contact_list) == 0:
            self.choice = input("(A)dd a new contact \n(Q)uit \n> ").lower()

        else:
            for index , contact in enumerate(self.contact_list):
                print(f"{index + 1}) {contact.first_name} {contact.last_name}")
            self.choice = input('\n(#) Select a name \n(A)dd a new contact\n(Q)uit \n> ').lower()
        self.handel_choice()
    
    def show_infor(self):
        pass

    def add_contact(self):
        new_contact = Information()
        self.contact_list.append(new_contact)

    def handel_choice(self):
        if self.choice == 'q':
            self.view = "quit"
        elif self.choice == 'a' and self.view == "list":
            self.view == "add"
        elif self.choice.isnumeric() and self.view == "list":
            index = int(self.choice) - 1
            if index >= 0 and index < len(self.contact_list):
                self.index = index
                self.view = "infor"

class Information:
    def __init__(self):
        self.first_name = input('Enter their first name: ')
        self.last_name = input('Enter their last name: ')
        self.personal_phone = input('Enter their personal phone number: ')
        self.personal_email = input('Enter their personal email address: ')
        self.work_phone = input('Enter their work phone number: ')
        self.work_email = input('Enter their work email address: ')
        self.title = input('Enter their work title: ')

contacts = Contact()
contacts.display()