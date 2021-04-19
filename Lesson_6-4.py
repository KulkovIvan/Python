# Реализуйте базовый класс Car. У данного класса должны быть следующие
# атрибуты: speed, color, name, is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать,
# что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} поехала')

    def stop(self):
        print(f'{self.name} остановилась')

    def turn_right(self):
        print(f'{self.name} повернул направо')

    def turn_left(self):
        print(f'{self.name} повернул налево')

    def show_speed(self):
        print(f'Текущая скорость {self.name} равна {self.speed} км/ч')

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'{self.name} едет со скоростью {self.speed} км/ч. Превышает скорость !!!!')
        else:
            print(f'{self.name} едет с допустимой скоростью {self.speed} км/ч')

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'{self.name}  едет со скоростью {self.speed} км/ч. Превышает скорость !!!!')
        else:
            print(f'{self.name} едет с допустимой скоростью {self.speed} км/ч')

class SportCar(Car):
    def show_speed(self):
        if self.speed > 100:
            print(f'{self.name} превышает скорость. {self.speed} км/ч !!!! Но это же спорткар ) ')
        else:
            print(f'{self.name} едет с допустимой скоростью {self.speed} км/ч, скучно (')

class PoliceCar(Car):
    def police(self):
        if self.is_police == True:
            print(f'в {self.name}  копы !!!!!!')
        else:
            print(f'Все в порядке, {self.name} обычная машина')


porshe = SportCar(150, 'оранжевый', 'Porshe', False)
skoda = TownCar(65, 'серый', 'Skoda', False)
kamaz = WorkCar(45, 'белый', 'Kamaz', False)
police = PoliceCar(50,'бело-голубой', 'Lada', True)
porshe.show_speed()
kamaz.turn_left()
skoda.go()
skoda.show_speed()
skoda.stop()
police.police()

