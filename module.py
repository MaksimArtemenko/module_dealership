class Dealership:
    def __init__(self, dealership_name: str, dealership_ID: int):
        if not isinstance(dealership_name, str):
            raise ValueError('dealership_name має бути рядком')
        self.dealership_name = dealership_name

        if not isinstance(dealership_ID, int):
            raise ValueError('dealership_ID має бути цілим числом')
        self.dealership_ID = dealership_ID
        if not isinstance(self.dealerships, list):
            raise ValueError('dealerships має бути списком')
        self.dealerships = []
class Car:
    def __init__(self, brand: str, model: str, years: int, type: str, purchasePrice: int, sellPrice: int, gearbox: str,
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
        self.__client_name = client_name
        self.__last_name = last_name
        self.__email = email
        self.__phoneNumber = phoneNumber
        self.clientID = clientID
class Operation:
    pass