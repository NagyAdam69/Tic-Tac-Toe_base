board = [
    [".", ".", "."],
    [".", ".", "."],
    [".", ".", "."]
    ]

def display_board():
        # board visualisation
        print("\n   1   2   3")
        print(f"A   {board[0][0]} | {board[0][1]} | {board[0][2]}")
        print("   ---+---+---") 
        print(f"B   {board[1][0]} | {board[1][1]} | {board[1][2]}")
        print("   ---+---+---")
        print(f"C   {board[2][0]} | {board[2][1]} | {board[2][2]}")
        print("   ---+---+---\n")
        valasz = None

def human_vs_human():

    while True:
        # X player
        while True:
            display_board()
            # horizontal winning condition
            for row in board:
                if row[0] ==  row[1] ==  row[2] !="." :
                    print("-" * 43)
                    print(' ' * 11 + f'The winner is the {row[1]}!' + ' ' * 11)
                    print("-" * 43)
                    print()
                    exit()

            # vertical winning condition        
            for col in range(3):
                if board[0][col] ==  board[1][col] == board[2][col] != "." :
                    print("-" * 43)
                    print(' ' * 11 + f'The winner is the {board[0][col]}!' + ' ' * 11)
                    print("-" * 43)
                    print()
                    exit()
            
            # diagonal winning condition
            if board[0][0] ==  board[1][1] == board[2][2] != "." or board[0][2] ==  board[1][1] == board[2][0] != ".":
                print("-" * 43)
                print(' ' * 11 + f'The winner is the {board[1][1]}!' + ' ' * 11)
                print("-" * 43)
                print()

            if "." not in board[0] and "." not in board[1] and "." not in board[2]:
                print("-" * 43)
                print(' ' * 15 + f'It is a tie!')
                print("-" * 43)
                print()
                exit()
            
            valasz = input('Choose a spot for "X" (a1, a2, etc.): ')
            
            match valasz:
                case "a1":
                        if board[0][0] != '.':
                            print()
                            print('-' * 43)
                            print('This has been chosen before, choose again.')
                            print('-' * 43)
                        else:
                            board[0][0] = 'X'
                            break
                case "a2":
                        if board[0][1] != '.':
                            print()
                            print('-' * 43)
                            print('This has been chosen before, choose again.')
                            print('-' * 43)
                        else:
                            board[0][1] = 'X'
                            break
                case "a3":
                        if board[0][2] != '.':
                            print()
                            print('-' * 43)
                            print('This has been chosen before, choose again.')
                            print('-' * 43)
                        else:
                            board[0][2] = 'X'
                            break

                case "b1":
                        if board[1][0] != '.':
                            print()
                            print('-' * 43)
                            print('This has been chosen before, choose again.')
                            print('-' * 43)
                        else:
                            board[1][0] = 'X'
                            break
                case "b2":
                        if board[1][1] != '.':
                            print()
                            print('-' * 43)
                            print('This has been chosen before, choose again.')
                            print('-' * 43)
                        else:
                            board[1][1] = 'X'
                            break
                case "b3":
                        if board[1][2] != '.':
                            print()
                            print('-' * 43)
                            print('This has been chosen before, choose again.')
                            print('-' * 43)
                        else:
                            board[1][2] = 'X'
                            break
                case "c1":
                        if board[2][0] != '.':
                            print()
                            print('-' * 43)
                            print('This has been chosen before, choose again.')
                            print('-' * 43)
                        else:
                            board[2][0] = 'X'
                            break
                case "c2":
                        if board[2][1] != '.':
                            print()
                            print('-' * 43)
                            print('This has been chosen before, choose again.')
                            print('-' * 43)
                        else:
                            board[2][1] = 'X'
                            break
                case "c3":
                        if board[2][2] != '.':
                            print()
                            print('-' * 43)
                            print('This has been chosen before, choose again.')
                            print('-' * 43)
                        else:
                            board[2][2] = 'X'
                            break
                case _:
                        print()
                        print('-' * 43)
                        print(' ' * 9 + 'Invalid input! Try again!')
                        print('-' * 43)

        # O player
        while True:
            display_board()
            # horizontal winning condition
            for row in board:
                if row[0] ==  row[1] ==  row[2] !="." :
                    print("-" * 43)
                    print(' ' * 11 + f'The winner is the {row[1]}!' + ' ' * 11)
                    print("-" * 43)
                    print()
                    exit()

            # vertical winning condition        
            for col in range(3):
                if board[0][col] ==  board[1][col] == board[2][col] != "." :
                    print("-" * 43)
                    print(' ' * 11 + f'The winner is the {board[0][col]}!' + ' ' * 11)
                    print("-" * 43)
                    print()
                    exit()
            
            # diagonal winning condition
            if board[0][0] ==  board[1][1] == board[2][2] != "." or board[0][2] ==  board[1][1] == board[2][0] != ".":
                print("-" * 43)
                print(' ' * 11 + f'The winner is the {board[1][1]}!' + ' ' * 11)
                print("-" * 43)
                print()

            if "." not in board[0] and "." not in board[1] and "." not in board[2]:
                print("-" * 43)
                print(' ' * 15 + f'It is a tie!')
                print("-" * 43)
                print()
                exit()
            
            valasz = input('Choose a spot for "O" (a1, a2, etc.): ')
            
            match valasz:
                case "a1":
                        if board[0][0] != '.':
                            print()
                            print('-' * 43)
                            print('This has been chosen before, choose again.')
                            print('-' * 43)
                        else:
                            board[0][0] = 'O'
                            break
                case "a2":
                        if board[0][1] != '.':
                            print()
                            print('-' * 43)
                            print('This has been chosen before, choose again.')
                            print('-' * 43)
                        else:
                            board[0][1] = 'O'
                            break
                case "a3":
                        if board[0][2] != '.':
                            print()
                            print('-' * 43)
                            print('This has been chosen before, choose again.')
                            print('-' * 43)
                        else:
                            board[0][2] = 'O'
                            break

                case "b1":
                        if board[1][0] != '.':
                            print()
                            print('-' * 43)
                            print('This has been chosen before, choose again.')
                            print('-' * 43)
                        else:
                            board[1][0] = 'O'
                            break
                case "b2":
                        if board[1][1] != '.':
                            print()
                            print('-' * 43)
                            print('This has been chosen before, choose again.')
                            print('-' * 43)
                        else:
                            board[1][1] = 'O'
                            break
                case "b3":
                        if board[1][2] != '.':
                            print()
                            print('-' * 43)
                            print('This has been chosen before, choose again.')
                            print('-' * 43)
                        else:
                            board[1][2] = 'O'
                            break
                case "c1":
                        if board[2][0] != '.':
                            print()
                            print('-' * 43)
                            print('This has been chosen before, choose again.')
                            print('-' * 43)
                        else:
                            board[2][0] = 'O'
                            break
                case "c2":
                        if board[2][1] != '.':
                            print()
                            print('-' * 43)
                            print('This has been chosen before, choose again.')
                            print('-' * 43)
                        else:
                            board[2][1] = 'O'
                            break
                case "c3":
                        if board[2][2] != '.':
                            print()
                            print('-' * 43)
                            print('This has been chosen before, choose again.')
                            print('-' * 43)
                        else:
                            board[2][2] = 'O'
                            break
                case _:
                        print()
                        print('-' * 43)
                        print('Invalid input, please write something, like "a1" or "c2"')
                        print('-' * 43)
    

while True:

    gamemode = input("\nChoose a gamemode!\n1: Human vs. Human\n2: Human vs. AI\n(1 or 2):")

    if gamemode == "1":
        human_vs_human()

    elif gamemode == "2":
        print("\nSadly, this gamemode hasn't been developed yet.")

    else:
        print("\nPlease choose from the available options.")