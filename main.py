from vs_human import vs_human
from vs_ai import vs_ai
from sign_in import sign_or_log, get_current_user
from board import winner

def update_points():
    current_user = get_current_user()
    if current_user:
        with open("felhasznalok.txt", "r", encoding="utf-8") as f:
            lines = f.readlines()
        
        with open("felhasznalok.txt", "w", encoding="utf-8") as f:
            for line in lines:
                user, password, points = line.strip().split(";")
                if user == current_user:
                    points = str(int(points) + 1)
                f.write(f"{user};{password};{points}\n")

sign_or_log()

while True:
    gamemode = input("\nChoose a gamemode!\n1: Human vs. Human\n2: Human vs. AI\n3: Human vs. AI (UNBEATABLE)\n(1 or 2 or 3):")

    if gamemode == "1":
        vs_human()

    elif gamemode == "2":
        vs_ai()
        if winner == "x":
            update_points()

    elif gamemode == "3":
        print()

    else:
        print("\nPlease choose from the available options.")