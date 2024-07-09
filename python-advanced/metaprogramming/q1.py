# Introspection

import inspect

class MyClass:
    def my_method(self):
        pass

obj = MyClass()

print(type(obj))  # <class '__main__.MyClass'>
print(dir(obj))   # List of attributes and methods
print(inspect.getmembers())  # List of members with their values
