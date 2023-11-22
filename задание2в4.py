'''Создать родительский класс «Путевки» (код путевки, фамилия клиента,
 название пансионата, номер, вид жилья, дата заезда,
дата выезда, количество человек, цена) и дочерние классы:
«Зарубежные путевки» (загран паспорт, страховка);
«Санатории» ( мед.полис, диагноз, направление);
«Детские оздоровительные» (возраст ребенка, свидетельство о рождении, пол).

'''
class Putevki:#новый класс Pytevki
    def __init__(self, kod, surname, pension_name, room_number, life_type, zaezd_in_date, zaezd_out_date, num_people, price):#коструктор с параметрами kod, surname, pension_name, room_number, accommodation_type, check_in_date, check_out_date, num_people, price
        self.kod = kod
        self.surname = surname
        self.pension_name = pension_name
        self.room_number = room_number
        self.life_type = life_type
        self.zaezd_in_date = zaezd_in_date
        self.zaezd_out_date = zaezd_out_date
        self.num_people = num_people
        self.price = price#инициализируем параметры

    def __str__(self):#метод для возвращения строки
        return f"Код путевки: {self.kod} Фамилия клиента: {self.surname} Название пансионата: {self.pension_name} Номер: {self.room_number} Вид жилья: {self.life_type} Дата заезда: {self.zaezd_in_date} Дата выезда: {self.zaezd_out_date} Количество человек: {self.num_people} Цена: {self.price}"


class ZarubezhnyePutevki(Putevki):#новый класс наследующий от transport
    def __init__(self, kod, surname, pension_name, room_number, life_type, zaezd_in_date, zaezd_out_date, num_people, price, passport, insurance):#конструктор класса ZarybejniePytevki с параметрами kod, surname, pension_name, room_number, accommodation_type, check_in_date, check_out_date, num_people, price, passport, insurance
        super().__init__(kod, surname, pension_name, room_number, life_type, zaezd_in_date, zaezd_out_date, num_people, price)#Вызов конструктора родительского класса
        self.passport = passport
        self.insurance = insurance

    def __str__(self):#метод для возврата строки
        return f"{super().__str__()} Загран паспорт: {self.passport} Страховка: {self.insurance}"


class Sanatorii(Putevki):#новый класс наследующий от transport
    def __init__(self, kod, surname, pension_name, room_number, life_type, zaezd_in_date, zaezd_out_date, num_people, price, medical_policy, diagnosis, direction):#конструктор с параметрами kod, surname, pension_name, room_number, accommodation_type, check_in_date, check_out_date, num_people, price, medical_policy, diagnosis, direction
        super().__init__(kod, surname, pension_name, room_number, life_type, zaezd_in_date, zaezd_out_date, num_people, price)#Вызов конструктора родительского класса
        self.medical_policy = medical_policy
        self.diagnosis = diagnosis
        self.direction = direction#инициализируем параметры

    def __str__(self):#метод для возврата строки
        return f"{super().__str__()} Мед.полис: {self.medical_policy} Диагноз: {self.diagnosis} Направление: {self.direction}"


class DetskieOzdorovitelnye(Putevki):#новый класс наследующий от transport
    def __init__(self, kod, surname, pension_name, room_number, life_type, zaezd_in_date, zaezd_out_date, num_people, price, age, birth_certificate, gender):#конструктор с параметрами kod, surname, pension_name, room_number, accommodation_type, check_in_date, check_out_date, num_people, price, age, birth_certificate, gender
        super().__init__(kod, surname, pension_name, room_number, life_type, zaezd_in_date, zaezd_out_date, num_people, price)#Вызов конструктора родительского класса
        self.age = age
        self.birth_certificate = birth_certificate
        self.gender = gender#инициализируем параметры

    def __str__(self):#метод для возврата строки
        return f"{super().__str__()} Возраст ребенка: {self.age} видетельство о рождении: {self.birth_certificate} Пол: {self.gender}"


#пример создания экземпляров классов
zarubezhnye = ZarubezhnyePutevki(312, "Мишенков", "Пансионат Солнечный", 228, "бомж общага", "12 сентября 2065", "28 сентября 2065", 12, 500, "8941244120", "Страховка 3123")
print(zarubezhnye)
sanatorii = Sanatorii(321, "Побединский", "Санаторий Здоровье", 998, "хороший", "4 августа 2043", "28 августа 2043", 1, 700, "423412412", "Диагноз", "Направление")
print(sanatorii)
detskie = DetskieOzdorovitelnye(52, "Алексеев", "Пансионат Дружба", 333, "V.I.P", "29 ноября 2023", "20 декабря 2023", 1, 40000, 9, "Свидетельство 4214125", "Мужской")
print(detskie)