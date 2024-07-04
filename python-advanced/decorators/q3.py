def simple_decorator(x_function):
    def internal_function01(*args, **kwargs):
        print('{} was called with the following arguments'.format(x_function.__name__))
        print('\n{}'.format(args))
        print('\n{}'.format(kwargs))
        x_function(*args, **kwargs)
        print('Decorator is still operating')

    return internal_function01

@simple_decorator
def combiner(*args, **kwargs):
    print("\n Hello from the decorator function, these are the arguments I received", args, kwargs)

combiner('a', 'b', myvar='yes')