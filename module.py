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
        self.purchasePrice = purchasePrice
        self.sellPrice = sellPrice
        self.gearbox = gearbox
        self.fuelType = fuelType
        self.colors = colors
        if not isinstance(brand, str) or not isinstance(model, str) or not isinstance(type, str) or not isinstance(
                gearbox, str) or not isinstance(fuelType, str) or not isinstance(colors, str):
            raise ValueError("The data must be a string")
        if not isinstance(purchasePrice, int) or not isinstance(sellPrice, int) or not isinstance(years, int):
            raise ValueError("The data must be a int")


class Client:
    def __init__(self, client_name: str, last_name: str, email: str, phone_number: str, clientID: int):
        self._client_name = client_name
        self._last_name = last_name
        self._email = email
        self._phone_number = phone_number
        self.clientID = clientID
        if not isinstance(clientID, int):
            raise ValueError("clientID must be integer")
        if not isinstance(client_name, str) or not isinstance(last_name, str) or not isinstance(email, str):
            raise ValueError("Name, last name and email must be strings")
        if not "@" in email:
            raise ValueError("Email must start with '@'")
        phone_str = str(phone_number)
        if not phone_str.isdigit():
            raise ValueError("Phone number must contain only digits")
        if len(phone_str) < 12:
            raise ValueError("Phone number is too short")
        if len(phone_str) > 12:
            raise ValueError("Phone number is too long")


    def show_client(self):
            return f"Name:{self._client_name}\nLastname:{self._last_name}\nPhone number:{self._phone_number}\nID:{self.clientID}\n"
class Operation:
    pass


try:
    cl1 = Client("max", "ART", "max06032007@gmail.com", 380993308065, 1)
    print(cl1.show_client())
except ValueError as e:
    print(f"Error: {e}")
