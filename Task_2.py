# Создайте класс Good, который будет вычислять значения стоимости товаров.
# В качестве атрибутов пусть будут:
# name (имя товара),
# price(цена за 1 кг),
# cost (стоимость),
# weight(масса);

# в качестве методов:
# calc - вычисляющий стоимость товара.

# Реализуйте два экземпляра класса Good:
# Яблоки apple('apple', price = 100, weight = 1.5)
# Груши pear('pear', price = 120, weight = 0.8)
# Выведите их стоимость

class Good:
    def __init__(self, name, price, weight, cost = 0):
        self.name = name
        self.price = price
        self.cost = cost
        self.weight = weight

    def calc(self):
        self.cost = self.price * self.weight

apple = Good('apple', 100, 1.5)
print(f'Имя товара: {apple.name}')
apple.calc()
print(f'Стоимость: {apple.cost} рублей')

print()

pear = Good('pear', 120, 0.8)
print(f'Имя товара: {pear.name}')
pear.calc()
print(f'Стоимость: {pear.cost} рублей')