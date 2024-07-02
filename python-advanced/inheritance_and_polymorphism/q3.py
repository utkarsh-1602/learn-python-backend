class Scanner:
    def scan(self):
        print("scan() method from scanner class")
    
    
class Printer:
    def print(self):
        print("print() method from Printer class")
        

class Fax:
    def send(self):
        print("send() method from Fax class")
        
    def print(self):
        print("print() method from Fax class")


class MFD_SPF(Scanner, Printer, Fax):
    pass


class MFD_SFP(Scanner, Fax, Printer):
    pass


mfd_spf = MFD_SPF()
mfd_sfp = MFD_SFP()

# Call the methods on MFD_SPF
print("calling methods on MFD_SPF: ")
mfd_spf.scan()
mfd_spf.print()
mfd_spf.send()

# Call the methods on MFD_SFP
print("\nCalling methods on MFD_SFP:")
mfd_sfp.scan()
mfd_sfp.print()
mfd_sfp.send()

