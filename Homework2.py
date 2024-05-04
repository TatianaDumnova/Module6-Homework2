# ДЗ по теме "Множественное наследование"
class Vehicle: # родительский (базовый) класс
    vehicle_type = 'none'


class Car: # родительский (базовый) класс
    price = 1000000

    def horse_power(self):
        return 'Количество лошадиных сил: 200'


class Nissan(Car, Vehicle): # Наследник класса Car, Vehicle
    price = 1200000  # Переопределение свойств
    vehicle_type = 'Minivan'

    def __str__(self):
        return 'Model: {}, Type: {}, Price: {}'.format(
            self.__class__.__name__,self.vehicle_type, self.price)

    def horse_power(self):  # Переопределение функции
        return 'Количество лошадиных сил: 200'


nissan = Nissan()
print(nissan)  # Распечатываю все параметры через __str__
print(nissan.horse_power())  # Распечатываю переопределенную функцию
print(nissan.vehicle_type, nissan.price)  # Распечатываю только vehicle_type и price
