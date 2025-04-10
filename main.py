from vs_human import vs_human
from vs_ai import vs_ai
from sign_in import sign_or_log, get_current_user

sign_or_log()
# print(f'current user:{get_current_user()}')

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