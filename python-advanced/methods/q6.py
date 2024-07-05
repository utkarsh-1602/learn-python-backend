class Bank:
    def __init__(self, iban):
        print("__init__ called")
        self.iban = iban

    @staticmethod
    def validate(iban):
        if(len(iban) == 20):
            return True
        else:
            return False 
    
Acc_Numbers = ['8'*20, '7'*4, '2222']

for element in Acc_Numbers:
    if Bank.validate(element):
        print('We can use', element, ' to create a bank account')

    else:
        print('The account number', element, 'is invalid')