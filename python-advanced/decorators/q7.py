import datetime

def timestamp_decorator(func):
    def wrapper(*args, **kwargs):
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f'Timestamp: {timestamp}')
        return func(*args, **kwargs)
    return wrapper
    
@timestamp_decorator
def add(a, b):
    return a + b

@timestamp_decorator
def multiply(a, b):
    return a * b

@timestamp_decorator
def greet(name):
    print(f"Hello, {name}!")

# Test the decorated functions
print(add(3, 4))
print(multiply(5, 6))
greet("Utkarsh")