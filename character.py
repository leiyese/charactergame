import random

from weapon import fists, iron_sword, wand, short_bow
from health_bar import HealthBar


class Character:
    race = "Human"

    def __init__(self, name: str, health: int) -> None:
        self.name = name
        self.health = health
        self.health_max = health

        self.weapon = fists

        self.shield = 0.2

    def attack(self, target) -> None:
        target.health -= self.weapon.damage
        target.health = max(target.health, 0)
        target.health_bar.update()
        print(
            f"{self.name} dealt {self.weapon.damage} damage to "
            f"{target.name} with {self.weapon.name}"
        )

    def defend(self, target):
        self.damage = round(target.weapon.damage * self.shield)
        self.health -= self.damage
        print(
            f"{self.name} defended against {target.name}'s attack of {target.weapon.damage} "
            f"but took {self.damage}"
        )


class Hero(Character):
    def __init__(self, name: str, health: int) -> None:
        super().__init__(name=name, health=health)

        self.default_weapon = self.weapon
        self.health_bar = HealthBar(self, color="green")

    def equip(self, weapon) -> None:
        self.weapon = weapon
        print(f"{self.name} equiped a(n) {self.weapon.name}!")

    def drop(self) -> None:
        print(f"{self.name} dropped the {self.weapon.name}")
        self.weapon = self.default_weapon


class Enemy(Character):
    def __init__(self, name: str, health: int, weapon) -> None:
        super().__init__(name=name, health=health)
        self.weapon = weapon
        self.health_bar = HealthBar(self, color="red")


enemy_list = [
    Enemy(name="Goblin", health=random.randint(80, 100), weapon=short_bow),
    Enemy(name="Skeleton Warrior", health=random.randint(90, 120), weapon=iron_sword),
    Enemy(name="Lich", health=random.randint(60, 80), weapon=wand),
]
