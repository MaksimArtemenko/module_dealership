"""
    Модуль для управління автосалоном, що забезпечує функціонал для роботи з автомобілями, клієнтами та різними типами операцій.
    """


class Dealership:
    """
    Клас для представлення автосалону.

    Attributes:
        all_dealerships (list): Список всіх зареєстрованих автосалонів
        all_cars_dealerships (list): Список всіх автомобілів у всіх автосалонах
    """
    all_dealerships = []
    all_cars_dealerships = []

    def __init__(self, dealership_name: str, dealership_ID: int):
        """
        Ініціалізує новий автосалон.

        Args:
            dealership_name (str): Назва автосалону
            dealership_ID (int): Унікальний ідентифікатор автосалону

        Raises:
            ValueError: Якщо dealership_name не є рядком
            ValueError: Якщо dealership_ID не є цілим числом
            ValueError: Якщо dealership_ID є від'ємним
            ValueError: Якщо автосалон з таким ID вже існує
        """
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
        """
        Відображає список всіх автомобілів у всіх автосалонах.

        Returns:
            str: Форматований список автосалонів та їх автомобілів, включаючи
                детальну інформацію про кожен автомобіль
        """

        if not Dealership.all_cars_dealerships:
                return f"Немає автомобілів в жодному автосалоні"

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
                           f"Ціна: {car['sellPrice']}$\n")
        return result

    def add_car(self, car):
        """
        Додає автомобіль до автосалону.

        Args:
            car (Car): Об'єкт автомобіля для додавання

        Returns:
            str: Повідомлення про успішне додавання або про те, що автомобіль
                вже є в автосалоні
        """
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
        """
        Показує список всіх автомобілів у поточному автосалоні.

        Returns:
            str: Форматований список автомобілів з їх характеристиками
                або повідомлення про відсутність автомобілів
        """
        if not hasattr(self, 'dealership_name') or self.dealership_name is None:
            return "Автосалон відсутній"
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

    @classmethod
    def all_dealerships_info(cls):
        """
        Відображає інформацію про всі зареєстровані автосалони

        Returns:
            str: Список всіх автосалонів з їх ID та назвами
                або повідомлення про відсутність автосалонів
        """
        if not cls.all_dealerships:
            return "Список автосалонів порожній"
        result = "Список автосалонів:\n"
        for dealership in cls.all_dealerships:
            result += f"ID: {dealership['ID']}, Назва: {dealership['Name']}\n"
        return result

    @staticmethod
    def remove_dealership(dealership_ID):
        """
        Видаляє автосалон за його ID.

        Args:
            dealership_ID (int): Ідентифікатор автосалону для видалення

        Returns:
            str: Оновлений список автосалонів або повідомлення про помилку
        """

        dealership_to_remove = next((d for d in Dealership.all_dealerships if d['ID'] == dealership_ID), None)
        if not dealership_to_remove:
            return f"Автосалон з ID {dealership_ID} не знайдено"
        Dealership.all_dealerships = [d for d in Dealership.all_dealerships if d['ID'] != dealership_ID]
        Dealership.all_cars_dealerships = [
            c for c in Dealership.all_cars_dealerships
            if c['dealership_name'] != dealership_to_remove['Name']]
        if not Dealership.all_dealerships:
            return "Список автосалонів порожній"
        return Dealership.all_dealerships_info()

    def remove_car(self, car):
        """
        Видаляє автомобіль з автосалону.

        Args:
            self: Поточний автосалон
            car (Car): Автомобіль для видалення

        Returns:
            str: Повідомлення про успішне видалення

        Raises:
            ValueError: Якщо автомобіль не належить цьому автосалону
        """

        if car not in self.cars:
            raise ValueError("Ця машина не належить цьому автосалону")

        self.cars.remove(car)
        car.dealership = None

        Dealership.all_cars_dealerships = [
            c for c in Dealership.all_cars_dealerships
            if c['car_ID'] != car.carID
        ]
        return f"Машина {car.brand} {car.model} видалена з автосалону"




