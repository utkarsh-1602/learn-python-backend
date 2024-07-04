# Decorators Stacking 

def decorator_one(func):
    def wrapper(*args, **kwargs):
        print("Decorator one - before")
        result = func(*args, **kwargs)
        print("Decorator one - after")
        return result
    return wrapper

def decorator_two(func):
    def wrapper(*args, **kwargs):
        print("Decorator two - before")
        result = func(*args, **kwargs)
        print("Decorator two - after")
        return result
    return wrapper

@decorator_one
@decorator_two
def say_hello(name):
    print(f"Hello, {name}!")

say_hello("Utkarsh")


# so the output of it will be 
'''
Decorator One - Before
Decorator Two - Before
Hello, Utkarsh!
Decorator Two - After
Decorator One - After

'''

# here first of all you should know that @decorator_two is wrapping the say_hello function, and then decorator_one is wrapping he decorator_two function, so kind of like nested functions, firstly decorator_one print function function ("decorator one - before") will execute then it will call internally @decorator_two, then @decorator_two will execute it's print function ("decorator two - before"). then it will call the say_hello function which will execute the "Hello Utkarsh" print function, then it will call the @Decorator two print("Decorator two - after") function and then it will finally call the @Decorator one print function print("Decorator one - after") 
