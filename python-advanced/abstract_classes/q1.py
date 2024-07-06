import abc

class BluePrint(abc.ABC):

    @abc.abstractmethod
    def hello(self):
        pass

class GreenField(BluePrint):
    def hello(self):
        print("Welcome to GreenField")


myinstance01 = GreenField()
myinstance01.hello()

# myinstance02 = BluePrint()
# myinstance02.hello()
# This will throw an error 