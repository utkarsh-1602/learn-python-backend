class Example:

    __internal_counter = 0

    def __init__(self, value):
        Example.__internal_counter += 1 
    
    # In Python, @classmethod is a decorator used to define a method within a class that operates on the class itself rather than on instances of the class. This means that class methods have access to the class itself. 

    @classmethod
    def my_fun(cls):
        return '# of objects created: {}'.format(cls.__internal_counter)


print(Example.my_fun()) # object created 0 

ins01 = Example(10)
print(Example.my_fun()) # object created 1

ins02 = Example(11)
print(Example.my_fun()) # object created 2