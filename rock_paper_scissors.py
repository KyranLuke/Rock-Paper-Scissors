import random

def play():
    player = input("Quartz, Parchment or Shears ")
    player = player.lower()

    computer = random.choice(["quartz", "parchment", "shears"])

    if player == computer:
        print ("Tie!")
    elif player == "quartz":
        if computer == "parchment":
            print("You have chosen {} and the computer has chosen {} You Lost!".format(player, computer))
        if computer == "shears":
            print("You have chosen {} and the computer has chosen {} You Won!".format(player, computer))
    elif player == "shears":
        if computer == "parchment":
            print("You have chosen {} and the computer has chosen {} You Won!".format(player, computer))
        if computer == "quartz":
            print("You have chosen {} and the computer has chosen {} You Lost!".format(player, computer))
    elif player == "parchment":
        if computer == "shears":
            print("You have chosen {} and the computer has chosen {} You Lost!".format(player, computer))
        if computer == "quartz":
            print("You have chosen {} and the computer has chosen {} You Won!".format(player, computer))
    else:
        print("Invalid Input")

play()   