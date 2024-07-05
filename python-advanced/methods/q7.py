class InvalidEngravingError(Exception):
    """Custom exception for invalid engraving text."""
    pass

class Lux_Watches:
    watches_created = 0
    
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price
        self.engraving = None 
        Lux_Watches.watches_created += 1 
    
    @classmethod 
    def with_engraving(cls, brand, price, engraving=None):
        
        if engraving:
            if len(engraving) > 40:
                raise InvalidEngravingError("Engraving text cannot be longer than 40 characters.")
            if not engraving.isalnum():
                raise InvalidEngravingError("Engraving text must be alphanumerical and contain no spaces")
                
        
        watch_var = cls(brand, price)
        watch_var.engraving = engraving 
        return watch_var
        
    @classmethod    
    def get_number_of_watches_created(cls):
        return cls.watches_created
        
    
    
print(Lux_Watches.get_number_of_watches_created())
    
myinst01 = Lux_Watches('titan', 50000)
myinst02 = Lux_Watches('rolex', 90000)

print(Lux_Watches.get_number_of_watches_created())

# creating an instance with engraving 
engrave_watch = Lux_Watches.with_engraving('Omega', 75000, 'beAwesome100')
print(engrave_watch.brand, engrave_watch.price, engrave_watch.engraving)

print(Lux_Watches.get_number_of_watches_created())