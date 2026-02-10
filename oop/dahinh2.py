class TestClass:
    def sum(self, a = None, b = None, c = None):
        if a is not None and b is not None and c is not None:
            return a + b + c
        elif a is not None and b is not None:
            return a + b
        elif a is not None:
            return a
        else:
            return 0
        
c = TestClass()
print(c.sum())
print(c.sum(1))
print(c.sum(1,2))
print(c.sum(1,2,3))