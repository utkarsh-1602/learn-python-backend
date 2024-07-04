def simple_hello():
    print("Hello world!")

def my_decorating_fun(function):
    print('We are about to call {}'.format(function.__name__))
    # {} serves as a placeholder for function.__name__. This method replaces {} with the value of function.__name__ within the string

    return function

my_decorator = my_decorating_fun(simple_hello)
my_decorator()
