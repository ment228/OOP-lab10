class Transport: #новый класс Transport

    def __init__(self, brand, max_speed, kind=None): # Конструктор с параметрами: бренд, максимальная скорость, и тип по умолчанию.
        self.brand = brand
        self.max_speed = max_speed
        self.kind = kind

    def __str__(self): #Метод для возврата строки
        return f'тип транспорта {self.kind} марки {self.brand} может развить скорость {self.max_speed} км/ч'

class Car(Transport): #новый класс Car наследующий от Transport.

    def __init__(self, brand, max_speed, mileage, gasoline_residue): # Конструктор класса Car с дополнительными параметрами.
        super().__init__(brand, max_speed, kind='Car') #Вызов конструктора родительского класса.
        self.mileage = mileage
        self.__gasoline_residue = gasoline_residue #Приватный атрибут для остатка бензина.

    @property
    def gasoline(self): #Определение свойства для получения остатка бензина.
        return f'Осталось бензина на {self.__gasoline_residue} км'

    @gasoline.setter #Определение метода-сеттера для свойства gasoline.
    def gasoline(self, value):#Проверка и установка значения остатка бензина.
        if isinstance(value, int):
            self.__gasoline_residue += value
            print(f'объем топлива увеличен на {value} л и составляет {self.__gasoline_residue} л')
        else:
            print('ошибка заправки автомобиля')

class Boat(Transport): #Определение класса Boat, наследующего от Transport.

    def __init__(self, brand, max_speed, owners_name): #Конструктор класса Boat.
        super().__init__(brand, max_speed, kind='Boat') #Вызов конструктора родительского класса.
        self.owners_name = owners_name

    def __str__(self): #Метод для возврата строкового представления объекта Boat.
        return f'этой лодкой марки {self.brand} владеет {self.owners_name}'

class Plane(Transport): #Определение класса Plane, наследующего от Transport.

    def __init__(self, brand, max_speed, capacity): #Конструктор класса Plane.
        super().__init__(brand, max_speed, kind='Plane') #Вызов конструктора родительского класса.
        self.capacity = capacity

    def __str__(self): #Метод для возврата строкового представления объекта Plane.
        return f'Самолёт марки {self.brand} вмещает в себя {self.capacity} людей'


transport = Transport('Telega', 10)
print(transport)  # Тип транспорта None марки Telega может развить скорость 10 км/ч
bike = Transport('shkolnik', 20, 'bike')
print(bike)  # Тип транспорта bike марки shkolnik может развить скорость 20 км/ч
first_plane = Plane('Virgin Atlantic', 700, 450)
print(first_plane)  # Самолет марки Virgin Atlantic вмещает в себя 450 людей
first_car = Car('BMW', 230, 75000, 300)
print(first_car)  # Тип транспорта Car марки BMW может развить скорость 230 км/ч
print(first_car.gasoline)  # Осталось бензина на 300 км
first_car.gasoline = 20  # Печатает 'Объем топлива увеличен на 20 л и составляет 320 л'
print(first_car.gasoline)  # Осталось бензина на 320 км
second_car = Car('Audi', 230, 70000, 130)
second_car.gasoline = [None]  # Печатает 'Ошибка заправки автомобиля'
first_boat = Boat('Yamaha', 40, 'Petr')
print(first_boat)  # Этой лодкой марки Yamaha владеет Petr
