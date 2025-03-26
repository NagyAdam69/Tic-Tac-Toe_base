import random
from board import display_board
from board import check_for_winner
from vs_human import vs_human
from board import board
from vs_ai import vs_ai

while True:
    gamemode = input("\nChoose a gamemode!\n1: Human vs. Human\n2: Human vs. AI\n3: Human vs. AI (UNBEATABLE)\n(1 or 2 or 3):")

    if gamemode == "1":
        vs_human()

    elif gamemode == "2":
        vs_ai()

    elif gamemode == "3":
        print()

    else:
        print("\nPlease choose from the available options.")