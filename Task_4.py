# Добавьте ограничение скорости в класс Car из предыдущего задания:
# для грузовика(truck) 60 км/ч, а для легкового(car) - 80 км/ч.
# При превышении пусть на экран выводится предупреждение:
# "Скорость превышена! Разрешенная скорость 60 км/ч"

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

    def speed_up_car(self, i=1):
        if self.speed + i <= 80:
            print(f'Скорость = {self.speed + i} км/ч')
            self.speed += i
        else:
            print('Скорость превышена! Разрешенная скорость 80 км/ч')

    def speed_up_truck(self, i=1):
        if self.speed + i <= 60:
            print(f'Скорость = {self.speed + i} км/ч')
            self.speed += i
        else:
            print('Скорость превышена! Разрешенная скорость 60 км/ч')


car = Car('Honda', 'black', 'sedan', 'mechanical')
print(f'Текущая скорость автомобиля: {car.speed}')

print()

print('Начнем движение')
car.start()

print()

print('Автомобиль прибавил скорость:')
car.speed_up_car(85)

print()

print('Автомобиль остановился: ')
car.stop()

print()

print('__________________________________________________________')

truck = Car('Honda', 'black', 'sedan', 'mechanical')
print(f'Текущая скорость автомобиля: {truck.speed}')

print()

print('Начнем движение')
truck.start()

print()

print('Автомобиль прибавил скорость:')
truck.speed_up_truck(62)

print()

print('Автомобиль остановился: ')
truck.stop()
