class Dealership:
    def __init__(self, dealership_name: str, dealership_ID: int):
        self.dealerships = []
        self.dealership_name = dealership_name
        self.dealership_ID = dealership_ID
        self.cars = []
        if not isinstance(dealership_name, str):
            raise ValueError('dealership_name має бути рядком')
        if not isinstance(dealership_ID, int):
            raise ValueError('dealership_ID має бути цілим числом')
        if not isinstance(self.dealerships, list):
            raise ValueError('dealerships має бути списком')

    def add_car(self, car):
        if car in self.cars:
            return "Ця машина вже є в автосалоні"

        self.cars.append(car)
        car.dealership = self
        return f"Додано авто {car.brand} {car.model} {car.years}, ID: {car.carID}"

    def list_cars(self):
        if not self.cars:
            return f"В автосалоні {self.dealership_name} немає машин."

        result = f"Машини в автосалоні {self.dealership_name}:\n"
        for car in self.cars:
            result += (
                f"- {car.brand} {car.model} ({car.years}), "
                f"ID: {car.carID}, Тип: {car.type}, "
                f"Ціна: {car.sellPrice} $\n"
            )
        return result


    def add_dealership(self, dealership):
        new_dealership = {
            "Name" : dealership.dealership_name,
            "ID" : dealership.dealership_ID
        }
        if any(d['ID'] == dealership.dealership_ID for d in self.dealerships):
            raise ValueError('Автосалон з таким ID уже існує')
        self.dealerships.append(new_dealership)
        return new_dealership

    def remove_dealership(self, dealership_ID):
        self.dealerships = [d for d in self.dealerships if d['ID'] != dealership_ID]
        if not self.dealerships:
            return "Список автосалонів порожній"
        result = "Оновлений список автосалонів:\n"
        for dealership in self.dealerships:
            result += f"ID: {dealership['ID']}, Назва: {dealership['Name']}\n"
        return result

    def list_dealerships(self):
        if not self.dealerships:
            return "Список автосалонів порожній"
        result = "Список автосалонів:\n"
        for dealership in self.dealerships:
            result += f"ID: {dealership['ID']}, Назва: {dealership['Name']}\n"
        return result


class Car:
    car_list = []
    def add_to_dealership(self, dealership):
        if self.dealership is not None:
            raise ValueError(f"Ця машина вже належить автосалону {self.dealership.dealership_name}!")

        if not isinstance(dealership, Dealership):
            raise ValueError("Потрібно передати об'єкт класу Dealership")
        dealership.cars.append(self)
        self.dealership = dealership
        return f"Машина {self.brand} {self.model} успішно додана до автосалону {dealership.dealership_name}"

    def __init__(self, brand: str, model: str, years: int, type: str, purchasePrice: int, sellPrice: int, gearbox: str,
                 fuelType: str, colors: str,carID: int):

        self.brand = brand
        self.model = model
        self.years = years
        self.type = type
        self.purchasePrice = purchasePrice
        self.sellPrice = sellPrice
        self.gearbox = gearbox
        self.fuelType = fuelType
        self.colors = colors
        self.carID = carID
        self.dealership = None

        if not isinstance(brand, str) or not isinstance(model, str) or not isinstance(type, str) or not isinstance(
                gearbox, str) or not isinstance(fuelType, str) or not isinstance(colors, str):
            raise ValueError("Повинно бути рядком значення")
        if not isinstance(purchasePrice, int) or not isinstance(sellPrice, int) or not isinstance(years, int) or not isinstance(carID, int):
            raise ValueError("Повинно бути числове значення")

        if dealership is not None:
            self.add_to_dealership(dealership)

        if dealership is not None:
            self.add_to_dealership(dealership)

    def add_to_dealership(self, dealership):
        if self.dealership is not None:
            raise ValueError(f"Ця машина вже належить автосалону {self.dealership.dealership_name}!")

        if not isinstance(dealership, Dealership):
            raise ValueError("Потрібно передати об'єкт класу Dealership")

        dealership.cars.append(self)
        self.dealership = dealership
        return f"Машина {self.brand} {self.model} додана до {dealership.dealership_name}"

    def get_dealership_info(self):
        if self.dealership is None:
            return "Ця машина не належить жодному автосалону."
        return f"Машина {self.brand} {self.model} знаходиться в {self.dealership.dealership_name} (ID: {self.dealership.dealership_ID})"



    def list_car(self):
        if not Car.car_list:
            return "Список авто порожній"
        result = "Список автосалонів:\n"
        for car in Car.car_list:
            result += f"ID: {car['ID']}, Марка: {car['brand']}, Модель: {car['model']}, Рік випуску: {car['years']}, Тип кузову: {car['Type']}, Ціна закупівлі: {car['purchasePrice']}, Ціна продажу: {car['sellPrice']}, Тип КПП: {car['gearbox']}, Тип палива: {car['FuelType']} \n"
        return result

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
        if not phone_number.isdigit():
            raise ValueError("Phone number must contain only digits")
        if len(phone_number) < 12:
            raise ValueError("Phone number is too short")
        if len(phone_number) > 12:
            raise ValueError("Phone number is too long")


    def show_client(self):
            return f"Name:{self._client_name}\nLastname:{self._last_name}\nPhone number:{self._phone_number}\nID:{self.clientID}\n"
class Operation:
    pass

try:
    car1 = Car("BMW", "550i", 2019, "sedan", 10000, 15000, "Manual", "Diesel", "White",1)
    car2 = Car("BMW", "M5", 2022, "sedan", 10000, 15000, "Auto", "Diesel", "Blue",2)
    print(car1.add_car(car1))
    print(car2.add_car(car2))
    print(car1.list_car())


except ValueError as e:
    print("error:", e)