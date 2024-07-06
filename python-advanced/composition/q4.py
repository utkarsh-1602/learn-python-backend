# Component Classes
class Tires:
    def __init__(self, size, pressure):
        self.size = size 
        self.pressure = pressure
        
    def get_pressure(self):
        print(f"{self.size} Inches of Tires can contain {self.pressure} PSI Pressure ")
        
    def pump(self):
        increase = 2  # Increase pressure by 2 PSI each time
        self.pressure += increase
        print(f"Pumping... The pressure is now {self.pressure} PSI")
        
    
class Engine:
    def __init__(self, fuel_type):
        self.fuel_type = fuel_type
        self.state = 0
        
    def start(self):
        self.state = 1 
        print(f"{self.fuel_type} Engine Started")
        
    def stop(self):
        self.state = 0
        print(f"{self.fuel_type} Engine Stopped")
        
    def get_state(self):
        if self.state == 1:
            print("State: The Engine is Running\n")
        if self.state == 0:
            print("State: The Engine is Stopped\n")
            

# composite Class
class Vehicle:
    def __init__(self, VIN, engine, tires):
        self.VIN = VIN
        self.engine = engine # instance of Engine Class
        self.tires = tires  # instance of Tires Class
        

# Using the composite class 
city_tires = Tires(size=15, pressure=30)
off_road_tires = Tires(size=18, pressure=35)

electric_engine = Engine(fuel_type="Electric")
petrol_engine = Engine(fuel_type="Petrol")

city_car = Vehicle(VIN="ABC123", engine=electric_engine, tires=city_tires)
off_road_car = Vehicle(VIN="XYZ456", engine=petrol_engine, tires=off_road_tires)

# Interaction with the cars 
city_car.engine.start()
city_car.tires.get_pressure()
city_car.tires.pump()
city_car.engine.stop()
city_car.engine.get_state()

off_road_car.engine.start()
off_road_car.tires.get_pressure()
off_road_car.tires.pump()
off_road_car.engine.stop()
off_road_car.engine.get_state()

    