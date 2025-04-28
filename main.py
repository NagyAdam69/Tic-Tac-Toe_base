from vs_human import vs_human
from vs_ai import vs_ai
from sign_in import sign_or_log, get_current_user
from board import winner, board

def update_points():
    current_user = get_current_user()
    if current_user:
        try:
            with open("felhasznalok.txt", "r", encoding="utf-8") as f:
                lines = f.readlines()
            
            updated_lines = []
            for line in lines:
                user, password, points = line.strip().split(";")
                if user == current_user:
                    points = str(int(points) + 1)
                updated_lines.append(f"{user};{password};{points}\n")
            
            with open("felhasznalok.txt", "w", encoding="utf-8") as f:
                f.writelines(updated_lines)
        except Exception as e:
            print(f"Error updating points: {e}")

sign_or_log()

while True:
    board = [["." for _ in range(3)] for _ in range(3)]
    
    gamemode = input("\nChoose a gamemode!\n1: Human vs. Human\n2: Human vs. AI\n(1 or 2):")

    if gamemode == "1":
        vs_human()

    elif gamemode == "2":
        vs_ai()
        if winner == "x":
            update_points()

    else:
        print("\nPlease choose from the available options.")