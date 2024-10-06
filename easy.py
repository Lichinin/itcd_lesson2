class Car:
    def __init__(
        self,
        speed: int,
        color: str,
        name: str,
        is_police: bool = False
    ):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        self.is_moving = False
        self.direction = None

    def go(self):
        self.is_moving = True
        print(f'Car {self.name} started move')

    def stop(self):
        self.is_moving = False
        print(f'Car {self.name} stoped')

    def turn(self, direction: str):
        self.direction = direction


class TownCar(Car):
    pass


class SportCar(Car):
    pass


class WorkCar(Car):
    pass


class PoliceCar(Car):
    def __init__(self, speed: int, color: str, name: str):
        super().__init__(speed, color, name, is_police=True)
