class Employee:
  def __init__(self, name, title):
    self.name = name
    self.title = title
    
  def display(self):
    print(f'Employee: {self.name}')
    print(f'Title: {self.title}')

def greeting():
  print('Hello from the "class_definition" module')