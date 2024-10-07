class Person:
    def __init__(self, health: int, damage: int, armor: int):
        self.health = health
        self.damage = damage
        self.armor = armor
        self.is_live = True

    def _calculate_damage(self, opponent):
        if opponent.armor == 0 and opponent.health <= self.damage:
            opponent.is_live = False
            print(
                f'КОНЕЦ! {self.__class__.__name__} '
                f'победил {opponent.__class__.__name__}!'
            )
        else:
            print(
                f'{self.__class__.__name__} '
                f'атакует {opponent.__class__.__name__}'
            )

            if opponent.armor >= self.damage:
                opponent.armor -= self.damage
            else:
                damage = abs(opponent.armor - self.damage)
                opponent.armor = 0
                if opponent.health > damage:
                    opponent.health -= damage
            print(
                f'Состояние {opponent.__class__.__name__} '
                f'после атаки: здоровье {opponent.health},'
                f'броня {opponent.armor}'
            )

    def attack(self, opponent):
        opponent._calculate_damage(self)


class Player(Person):
    pass


class Enemy(Person):
    pass


class Game:
    def __init__(self, player: Person, enemy: Person):
        self.player = player
        self.enemy = enemy

    def run(self):
        print(
            'Бой начинается!\n'
            f'Характеристики {player.__class__.__name__}: '
            f'Здоровье {player.health}, Сила удара {player.damage}, '
            f'Броня {player.armor}\n'
            f'Характеристики {enemy.__class__.__name__}: '
            f'Здоровье {enemy.health}, Сила удара {enemy.damage}, '
            f'Броня {enemy.armor}\n'
        )
        while player.is_live and enemy.is_live:
            if player.is_live and enemy.is_live:
                player.attack(enemy)
            if player.is_live and enemy.is_live:
                enemy.attack(player)


player = Player(50, 53, 100)
enemy = Enemy(100, 10, 100)

game = Game(player, enemy)
game.run()
