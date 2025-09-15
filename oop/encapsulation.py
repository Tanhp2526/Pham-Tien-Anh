class PrivateClass:
    def __init__(self):
        self.__private_attribute = "I am a private attribute"
    
        
obj = PrivateClass()
print(obj._PrivateClass__private_attribute)