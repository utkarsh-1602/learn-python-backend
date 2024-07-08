class CustomDict(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get_keys(self):
        return list(self.keys())
        # list() is a built-in function used to create a new object in python 
        # When you pass an iterable (like a tuple, set, dictionary keys, etc.) to list(), it converts it into a new list object containing all elements of that iterable.

        # In Python, `keys()` is a method available on dictionary objects (dict type) that returns a view object representing the keys of the dictionary.


# Creating an instance of CustomDict 
my_dict = CustomDict({'a': 1, 'b': 2, 'c': 3})

# Using inherited methods from dict 
print(my_dict.get_keys())
print(my_dict.values())

my_dict['d'] = 4
print(my_dict)