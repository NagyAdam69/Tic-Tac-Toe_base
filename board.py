board = [
      [".", ".", "."],
      [".", ".", "."],
      [".", ".", "."]
      ]
winner = None

def display_board():
        
        
        print("\n   1   2   3")
        print(f"A   {board[0][0]} | {board[0][1]} | {board[0][2]}")
        print("   ---+---+---") 
        print(f"B   {board[1][0]} | {board[1][1]} | {board[1][2]}")
        print("   ---+---+---")
        print(f"C   {board[2][0]} | {board[2][1]} | {board[2][2]}")
        print("   ---+---+---\n")
        valasz = None

def check_for_winner():

    for row in board:
        if row[0] ==  row[1] ==  row[2] != "." :
            if row[1] == "x":
                winner = row[1]
            else:
                continue

            display_board()
            print("-" * 43)
            print(' ' * 11 + f'The winner is the {row[1]}!')
            print("-" * 43)
            print()
            exit()

        
    for col in range(3):
        if board[0][col] ==  board[1][col] == board[2][col] != "." :
            if board[0][col] == "x":
                winner = board[0][col]
            else:
                continue
            
            display_board()
            print("-" * 43)
            print(' ' * 11 + f'The winner is the {board[0][col]}!')
            print("-" * 43)
            print()
            exit()
    

    if board[0][0] ==  board[1][1] == board[2][2] != "." or board[0][2] ==  board[1][1] == board[2][0] != ".":
        if board[1][1] == "x":
                winner = board[1][1]
            else:
                continue
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