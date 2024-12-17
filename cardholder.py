class cardHolder():
    def __init__(self, cardNum, pin, firstname, lastname, balance):
        self.cardNum = cardNum
        self.pin = pin
        self.firstname = firstname
        self.lastname = lastname
        self.balance= balance

###getter method to get things everytime we need
def get_cardNum(self):
    return self.cardNum
def get_pin(self):
    return self.pin
def get_firstname(self):
    return self.firstname
def get_lastname(self):
    return self.lastname
def get_balance(self):
    return self.balance 

###setter method give values
 def set_cardNum(self, newVal):
    self.cardNum = newval
def set_pin(self, newVal):
    self.pin = newval
def set_firstname(self, newVal):
    self.firstname = newval
def set_lastname(self, newVal):
    self.lastname = newval
def set_balance(self, newVal):
    self.balance = newval

def pint_out(self):
    print("Card #: ",self.cardNum)
    print("pin: ",self.pin)
    print("firstname: ",self.firstname)
    print("lastname: ",self.lastname)
    print("balance: ",self.balance)