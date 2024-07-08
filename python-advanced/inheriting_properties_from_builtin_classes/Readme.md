# Inheriting Properties from Built-in classes 

- In Python, you can inherit properties and methods from built-in classes by using inheritance. Built-in classes in Python, such as `list`, `dict`, `str`, etc., provide a rich set of functionalities that can be extended or customized through inheritance.

## Inheriting from `list`

- Let's say you want to create a custom list class that adds some additional functionality to a standard list : [Refer q1.py](./q1.py)

- `super()` function returns a proxy object that represents the parent class of the current instance. It allows you to call methods of the superclass from within a subclass.

[Refer q3.py](./q3.py)

- `__setitem__()` is a special method used for assignment to an index in an object. It is invoked when you use square brackets ([]) to assign a value to an index in an object, typically in sequence-like objects such as lists, dictionaries, or custom classes that implement this method.


## Inheriting from `dict`

- Similarly, you can inherit from the dict class to create a custom dictionary with additional functionalities : [Refer q2.py](./q2.py)

- `list()` function : 
    - `list()` is a built-in function used to create a new object in python. 
    - When you pass an iterable (like a tuple, set, dictionary keys, etc.) to `list()`, it converts it into a new list object containing all elements of that iterable.
    - If `list()` is called without arguments, it returns an empty list.

- `keys()` method:
    - In Python, `keys()` is a method available on dictionary objects (dict type) that returns a view object representing the keys of the dictionary.

[Refer q4.py](./q4.py)

- The __getitem__() method : 

    - in Python is a special method, also known as a magic method or dunder method, which allows an object to be accessed using the square bracket notation ([]). This method is automatically called when you use square brackets to access an item from an object, such as a list, dictionary, or a custom object that implements `__getitem__()`.

    - `__getitem__()` allows objects to support indexing and slicing operations. It defines what happens when you use obj[key] to retrieve an item from obj.

    ```python
    class CustomList:
        def __init__(self, data):
            self.data = data
        
        def __getitem__(self, index):
            return self.data[index]

    # Creating an instance of CustomList
    my_list = CustomList([1, 2, 3, 4, 5])

    # Accessing elements using square brackets
    print(my_list[0])  # Output: 1
    print(my_list[2])  # Output: 3

    # Iterating over the CustomList
    for item in my_list:
        print(item)  # Output: 1, 2, 3, 4, 5

    ```
    