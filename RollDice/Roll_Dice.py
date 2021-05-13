import random

def main():
    player1 = 0
    player2 = 0
    rounds = 1

    while rounds != 4:
         print("Round" + str(rounds))
         player1 = roll_dice()
         player2 = roll_dice()
         print("player 1 roll: " + str(player1))
         print("player 2 roll: " + str(player2))
         rounds = rounds + 1

def roll_dice():
    rollDice = random.randint(1, 6)
    return rollDice

main()