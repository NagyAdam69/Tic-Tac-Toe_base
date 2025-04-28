board = [
      [".", ".", "."],
      [".", ".", "."],
      [".", ".", "."]
      ]
winner = None
from sign_in import sign_or_log, get_current_user

def display_board():
    print(f'\n\ncurrent user:{get_current_user()}')        
        
    print("\n   1   2   3")
    print(f"A   {board[0][0]} | {board[0][1]} | {board[0][2]}")
    print("   ---+---+---") 
    print(f"B   {board[1][0]} | {board[1][1]} | {board[1][2]}")
    print("   ---+---+---")
    print(f"C   {board[2][0]} | {board[2][1]} | {board[2][2]}")
    print("   ---+---+---\n")
    valasz = None

def update_user_points():
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

def check_for_winner():
    global winner
    
    for row in board:
        if row[0] == row[1] == row[2] != ".":
            winner = row[0].lower()  # Convert to lowercase for consistency
            if winner == "x":
                update_user_points()
            display_board()
            print("-" * 43)
            print(' ' * 11 + f'The winner is the {row[0]}!')
            print("-" * 43)
            print()
            exit()

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != ".":
            winner = board[0][col].lower()  # Convert to lowercase for consistency
            if winner == "x":
                update_user_points()
            display_board()
            print("-" * 43)
            print(' ' * 11 + f'The winner is the {board[0][col]}!')
            print("-" * 43)
            print()
            exit()

    if board[0][0] == board[1][1] == board[2][2] != "." or board[0][2] == board[1][1] == board[2][0] != ".":
        winner = board[1][1].lower()  # Convert to lowercase for consistency
        if winner == "x":
            update_user_points()
        display_board()
        print("-" * 43)
        print(' ' * 11 + f'The winner is the {board[1][1]}!')
        print("-" * 43)
        print()
        exit()

    if "." not in board[0] and "." not in board[1] and "." not in board[2]:
        display_board()
        print("-" * 43)
        print(' ' * 15 + f'It is a tie!')
        print("-" * 43)
        print()
        exit()
