# composition in python

- Composition in Python is a design principle where a class is composed of one or more objects of other classes, meaning that it uses instances of other classes as attributes to achieve its functionality. This allows for more modular, maintainable, and reusable code by building complex types from simpler ones.

Here is a step-by-step guide and example to illustrate the concept of composition:

Step-by-Step Guide:
1. **Define the Component Classes**: These are the simpler classes that will be used as building blocks.
2. **Define the Composite Class**: This is the class that will use instances of the component classes as attributes.
3. **Use the Composite Class**: Instantiate the composite class and use its methods to interact with the component objects

Example 1 : Let's create an example where we have a `Book` class and an `Author` class. We will then create a `Library` class that uses instances of the `Book` class. [Refer q1.py](./q1.py)

- `__str__` : The `__str__` method in Python is a special method used to define the string representation of an object. This method is called by the built-in `str()` function and by the print function to convert an object to a string. The string returned by the `__str__` method is meant to be readable and informative, often used for display purposes.

```python 
    class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person(name={self.name}, age={self.age})"

    # Create an instance of Person
    person = Person("Alice", 30)

    # Using the __str__ method
    print(person)  # Output: Person(name=Alice, age=30)

    # Directly calling str() on the object
    print(str(person))  # Output: Person(name=Alice, age=30)

```

-  A good rule of thumb is to prefer composition over inheritance (often summarized as "composition over inheritance") when possible, as it tends to lead to more flexible and maintainable code.
- To favor composition over inheritance is a design principle that gives the design higher flexibility, as you can choose which domain-specific objects should be incorporated into your ultimate object. It's like arming your base machine with tooling, dedicated to running a specific task, but not building a wide hierarchy structure of classes covering all possible hardware combinations.

    