import os  # Imported for system clear
from datetime import datetime  # Imported for savefile to log date
import random  # Imported to randomize predetermined enemies

# Importing character and weapon classes
from character import Hero, enemy_list
from weapon import short_bow, iron_sword, steel_sword, fists

# Creating hero and enemies
hero = Hero(name="Hero", health=100)

counter = [random.randrange(0, 3, 1) for i in range(random.randint(1, 3))]
enemies = []
for i in counter:
    enemies.append(enemy_list[i])


# ActionError class
class ActionError(Exception):
    """Exception when file error occurs"""

    pass


# Function for user input for hero outside battle
def user_input():
    print("\nMENU")
    print("1 Fight an enemy")
    print("2 Rest")
    print("3 Return home(exit game)")
    print("==================")
    try:
        action = int(input("Choose an action! (1-3) "))
        if 0 > action or action > 3:
            raise ActionError("Wrong Action!")
        return action
    except ActionError as e:
        print(e)
    except ValueError:
        print("Invalid action! Please enter a valid action number.")


# Function for user input for hero when in battle
def battle_input():
    print("\nMENU")
    print("1 Attack")
    print("2 Defend")
    print("3 Equip a weapon")
    print("==================")
    try:
        action = int(input("Choose an action! (1-3) "))
        if 0 > action or action > 3:
            raise ActionError("Wrong Action!")
        return action
    except ActionError as e:
        print(e)
    except ValueError:
        print("Invalid action! Please enter a valid action number.")


# Function for battle actions based on user input
def battle_actions(action, hero, enemy):
    if action == 1:
        hero.attack(enemy)
        enemy.attack(hero)
    if action == 2:
        hero.defend(enemy)
    if action == 3:
        hero.drop()
        hero.equip(inventory())


# Function for breaks in the game
def input_break():
    input("\n--Press Any key to continue--")


# Function for showing inventory and choosing new weapon and returning a weapon
def inventory():
    while True:
        os.system("clear")
        print("===== INVENTORY =====\n")
        print(f"1 {iron_sword.name:14} (dmg: {iron_sword.damage})")
        print(f"2 {short_bow.name:14} (dmg: {short_bow.damage})")
        print(f"3 {steel_sword.name:14} (dmg: {steel_sword.damage})")
        print(f"4 {fists.name:14} (dmg: {fists.damage})")
        print("=====================\n")
        try:
            weapon_choice = int(input("Choose your weapon (1-4) "))
            if 0 > weapon_choice or weapon_choice > 4:
                raise ActionError("Wrong Action!")
            else:
                if weapon_choice == 1:
                    return iron_sword
                if weapon_choice == 2:
                    return short_bow
                if weapon_choice == 3:
                    return steel_sword
                if weapon_choice == 4:
                    return fists
        except ActionError as e:
            print(e)
            input_break()
        except ValueError:
            print("Invalid action! Please enter a valid action number.")
            input_break()


# Function to save battle results
def save_info(win: bool, enemy: str):
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    result = "Win" if win else "Defeated"

    try:
        with open("save_data.txt", "a") as file:
            if win == True:
                file.write(f"[Date Time] {time}: Win by defeating {enemy}!\n")
            else:
                file.write(f"[Date Time] {time}: Loss by {enemy}!\n")
        print("The savefile is updated.")
    except FileNotFoundError:
        print("The savefile could not be found!")


# MAIN PROGRAM
win = False  # This variable was added to use in save_info function
for enemy in enemies:  # We have to defeat all randomized enemies in order to win
    while win == False:
        if hero.health > 0:
            os.system("clear")
            hero.health_bar.draw()  # Prints the healthbar for the hero
            user = user_input()  # Returns the userinput

            if user == 1:
                print(f"\n---You have encountered {enemy.name}---\n")
                input_break()
                while True:
                    os.system("clear")
                    hero.health_bar.draw()  # Draws the current healthbar for the hero
                    enemy.health_bar.draw()  # Draws the current healthbar for the enemy

                    # Calling battle function with input from user
                    battle_actions(battle_input(), hero, enemy)

                    # If hero has 0 HP user looses and the log is updated
                    if hero.health <= 0:
                        print(f"{hero.name} died. Game over.")
                        save_info(win, enemy.name)
                        exit()
                    # If enemy has 0 HP we break loop and go back to main menu
                    if enemy.health <= 0:
                        print(f"You have defeated {enemy.name}! You won!")
                        input_break()
                        break
                    input_break()
                break
            if user == 2:  # Resting option, sets hero health to max again
                print(f"\n{hero.name} is being lazy as f.. but healed to max health!")
                hero.health = 100
                hero.health_bar.update()  # Need to update bar after setting new health
                input_break()

            if user == 3:  # player can choose to quite, but it will be logged
                print(f"You have Lost! Bye Bye")
                save_info(win, "Deserting")
                exit()
win = True
# After defeating all the enemies, it will be logged as a win
save_info(win, enemy.name)
