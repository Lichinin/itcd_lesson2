class Toy:

    def __init__(self, name, color, toy_type):
        self.name = name
        self.color = color
        self.toy_type = toy_type

    def __str__(self) -> str:
        return (
            f'Это игрушка типа "{self.toy_type}". '
            f'Её цвет "{self.color}". А зовут её "{self.name}".'
        )


class ToyFabric:

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
        self.buy_materials(name, toy_type)
        self.sew(name, toy_type)
        self.paint(name, color, toy_type)
        print(
            f'Игрушка готова:\nТип: "{toy_type}"\n'
            f'Имя: "{name}"\nЦвет: "{color}"'
        )
        return Toy(name, color, toy_type)


if __name__ == '__main__':
    fabric = ToyFabric()
    bear = fabric.create_toy('Igor', 'red', 'bear')
    print(bear)
