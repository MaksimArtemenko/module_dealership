# module_dealership
`module_dealership` - це модуль для управління автосалоном. Забезпечує функціонал для роботи з автомобілями та різними типами операцій (лізинг, трейд-ін).

 ----

## Опис
### Клас Автосалон(Dealership)
 - [X]  Створення нового автосалону з унікальним ID

- [X]  Додавання автомобілів до автосалону

- [X] Перегляд списку авто, які належать автосалону

- [X] Видалення автосалону з глобального списку

- [X] Видалення конкретного авто із салону

- [X] Перегляд усіх автосалонів та їх авто (загальний звіт)

### Клас Авто(Car)
 - [X]  Створення автомобіля з детальною інформацією:

  - марка, модель, рік, тип кузова, коробка, паливо, колір, ID

- [X] Авто одразу прив’язується до конкретного салону

- [X] Можливість отримати унікальний carID та ціну

### Клас Клієнт(Client)
- [X]  Створення клієнта з:

  - ім’ям, прізвищем, email, телефоном, ID

- [x] Закритий доступ до особистих даних (через геттери)

### Клас Операції(Operation)
- [x]  Лізинг автомобіля:

  - розрахунок щомісячного платежу

  - формування повної інформації про лізинг

- [x]  Трейд-ін (обмін авто):

   - порівняння цін старого і нового авто

    - підрахунок доплати або повернення коштів

- [X]  Історія всіх операцій, що були проведені

## Встановлення
1. Скопіюйте файл до свого проєкту.

2. Імпортуйте необхідні класи:
```py
from dealership_module import Dealership, Car, Client, Operation
```
## Інструкція до методів класу `Dealership`
1. ## Ініціалізує автосалон.
**Призначення**:
 Ініціалізує новий автосалон.

**Як використовувати**:
Створити автосалон за всіма потрібними атрибутами.

**Приклад**:
```py
d1 = Dealership("BMW Kyiv", 1)
d2 = Dealership("Volvo Kharkiv", 2)
```

2. ## `list_dealerships_car`

**Призначення**:
Відображає список всіх автомобілів у всіх автосалонах.

**Як використовувати**:
```py
d1 = Dealership("BMW Kyiv", 1)
print(Dealership.list_dealerships_car())
```
**Вивід**:
```py
Список автосалонів та їх автомобілів:

Автосалон BMW Kyiv:
- BMW 5 Series, ID: 1, Рік: 2020, Тип: Sedan, Ціна: 12000$

Автосалон Volvo Kharkiv:
- Volvo V40, ID: 2, Рік: 2018, Тип: Sedan, Ціна: 18000$

Автосалон Kia Sumy:
- Kia Rio, ID: 3, Рік: 2019, Тип: Sedan, Ціна: 15000$

```
3. ## `add_car`
**Призначення**:
Додає автомобіль до автосалону

**Як використовувати**:
```py
car1 = Car("BMW", "5 Series", 2020, "Sedan", 10000, 12000, "Manual", "Gasoline", "Black", 1)
d1 = Dealership("BMW Kyiv", 1)
print(d1.add_car(car1))
```
**Вивід**:
```py
Додано авто BMW 5 Series 2020, ID 1
```
4. ## `list_cars`
**Призначення**:
Показує список всіх автомобілів у поточному автосалоні

**Як використовувати**:
```py
car1 = Car("BMW", "5 Series", 2020, "Sedan", 10000, 12000, "Manual", "Gasoline", "Black", 1)
d1 = Dealership("BMW Kyiv", 1)
print(d1.add_car(car1))
print(d1.list_cars())
```
**Вивід**:
```py
Машини в автосалоні BMW Kyiv:
- BMW 5 Series (2020), ID: 1, Тип: Sedan, Ціна: 12000 $
```
5. ## `all_dealerships_info`
**Призначення**:
Відображає інформацію про всі зареєстровані автосалони

**Як використовувати**:
```py
d1 = Dealership("BMW Kyiv", 1)
d2 = Dealership("Volvo Kharkiv", 2)

print(Dealership.all_dealerships_info())
```
**Вивід**:
```py
Список автосалонів:
ID: 1, Назва: BMW Kyiv
ID: 2, Назва: Volvo Kharkiv
ID: 3, Назва: Kia Sumy
ID: 4, Назва: Skoda Kyiv
```
6. ## `remove_dealership`
**Призначення**:
Видаляє автосалон за його ID.

**Як використовувати**:
```py
 d1 = Dealership("BMW Kyiv", 1)
 print(Dealership.remove_dealership(1))
 ```
 **Вивід**:
 ```py
 Список автосалонів:
ID: 2, Назва: Volvo Kharkiv
ID: 3, Назва: Kia Sumy
ID: 4, Назва: Skoda Kyiv
```
7. ## `remove_car`
  **Призначення**:
  Видаляє автомобіль з автосалону.
**Як використовувати**:
```py
car1 = Car("BMW", "5 Series", 2020, "Sedan", 10000, 12000, "Manual", "Gasoline", "Black", 1)
d1 = Dealership("BMW Kyiv", 1)
d1.add_car(car1)

print(d1.remove_car(car1))
```
**Вивід**:
```py
Машина BMW 5 Series видалена з автосалону
```

