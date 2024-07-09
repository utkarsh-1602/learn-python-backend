
class MyClass(type):
    def __new__(cls, name, bases, dct):
        print(f"Creating class {name}")
        return super().__new__(cls, name, bases, dct)
    
class MyNewClass(x = MyClass):
    pass

my_instance = MyNewClass()