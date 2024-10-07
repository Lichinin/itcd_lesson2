class Toy:

    def __init__(self, name, color, toy_type):
        self.name = name
        self.color = color
        self.toy_type = toy_type

    def __str__(self) -> str:
        return (
            f'Это игрушка типа "{self.toy_type}". '
            f'Её цвет "{self.color}". А зовут её "{self.name}". '
            f'Класс игрушки: "{self.__class__.__name__}"'
        )


class AnimalToy(Toy):
    pass


class SoldierToy(Toy):
    pass


class ProgrammerToy(Toy):
    pass


class ToyFabric:
    TOY_TYPES = {
        'animal': AnimalToy,
        'soldier': SoldierToy,
        'programmer': ProgrammerToy
    }

    def buy_materials(self, name, toy_type):
        print(
            f'Покупаем материалы для игрушки '
            f'типа "{toy_type}" с именем "{name}"'
        )

    def sew(self, name, toy_type):
        print(f'Шьем игрушку типа "{toy_type}" с именем "{name}"')

    def paint(self, name, color, toy_type):
        print(
            f'Окрашиваем игрушку типа "{toy_type}" '
            f'с именем "{name}" в цвет "{color}"'
        )

    def create_toy(self, name, color, toy_type):
        try:
            toy_class = self.TOY_TYPES[toy_type]
            self.buy_materials(name, toy_type)
            self.sew(name, toy_type)
            self.paint(name, color, toy_type)
            print(
                f'Игрушка готова:\nТип: "{toy_type}"\n'
                f'Имя: "{name}"\nЦвет: "{color}"\n'
                f'Класс игрушки: "{toy_class.__name__}"'
            )
            return toy_class(name, color, toy_type)
        except KeyError:
            print(
                'Некорректный тип игрушки. Можно создавать'
                f'игрушки типа {", ".join(self.TOY_TYPES.keys())}'
            )


if __name__ == '__main__':
    fabric = ToyFabric()
    print('--- Создаем игрушку корректно ---')
    soldier = fabric.create_toy('Igor', 'red', 'soldier')
    print(soldier)
    print('--- Создаем игрушку несуществующего типа ---')
    bad_soldier = fabric.create_toy('Igor', 'red', 'Soldvier')
