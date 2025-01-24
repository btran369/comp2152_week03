# lab 3 coding questions
# dice
diceOptions = list(range(1,7))

# weapons
weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear bomb"] 

print("Available Weapons: ", ", ".join(weapons))

def getCombatStrength(prompt):
    while True:
        value = input(prompt)
        if 1 <= value <= 6:
            return value
        else:
            print("Invalid input, enter value from 1-6")