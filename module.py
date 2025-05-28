class Dealership:
    all_dealerships = []
    all_cars_dealerships = []

    def __init__(self, dealership_name: str, dealership_ID: int):
        self.dealership_name = dealership_name
        self.dealership_ID = dealership_ID
        self.cars = []
        if not isinstance(dealership_name, str):
            raise ValueError('dealership_name має бути рядком')
        if not isinstance(dealership_ID, int):
            raise ValueError('dealership_ID має бути цілим числом')
        if dealership_ID < 0:
            raise ValueError("ID повинно бути додатнім значенням")
        new_dealership = {
            "Name": dealership_name,
            "ID": dealership_ID
        }
        if any(d['ID'] == dealership_ID for d in Dealership.all_dealerships):
            raise ValueError('Автосалон з таким ID уже існує')
        Dealership.all_dealerships.append(new_dealership)

    @staticmethod
    def list_dealerships():
            if not Dealership.all_cars_dealerships:
                return "Немає автомобілів в жодному автосалоні"

            dealerships_dict = {}

            for car in Dealership.all_cars_dealerships:
                dealership_name = car['dealership_name']
                if dealership_name not in dealerships_dict:
                    dealerships_dict[dealership_name] = []
                dealerships_dict[dealership_name].append(car)

            result = "Список автосалонів та їх автомобілів:\n"
            for dealership_name, cars in dealerships_dict.items():
                result += f"\nАвтосалон {dealership_name}:\n"
                for car in cars:
                    result += (f"- {car['brand']} {car['model']}, "
                               f"ID: {car['car_ID']}, "
                               f"Рік: {car['years']}, "
                               f"Тип: {car['type']}, "
                               f"Ціна: {car['sellPrice']}\n")
            return result

    def add_car(self, car):
        if car in self.cars:
            return "Ця машина вже є в автосалоні"
        self.cars.append(car)
        car.dealership = self
        return f"Додано авто {car.brand} {car.model} {car.years}, ID: {car.carID}"

    def list_cars(self):
        if not hasattr(self, 'dealership_name') or self.dealership_name is None:
            return "Автосалон відсутній"
        if not self.cars:
            return f"В автосалоні {self.dealership_name} немає машин."

        result = f"Машини в автосалоні {self.dealership_name}:\n"
        for car in self.cars:
            result += (
                f"- {car.brand} {car.model} ({car.years}), "
                f"ID: {car.carID}, Тип: {car.type}, "
                f"Ціна: {car.sellPrice} ₴\n"
            )
        return result

    @classmethod
    def all_dealerships_info(cls):
        if not cls.all_dealerships:
            return "Список автосалонів порожній"
        result = "Список автосалонів:\n"
        for dealership in cls.all_dealerships:
            result += f"ID: {dealership['ID']}, Назва: {dealership['Name']}\n"
        return result

    def remove_dealership(self, dealership_ID):
        initial_length = len(Dealership.all_dealerships)
        Dealership.all_dealerships = [d for d in Dealership.all_dealerships if d['ID'] != dealership_ID]
        if len(Dealership.all_dealerships) == initial_length:
            return f"Автосалон з ID {dealership_ID} не знайдено"
        if not Dealership.all_dealerships:
            return "Список автосалонів порожній"
        result = "Оновлений список автосалонів:\n"
        for dealership in Dealership.all_dealerships:
            result += f"ID: {dealership['ID']}, Назва: {dealership['Name']}\n"
        return result




class Car:
    car_list = []
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
        if self.years and self.purchasePrice and self.sellPrice < 0:
            raise ValueError("Значення не може бути мінімальним, мінімальне значення - 0")
        if self.years > 2025:
            raise ValueError("Значення не може бути більшим, максимальне значення - 2025")


    def add_to_dealership(self, dealership):
        if self.dealership is not None:
            raise ValueError(f"Автосалон порожній: {dealership.dealership_name}!")

        if not isinstance(dealership, Dealership):
            raise ValueError("Потрібно передати об'єкт класу Dealership")
        dealership.cars.append(self)
        self.dealership = dealership
        return f"Машина {self.brand} {self.model} успішно додана до автосалону {dealership.dealership_name}"

    def get_dealership_info(self):
        if self.dealership is None:
            return "Ця машина не належить жодному автосалону."
        return f"Машина {self.brand} {self.model} знаходиться в {self.dealership.dealership_name} (ID: {self.dealership.dealership_ID})"


def list_cars(self):
    if not self.cars:
        return f"В автосалоні {self.dealership_name} немає автомобілів"

    result = f"Автомобілі в автосалоні {self.dealership_name}:\n"
    for car in self.cars:
        result += (f"ID: {car.carID}, "
                   f"Марка: {car.brand}, "
                   f"Модель: {car.model}, "
                   f"Рік випуску: {car.years}, ")
    return result


class Client:
    def __init__(self, client_name: str, last_name: str, email: str, phone_number: str, clientID: int):
        self._client_name = client_name
        self._last_name = last_name
        self._email = email
        self._phone_number = phone_number
        self.clientID = clientID
        if not isinstance(clientID, int):
            raise ValueError("ID повино бути в цифровому форматі")
        if not isinstance(client_name, str) or not isinstance(last_name, str) or not isinstance(email, str):
            raise ValueError("Ім'я та прізвище повино бути текстом.")
        if not "@" in email:
            raise ValueError("Додайте символ @ в email")
        if not phone_number.isdigit():
            raise ValueError("Phone number must contain only digits")
        if len(phone_number) < 12:
            raise ValueError("Невірний номер телефону. Введіть номер телефону в форматі +380123456789")
        if len(phone_number) > 12:
            raise ValueError("Невірний номер телефону. Введіть номер телефону в форматі +380123456789")
        if phone_number <= 0:
            raise ValueError("Числове значення повинно бути більше або дорівнює 0")


    def show_client(self):
            return f"Name:{self._client_name}\nLastname:{self._last_name}\nPhone number:{self._phone_number}\nID:{self.clientID}\n"
class Operation:
    pass

try:
    d1 = Dealership("D1", 1)
    d2 = Dealership("D2", 2)
    car1 = Car("BMW", "550i", 2019, "sedan", 10000, 15000, "Manual", "Diesel", "White",1)
    car2 = Car("BMW", "M5", 2022, "sedan", 10000, 15000, "Auto", "Diesel", "Blue",2)
    car3 = Car("BMW", "M6", 2023, "sedan", 10000, 15000, "Auto", "Diesel", "Black",3)
    print(d1.add_car(car1))
    print(d2.add_car(car2))

    print(car1.add_to_dealership(d1))
    print(car2.add_to_dealership(d2))
    print(car3.add_to_dealership(d1))
    print(Dealership.list_dealerships())
except ValueError as e:
    print("error:", e)