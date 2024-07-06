#composite class 
class Car:
    def __init__(self, engine):
        self.engine = engine # this is the instance of gasEngine and DieselEngine 


#component classes
class GasEngine:
    def __init__(self, horse_power):
        self.horse_power = horse_power

    def start(self):
        print(f"Starting the {self.horse_power} HP Gas Engine")


class DieselEngine:
    def __init__(self, horse_power):
        self.horse_power = horse_power

    def start(self):
        print(f"Starting the {self.horse_power} HP Gas Engine")


# use the composite class 
gasEngine = GasEngine(20)
dieselEngine = DieselEngine(50)

car1 = Car(gasEngine)
car2 = Car(dieselEngine)

car1.engine.start()
car2.engine.start()