def my_decorator(function):
    print(f"we will call function {function.__name__}")
    return function

@my_decorator
def my_fun():
    print("Hello from a simple function")

my_fun()