# Создайте класс cat и добавьте 3 атрибута (имя, окрас, возраст) и 3 метода класса (мяукнуть,
# мурлыкать и еще один на ваше усмотрение).
# Создайте 1 экземпляр класса и продемонстрируйте его атрибуты и методы.

class cat:
    def __init__(self, name, color, age = 1):
        self.name = name
        self.color = color
        self.age = age

    def meow(self, i = 0):
        print(f'Мяукнуть: {i}')
        self.meow = i

    def purr(self, i = 0):
        print(f'Мурлыкать: {i}')
        self.purr = i

    def cat_breed(self, breed):
        print(f'Порода: {breed}')
        self.cat_breed = breed

print('Показ атрибутов:')
tom = cat('Tom', 'grey', 3)
print(tom.name)
print(tom.color)
print(tom.age)

print()

print('Показ экземпляров:')
tom.meow(2)
print(tom.meow)
tom.purr(6)
print(tom.purr)
tom.cat_breed('Шотландская')
print(tom.cat_breed)
