import os

os.system("")


# Healthbar class, with constant variables and attributes for the look of the healthbar in the terminal
class HealthBar:
    symbol_remaining: str = "█"
    symbol_lost: str = "_"
    barrier: str = "|"
    # Creating a dictionary for ANSI escape codes for text colors in the terminal
    colors: dict = {
        "red": "\033[91m",
        "purple": "\33[95m",
        "blue": "\33[34m",
        "green": "\033[92m",
        "brown": "\33[33m",
        "yellow": "\33[93m",
        "grey": "\33[37m",
        "default": "\033[0m",
    }

    def __init__(
        self, entity, length: int = 20, is_colored: bool = True, color: str = ""
    ) -> None:
        # this is the character that we want to project the health for
        self.entity = entity
        # The current health of the character
        self.current_value = entity.health
        # The max health of the character, which is a contant value
        self.max_value = entity.health_max
        # The length of the healthbar, this is constant for now, but can be changed depending on boss battle
        self.length = length

        # The color of the healthbar is different for hero and enemies
        self.is_colored = is_colored
        self.color = self.colors.get(color) or self.colors("default")

    # The update health function
    def update(self) -> None:
        self.current_value = self.entity.health

    # The function to project the health for the entity in the terminal
    def draw(self) -> None:
        remaining_bars = round(self.current_value / self.max_value * self.length)
        lost_bars = self.length - remaining_bars
        print(
            f"{self.entity.name}'s HEALTH: {self.entity.health}/{self.entity.health_max}"
        )
        # The look I want is this: |████████████████████|
        print(
            f"{self.barrier}"
            f"{self.color if self.is_colored else ''}"
            f"{remaining_bars * self.symbol_remaining}"
            f"{lost_bars * self.symbol_lost}"
            f"{self.colors['default'] if self.is_colored else ''}"
            f"{self.barrier}"
        )
