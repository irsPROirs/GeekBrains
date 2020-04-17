class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(self.name, 'поехала')

    def stop(self):
        print(self.name, 'остановилась')

    def turn(self, direction):
        print(self.name, 'повернула на', direction)

    def show_speed(self):
        print(self.name, 'едет со скоростью', self.speed)


class TownCar(Car):
    def show_speed(self):
        print(self.name, 'едет со скоростью', self.speed)
        if self.speed > 60:
            print('Превышение скорости')


class WorkCar(Car):
    def show_speed(self):
        print(self.name, 'едет со скоростью', self.speed)
        if self.speed > 40:
            print('Превышение скорости')


class PoliceCar(Car):
    def lights(self):
        print('Включаю мигалки')


class SportCar(Car):
    pass


town = TownCar(200, 'black', 'town_car', False)
town.go()
town.turn('направо')
town.show_speed()

work = WorkCar(30, 'blue', 'work_car', False)
print('скорость', work.name, work.speed)
work.show_speed()

police = PoliceCar(150, 'white', 'police_car', True)
police.show_speed()
print(police.is_police)
police.lights()

sport = SportCar(300, 'yellow', 'sport_car', False)
sport.go()
sport.show_speed()
