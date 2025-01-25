# lab 3 coding questions
import random
# dice
diceOptions = list(range(1,7))

# weapons
weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear bomb"] 

print("Available Weapons: ", ", ".join(weapons))

def getCombatStrength(prompt):
    while True:
        value = int(input(prompt))
        if 1 <= value <= 6:
            return value
        else:
            print("Invalid input, enter value from 1-6")

heroCombatStrength = getCombatStrength("Please enter number between 1-6 for Player: ")
monsCombatStrength = getCombatStrength("Please enter number between 1-6 for Monster: ")

heroWinCount = monsWinCount = tieCount = 0

for i in range(1,21, 2):
    heroRoll = random.choice(diceOptions)
    monsRoll = random.choice(diceOptions)

    heroWeapon = weapons[heroRoll - 1]
    monsWeapon = weapons[monsRoll - 1]

    heroTotalStrength = heroRoll + heroCombatStrength
    monsTotalStrength = monsRoll + monsCombatStrength
    print(f"\n\nRound {i}:")
    print(f"Hero rolled {heroRoll}, selected {heroWeapon}, total strength: {heroTotalStrength}")
    print(f"Monster rolled {monsRoll}, selected {monsWeapon}, total strength: {monsTotalStrength}")
    if heroTotalStrength > monsTotalStrength:
        print("Hero wins!")
        heroWinCount += 1
    elif heroTotalStrength < monsTotalStrength:
        print("Monster wins!")
        monsWinCount += 1
    else:
        print("It's a tie")
        tieCount += 1
print("\nBattle truce at round 11")
print(f"Hero wins {heroWinCount} times")
print(f"Monster wins {monsWinCount} times")
print(f"Both tied {tieCount}")

