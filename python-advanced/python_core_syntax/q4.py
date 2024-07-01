class TIMEINTERVAL:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours 
        self.minutes = minutes
        self.seconds = seconds 
        
    def __add__(self, other):
        x = self.hours + other.hours 
        y = self.minutes + other.minutes
        z = self.seconds + other.seconds 
        
        # Handle overflow for seconds and minutes
        if z >= 60:
            y += z // 60
            z = z % 60
        if y >= 60:
            x += y // 60
            y = y % 60
        
        return TIMEINTERVAL(x, y, z)
        
        
    def __sub__(self, other):
        x = self.hours - other.hours 
        y = self.minutes - other.minutes
        z = self.seconds - other.seconds
        
         # Handle underflow for seconds and minutes
        if z < 0:
            y -= 1
            z += 60
        if y < 0:
            x -= 1
            y += 60
        
        return TIMEINTERVAL(x, y, z)
        
    def __str__(self):
        return f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}"

        
    
mytimeinstance = TIMEINTERVAL(5,30,55)
mytimeinstance2 = TIMEINTERVAL(1,20,30)
print(mytimeinstance)
print(mytimeinstance - mytimeinstance2)
print(str(mytimeinstance))
print(mytimeinstance + mytimeinstance2)