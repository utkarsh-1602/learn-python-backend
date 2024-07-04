def simple_decorator(function):
    print('we are about to call {}'.format(function.__name__))
    return function
    
@simple_decorator
def simple_hello():
    print("Hello world")

simple_hello()