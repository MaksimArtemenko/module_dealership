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
    def list_dealerships_car():
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

        car_info = {
            "dealership_name":self.dealership_name,
            "brand":car.brand,
            "model":car.model,
            "years":car.years,
            "type":car.type,
            "sellPrice":car.sellPrice,
            "car_ID":car.carID
        }
        Dealership.all_cars_dealerships.append(car_info)
        return f"Додано авто {car.brand} {car.model} {car.years}, ID {car.carID}"


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
        return dealership.add_car(self)

    def get_dealership_info(self):
        if self.dealership is None:
            return "Ця машина не належить жодному автосалону."
        return f"Машина {self.brand} {self.model} знаходиться в {self.dealership.dealership_name} (ID: {self.dealership.dealership_ID})"

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
        if len(phone_number) <= 0:
            raise ValueError("Числове значення повинно бути більше або дорівнює 0")
        if len(email) == 0:
            raise ValueError("Введіть email")


    def show_client(self):
            return f"Name:{self._client_name}\nLastname:{self._last_name}\nPhone number:{self._phone_number}\nID:{self.clientID}\n"
class Operation:
    operation_history = []
    @staticmethod
    def leasing_car(client: Client, car: Car, months: int, first_payment: int):
        if car.dealership is None:
            raise ValueError("Автомобіль не належить жодному автосалону")

        if not isinstance(months, int) or months <= 0:
            raise ValueError("Значення повинно бути додатнім")

        if not isinstance(first_payment, int):
            raise ValueError("Перший внесок має бути числом")
        if first_payment < 0:
            raise ValueError("Значення повинно бути додатнім")
        if car.sellPrice < 0:
            raise ValueError("Значення повинно бути додатнім")


        monthly_payment = (car.sellPrice - first_payment) / months

        if monthly_payment < 0:
            raise ValueError("Значення повинно бути більше 0")
        operation_info = {
            "type": "Лізінг",
            "client": f"{client._client_name} {client._last_name}",
            "car": f"{car.brand} {car.model}",
            "monthly_payment": monthly_payment,
            "down_payment": first_payment,
            "total_price": car.sellPrice
        }
        Operation.operation_history.append(operation_info)

        return (f"Лізінг оформленно: {client._client_name} {client._last_name}, отримує {car.brand} {car.model}\n"
        f"Перший внесок {first_payment}\n"
        f"Щомісячний платіж: {monthly_payment:.2f} на {months} місяців")


    @staticmethod
    def trade_in(client:Client, old_car: Car, new_car: Car, additional_payment: int = 0):
        if new_car.dealership is None:
            raise ValueError("Новий автомобіль не належить жодному автосалону")
        if old_car.dealership is None:
            raise ValueError("Старий автомобіль не належить жодному автосалону")

        trade_in_value = old_car.purchasePrice * 0.8
        total_payment = new_car.sellPrice - trade_in_value + additional_payment
        if total_payment < 0 or additional_payment < 0:
            raise ValueError("Значення повинно бути більше 0")

        if old_car.dealership:
            old_car.dealership.cars.remove(old_car)
            old_car.dealership = None

        operation_info = {
            "type":"Трейд-ін",
            "client":f"{client._client_name} {client._last_name}",
            "old_car":f"{old_car.brand} {old_car.model}",
            "new_car":f"{new_car.brand} {new_car.model}",
            "trade_in_value":trade_in_value,
            "total_payment":total_payment,
            "additional_payment":additional_payment
        }
        Operation.operation_history.append(operation_info)
        return (f"Трейд-ін оформлено: {client._client_name} {client._last_name}\n"
                f"Здає:{old_car.brand} {old_car.model} за {trade_in_value}\n"
                f"Отримує:{new_car.brand} {new_car.model}\n"
                f"Додаткова плата {additional_payment}\n"
                f"Загальна сума: {total_payment:.2f}")


try:

    car1 = Car("Volvo", "V40", 2018, "Sedan", 100000, 150000, "Manual", "Gasoline", "White", 1)


except ValueError as e:
    print("Error:", e)