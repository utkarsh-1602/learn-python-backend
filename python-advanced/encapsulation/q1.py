class ATM:
    def __init__(self, transaction_id, account_number, pin):
        self.transaction_id = transaction_id # public attribute 
        self._account_number = account_number # protected attribute
        self.__pin = pin # private attribute

    # getter method for private attribute __pin
    @property
    def pin(self):
        return self.__pin
    
    # setter method for private attribute __pin
    @pin.setter
    def pin(self, new_pin):
        self.__pin = new_pin

    def display_info(self):
        print(f"account_number: {self._account_number}")
        print(f"PIN: {self.__pin}")


myinst01 = ATM("TXN123", "1234567890", "1234")

# Display initial info
print("Initial Information:")
myinst01.display_info()


# Change PIN using setter method
new_pin = "5678"
myinst01.pin = new_pin

# Display updated info
print("\nUpdated Information:")
myinst01.display_info()