## Інструкція до методів класу `Car`

1. ## `get_dealership_info`
  **Призначення**:
Отримує інформацію про автосалон, якому належить автомобіль

**Як використовувати**:
```py
car1 = Car("BMW", "5 Series", 2020, "Sedan", 10000, 12000, "Manual", "Gasoline", "Black", 1)
d1 = Dealership("BMW Kyiv", 1)
d1.add_car(car1)

print(car1.get_dealership_info())
```
**Вивід**:
```py
Машина BMW 5 Series знаходиться в BMW Kyiv (ID: 1)
```
## Інструкція до методів класу `Client`

1. ## `show_client`
**Призначення**:
Відображає інформацію про клієнта

**Як використовувати**:
```py
 client1 = Client("Maksim", "Artemenko", "max06032007@gmail.com", "380123456789", 1)
 print(client1.show_client())
 ```
 **Вивід**:
 ```py
 Ім'я: Maksim
Прізвище: Artemenko
Номер телефону: 380123456789
ID: 1
```

## Інструкція до методів класу `Operation`
1. ## `leasing_car`
  **Призначення**:
  Оформлює операцію лізингу автомобіля

**Як використовувати**:
```py
client1 = Client("Maksim", "Artemenko", "max06032007@gmail.com", "380123456789", 1)
car1 = Car("BMW", "5 Series", 2020, "Sedan", 10000, 12000, "Manual", "Gasoline", "Black", 1)

print(Operation.leasing_car(client1, car1, 12, 2000))
```
**Вивід**:
```py
Лізінг оформленно: Maksim Artemenko, отримує BMW 5 Series
Перший внесок 2000 $
Щомісячний платіж: 833.33 $ на 12 місяців
```
2. ## `trade_in`
**Призначення**:
Оформлює операцію обміну старого автомобіля на новий (трейд-ін).

**Як використовувати**:
```py
client1 = Client("Maksim", "Artemenko", "max06032007@gmail.com", "380123456789", 1)
car1 = Car("BMW", "5 Series", 2020, "Sedan", 10000, 12000, "Manual", "Gasoline", "Black", 1)
car2 = Car("Volvo","V40", 2018, "Sedan", 15000, 18000, "Manual", "Gasoline", "Black", 2)

print(Operation.trade_in(client1, car1, car2, 1000))
```
**Вивід**:
```py
Трейд-ін оформлено: Maksim Artemenko
Здає:BMW 5 Series за 8000.0
Отримує:Volvo V40
Додаткова плата 1000$
Загальна сума: 11000.00$
```
3. ## `sell_car`
**Призначення**:
Оформлює продаж автомобіля клієнту.

**Як викоистовувати**:
```py
client1 = Client("Maksim", "Artemenko", "max06032007@gmail.com", "380123456789", 1)
car1 = Car("BMW", "5 Series", 2020, "Sedan", 10000, 12000, "Manual", "Gasoline", "Black", 1)

print(Operation.sell_car(client1, car1))
```
**Вивід**:
```py
Продаж оформлено: Maksim Artemenko купив BMW 5 Series
Ціна: 12000 $
```
4. ## `buy_car`
**Призначення**:
Оформлює закупівлю автомобіля автосалоном

**Як використовувати**:
```py
car4 = Car("Skoda","Kamiq", 2017, "Sedan", 13000, 17000, "Manual", "Gasoline", "Black", 4)
d4 = Dealership("Skoda Kyiv", 4)

print(Operation.buy_car(d4, car4))
```
**Вивід**:
```py
Закупівля оформлена: автосалон Skoda Kyiv придбав Skoda Kamiq
Ціна закупівлі: 13000 $
```

5. ## `show_operation_history`
**Призначення**:
Відображає повну історію всіх операцій

**Як використовувати**:
```py
Operation.buy_car(d4, car4)
Operation.sell_car(client1, car1)
Operation.trade_in(client1, car2, car3, 1000)
Operation.leasing_car(client1, car4, 12, 10000)
        
print(Operation.show_operation_history())
```
**Вивід**:
```py
Історія операцій:Операція #1:
Тип: Закупівля
Автосалон: Skoda Kyiv
Автомобіль: Skoda Kamiq
Ціна закупівлі: 13000$
Операція #2:
Тип: Продаж
Клієнт: Maksim Artemenko
Автомобіль: BMW 5 Series
Ціна продажу: 12000$
Автосалон: BMW Kyiv
Операція #3:
Тип: Трейд-ін
Клієнт: Maksim Artemenko
Зданий автомобіль: Volvo V40
Отриманий автомобіль: Kia Rio
Вартість трейд-іну: 12000.0
Додаткова плата: 1000
Загальна сума: 4000.0
Операція #4:
Тип: Лізінг
Клієнт: Maksim Artemenko
Автомобіль: Skoda Kamiq
Перший внесок: 10000 ₴
Щомісячний платіж: 583.33
Загальна вартість: 17000 
```
# Author
Artemenko Maksim  11IPZ and Machok Oleksandr 11IPZ
