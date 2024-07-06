import abc

class BluePrint(abc.ABC):

    @abc.abstractmethod
    def hello(self):
        pass

class GreenField(BluePrint):
    def hello(self):
        print("Welcome to GreenField")


class RedField(BluePrint):
    def yellow(self):
        pass 


myinstance01 = GreenField()
myinstance01.hello()

myinstance02 = RedField()

# the RedField class is still recognized as an abstract one, because it inherits all elements of its super class, which is abstract, and the RedField class does not override the abstract hello method