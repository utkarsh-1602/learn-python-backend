# Exceptions in Python

## Try and except 

        try:
            value = int(input('Enter a natural number: '))
            print('The reciprocal of', value, 'is', 1/value)        
        except:
            print('I do not know what to do.')


### Two exceptions after one try 

        try:
            value = int(input('Enter a natural number: '))
            print('The reciprocal of', value, 'is', 1/value)        
        except ValueError:
            print('I do not know what to do.')    
        except ZeroDivisionError:
            print('Division by zero is not allowed in our Universe.') 

[refer q1.py](./q1.py)


### the default except 

        try:
            value = int(input('Enter a natural number: '))
            print('The reciprocal of', value, 'is', 1/value)        
        except ValueError:
            print('I do not know what to do.')    
        except ZeroDivisionError:
            print('Division by zero is not allowed in our Universe.')    
        except:
            print('Something strange has happened here... Sorry!')


