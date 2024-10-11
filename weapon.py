class weapon:
    def __init__(self, name: str, weapon_type: str, damage: int, value: int) -> None:
        self.name = name
        self.weapon_type = weapon_type
        self.damage = damage
        self.value = value


iron_sword = weapon(name="Iron Sword", weapon_type="sharp", damage=5, value=10)

steel_sword = weapon(name="Steel Sword", weapon_type="sharp", damage=50, value=15)

short_bow = weapon(name="Short Bow", weapon_type="ranged", damage=4, value=8)

fists = weapon(name="Fists", weapon_type="melee", damage=2, value=0)

wand = weapon(name="Wand", weapon_type="magic", damage=3, value=5)
