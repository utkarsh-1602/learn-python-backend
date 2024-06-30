import random

class Shop:
    totalApples = 0
    totalWeight = 0
    
    def __init__(self): 
        self.Weight = random.uniform(0.2, 0.5)
        Shop.totalApples += 1
        Shop.totalWeight += self.Weight
        
    
max_apples = 1000
max_weight = 300.0

#List to store apple objects 
apples = []

# Create apple objects until the limitations are met
while Shop.totalApples < max_apples and Shop.totalWeight < max_weight: 
    newobj = Shop()
    apples.append(newobj)
    
# Result : 
print(f"Number of apples processed: {Shop.totalApples}")
print(f"Number of Weight processed: {Shop.totalWeight:.2f}")    

    