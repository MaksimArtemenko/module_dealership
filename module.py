class Dealership:
    def __init__ (self, dealership_name, dealership_ID):
        self.dealership_name = dealership_name
        self.dealership_ID = dealership_ID
class Car:
    def __init__ (self, brand: str, model: str, years: int, type: str, purchasePrice: int, sellPrice: int, gearbox: str,
             fuelType: str, colors: str):
        self.brand = brand
        self.model = model
        self.years = years
        self.type = type
        self.purchasePrice = int
        self.sellPrice = int
        self.gearbox = gearbox
        self.fuelType = fuelType
        self.colors = colors
class Client:
    def __init__ (self, client_name: str, last_name: str, email: str, phoneNumber: int, clientID: int):
        self.client_name = client_name
        self.last_name = last_name
        self.email = email
        self.phoneNumber = phoneNumber
        self.clientID = clientID
class Operation:
    pass