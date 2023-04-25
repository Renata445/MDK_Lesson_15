# Создайте класс светофор (trafficlight).
# Реализуйте в нем метод, который будет переключать цвета (red, green, yellow)
# по определенному времени: red = 1 сек, green 2 сек, yellow = 0.5 сек.
# Подсказка:
# Воспользуйтесь модулем time. В нем есть функция sleep

from time import sleep

class trafficlight:
    red_wait = 1
    yellow_wait = 2
    green_wait = 0.5

    red_name = 'красный'
    yellow_name = 'желтый'
    green_name = 'зеленый'

    def __init__(self, color = 'красный'):
        self.color = color

    def switch_light(self, color, wait_period):
        self.wait_period = wait_period
        print(f'Включен {color} свет, время ожидания {self.wait_period} сек')
        sleep(self.wait_period)

    def running(self, color=''):
        if not color:
            l_color = self.color
        else:
            l_color = color

        if l_color == self.red_name:
            self.switch_light('красный', self.red_wait)
            self.switch_light('желтый', self.yellow_wait)
            self.switch_light('зеленый', self.green_wait)
        elif l_color == self.yellow_name:
            self.switch_light('желтый', self.yellow_wait)
            self.switch_light('зеленый', self.green_wait)
        else:
            self.switch_light('зеленый', self.green_wait)

        print('Светофор прекратил переключение цветов')

tl1 = trafficlight()
tl1.running()

