class Phone:
    def __init__(self, model, storage, megapixels):
        self._mode = model
        self._storage = storage
        self._megapixels = megapixels

    def get_mode(self):
        return self._mode
    
    def set_mode(self, new_mode):
        self._mode = new_mode

my_phone = Phone("iPhone", 256, 12)
print(my_phone.get_mode())
my_phone.set_mode("Galaxy")
print(my_phone.get_mode())