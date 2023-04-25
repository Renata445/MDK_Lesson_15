# Создайте класс Car, реализуйте в нем 5 атрибутов :
# цвет,
# марку,
# кузов (сидан sedan, грузовик truck),
# скорость,
# тип коробки передач;

# и 6 методов:
# start - заставляет начинать движение
# stop - останавливает машину
# turn - поворачивает машину в какую-либо сторону, и выводит сообщение:" Машина повернула налево"
# speed_up - ускоряет автомобиль
# speed_down - замедляет автомобиль
# beep - сигналит
# Создайте два экземпляра класса truck и car. Продемонстрируйте работу всех методов

class Car:
    def __init__(self, brand, color, body, transmission, speed = 0):
        self.brand = brand
        self.color = color
        self.body = body
        self.transmission = transmission
        self.speed = speed

    def start(self):
        print('Скорость = 10 км/ч')
        self.speed = 10

    def stop(self):
        print('Скорость = 0 км/ч')
        self.speed = 0

    def speed_up(self, i=1):
        print(f'Скорость = {self.speed + i} км/ч')
        self.speed += i

    def speed_down(self, i=1):
        if self.speed == 0:
            print('Скорость = 0 км/ч')
        else:
            print(f'Скорость = {self.speed - i} км/ч')
            self.speed -= i

    def turn(self, side):
        print(f'Машина повернула на {side}')
        self.turn = side

    def beep(self):
        print('Машина сигналит')

car = Car('Honda', 'black', 'sedan', 'mechanical')
print(f'Текущая скорость автомобиля: {car.speed}')

print()

print('Начнем движение')
car.start()

print()

print('Автомобиль прибавил скорость:')
car.speed_up(32)

print()

print('Автомобиль снизил скорость:')
car.speed_down(25)

print()

print('Автомобиль сменил траекторию:')
car.turn('право')

print()

print('Автомобиль остановился: ')
car.stop()

print()

car.beep()
print()

print('__________________________________________________________')

truck = Car('Honda', 'black', 'sedan', 'mechanical')
print(f'Текущая скорость автомобиля: {truck.speed}')

print()

print('Начнем движение')
truck.start()

print()

print('Автомобиль прибавил скорость:')
truck.speed_up(32)

print()

print('Автомобиль снизил скорость:')
truck.speed_down(25)

print()

print('Автомобиль сменил траекторию:')
truck.turn('право')

print()

print('Автомобиль остановился: ')
truck.stop()

print()

truck.beep()
