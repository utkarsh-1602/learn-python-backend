
def myfunc(a, b, *args, **kwargs):
    print(a, type(a))
    print(b, type(b))
    print(args, type(args))
    print(kwargs, type(kwargs))


myfunc(10, 'abc', 1,2,3, arg1=100, arg2='hello world')