class Car:
    """
    Клас для представлення автомобіля.

    Attributes:
        car_list (list): Список всіх автомобілів
        brand (str): Марка автомобіля
        model (str): Модель автомобіля
        years (int): Рік випуску
        type (str): Тип кузова
        purchasePrice (int): Ціна закупівлі
        sellPrice (int): Ціна продажу
        gearbox (str): Тип коробки передач
        fuelType (str): Тип палива
        colors (str): Колір автомобіля
        carID (int): Унікальний ідентифікатор
        dealership (Dealership): Автосалон, якому належить автомобіль
    """
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


    def get_dealership_info(self):
        """
        Отримує інформацію про автосалон, якому належить автомобіль.

        Returns:
            str: Інформація про автосалон або повідомлення про відсутність
                приналежності до автосалону
        """
        if self.dealership is None:
            return "Ця машина не належить жодному автосалону."
        return f"Машина {self.brand} {self.model} знаходиться в {self.dealership.dealership_name} (ID: {self.dealership.dealership_ID})"


class Client:
    """
    Клас для представлення клієнта автосалону.

    Attributes:
        _client_name (str): Ім'я клієнта
        _last_name (str): Прізвище клієнта
        _email (str): Email адреса
        _phone_number (str): Номер телефону
        clientID (int): Унікальний ідентифікатор клієнта
    """

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
        if len(email) == 0:
            raise ValueError("Введіть email")


    def show_client(self):
        """
        Відображає інформацію про клієнта.

        Returns:
            str: Форматована інформація про клієнта, включаючи ім'я,
                прізвище, номер телефону та ID
        """
        return f"Ім'я:{self._client_name}\nПрізвище:{self._last_name}\nНомер телефону:{self._phone_number}\nID:{self.clientID}\n"
