import datetime

class TimestampDecorator:

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(timestamp)
        return self.func(*args, **kwargs)
    

@TimestampDecorator
def add(a,b):
    return a+b


@TimestampDecorator
def multiply(a,b):
    return a*b


print(add(1,2))
print(multiply(4,5))