class Operation:
    """
    Клас для управління операціями з автомобілями.

    Attributes:
        operation_history (list): Історія всіх виконаних операцій
    """
    operation_history = []

    @staticmethod
    def leasing_car(client: Client, car: Car, months: int, first_payment: int):
        """
        Оформлює операцію лізингу автомобіля.

        Args:
            client (Client): Клієнт, який оформлює лізинг
            car (Car): Автомобіль для лізингу
            months (int): Термін лізингу в місяцях
            first_payment (int): Сума першого внеску

        Returns:
            str: Інформація про оформлений лізинг

        Raises:
            ValueError: Якщо введені некоректні дані або автомобіль недоступний
        """
        if car.dealership is None:
            raise ValueError("Автомобіль не належить жодному автосалону")

        if not isinstance(months, int) or months <= 0:
            raise ValueError("Термін лізінгу має бути додатнім числом")

        if not isinstance(first_payment, int):
            raise ValueError("Перший внесок має бути числом")
        if first_payment < 0:
            raise ValueError("Значення повинно бути додатнім")
        if car.sellPrice < 0:
            raise ValueError("Значення повинно бути додатнім")


        monthly_payment = (car.sellPrice - first_payment) / months
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
        f"Перший внесок {first_payment} $\n"
        f"Щомісячний платіж: {monthly_payment:.2f} $ на {months} місяців")


    @staticmethod
    def trade_in(client:Client, old_car: Car, new_car: Car, additional_payment: int):
        """
        Оформлює операцію обміну старого автомобіля на новий (трейд-ін).

        Args:
            client (Client): Клієнт, який здійснює обмін
            old_car (Car): Старий автомобіль для обміну
            new_car (Car): Новий автомобіль
            additional_payment (int): Додаткова плата

        Returns:
            str: Інформація про операцію трейд-ін

        Raises:
            ValueError: Якщо автомобілі недоступні
        """
        if new_car.dealership is None:
            raise ValueError("Новий автомобіль не належить жодному автосалону")
        if old_car.dealership is None:
            raise ValueError("Старий автомобіль не належить жодному автосалону")

        trade_in_value = old_car.purchasePrice * 0.8
        total_payment = new_car.sellPrice - trade_in_value + additional_payment

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
                f"Додаткова плата {additional_payment}$\n"
                f"Загальна сума: {total_payment:.2f}$")

    @staticmethod
    def sell_car(client: Client, car: Car):
        """
        Оформлює продаж автомобіля клієнту.

        Args:
            client (Client): Клієнт-покупець
            car (Car): Автомобіль для продажу

        Returns:
            str: Інформація про продаж

        Raises:
            ValueError: Якщо автомобіль не доступний для продажу
        """
        if car.dealership is None:
            raise ValueError("Автомобіль не належить жодному автосалону")

        operation_info = {
            "type": "Продаж",
            "client": f"{client._client_name} {client._last_name}",
            "car": f"{car.brand} {car.model}",
            "price": car.sellPrice,
            "dealership": car.dealership.dealership_name
        }
        Operation.operation_history.append(operation_info)

        car.dealership.cars.remove(car)
        Dealership.all_cars_dealerships = [c for c in Dealership.all_cars_dealerships if c['car_ID'] != car.carID]
        car.dealership = None

        return (f"Продаж оформлено: {client._client_name} {client._last_name} купив {car.brand} {car.model}\n"
                f"Ціна: {car.sellPrice} $")

    @staticmethod
    def buy_car(dealership: Dealership, car: Car):
        """
        Оформлює закупівлю автомобіля автосалоном.

        Args:
            dealership (Dealership): Автосалон, який купує
            car (Car): Автомобіль для закупівлі

        Returns:
            str: Інформація про закупівлю

        Raises:
            ValueError: Якщо автомобіль вже належить іншому автосалону
        """
        if car.dealership is not None:
            raise ValueError("Цей автомобіль вже належить іншому автосалону")

        operation_info = {
            "type": "Закупівля",
            "dealership": dealership.dealership_name,
            "car": f"{car.brand} {car.model}",
            "purchase_price": car.purchasePrice
        }
        Operation.operation_history.append(operation_info)


        dealership.add_car(car)

        return (f"Закупівля оформлена: автосалон {dealership.dealership_name} придбав {car.brand} {car.model}\n"
                f"Ціна закупівлі: {car.purchasePrice} $")

    @classmethod
    def show_operation_history(cls):
        """
        Відображає повну історію всіх операцій.

        Returns:
            str: Форматований список всіх операцій з деталями кожної операції
                або повідомлення про відсутність операцій
        """
        if not cls.operation_history:
            return "Історія операцій порожня"

        result = "Історія операцій:"
        for i, operation in enumerate(cls.operation_history, 1):
            result += f"Операція #{i}:\n"
            result += f"Тип: {operation['type']}\n"

            if operation['type'] == "Лізінг":
                result += (f"Клієнт: {operation['client']}\n"
                           f"Автомобіль: {operation['car']}\n"
                           f"Перший внесок: {operation['down_payment']} ₴\n"
                           f"Щомісячний платіж: {operation['monthly_payment']:.2f}\n"
                           f"Загальна вартість: {operation['total_price']} \n")

            elif operation['type'] == "Трейд-ін":
                result += (f"Клієнт: {operation['client']}\n"
                           f"Зданий автомобіль: {operation['old_car']}\n"
                           f"Отриманий автомобіль: {operation['new_car']}\n"
                           f"Вартість трейд-іну: {operation['trade_in_value']}\n"
                           f"Додаткова плата: {operation['additional_payment']}\n"
                           f"Загальна сума: {operation['total_payment']}\n")

            elif operation['type'] == "Продаж":
                result += (f"Клієнт: {operation['client']}\n"
                           f"Автомобіль: {operation['car']}\n"
                           f"Ціна продажу: {operation['price']}$\n"
                           f"Автосалон: {operation['dealership']}\n")

            elif operation['type'] == "Закупівля":
                result += (f"Автосалон: {operation['dealership']}\n"
                           f"Автомобіль: {operation['car']}\n"
                           f"Ціна закупівлі: {operation['purchase_price']}$\n")


        return result


if __name__ == "__main__":

    try:
        car1 = Car("BMW", "5 Series", 2020, "Sedan", 10000, 12000, "Manual", "Gasoline", "Black", 1)
        car2 = Car("Volvo","V40", 2018, "Sedan", 15000, 18000, "Manual", "Gasoline", "Black", 2)
        car3 = Car("Kia","Rio", 2019, "Sedan", 12000, 15000, "Manual", "Gasoline", "Black", 3)
        car4 = Car("Skoda","Kamiq", 2017, "Sedan", 13000, 17000, "Manual", "Gasoline", "Black", 4)

        d1 = Dealership("BMW Kyiv", 1)
        d2 = Dealership("Volvo Kharkiv", 2)
        d3 = Dealership("Kia Sumy", 3)
        d4 = Dealership("Skoda Kyiv", 4)


        client1 = Client("Maksim", "Artemenko", "max06032007@gmail.com", "380123456789", 1)

        d1.add_car(car1)
        d2.add_car(car2)
        d3.add_car(car3)

        Operation.buy_car(d4, car4)
        Operation.sell_car(client1, car1)
        Operation.trade_in(client1, car2, car3, 1000)
        Operation.leasing_car(client1, car4, 12, 10000)

        print(Operation.show_operation_history())







    except Exception as e:
        print("Error:",e)