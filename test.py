board = [
    [".", ".", "."],
    [".", ".", "."],
    [".", ".", "."]
    ]

def display_board():
        print("\n   1   2   3")
        print(f"A   {board[0][0]} | {board[0][1]} | {board[0][2]}")
        print("   ---+---+---") 
        print(f"B   {board[1][0]} | {board[1][1]} | {board[1][2]}")
        print("   ---+---+---")
        print(f"C   {board[2][0]} | {board[2][1]} | {board[2][2]}")
        print("   ---+---+---")
        valasz = None

while True:
    while True:
        display_board()
        for row in board:
            if row[0] ==  row[1] ==  row[2] !="." :
                print(f'Winner is player "{row[1]}"')
                exit()
                
        for col in range(3):
            if board[0][col] ==  board[1][col] == board[2][col] != "." :
                print(f'Winner is player "{board[0][col]}"')
                exit()
        valasz = input('\nValasz egy mezot (a1, a2, stb)')
        
        if board[0][col] ==  board[1][col] == board[2][col] != "." :
            print(f'Winner is player "{board[0][col]}"')
            exit()
            
        
        match valasz:
            case "a1":
                    if board[0][0] != '.':
                        print('This has been chosen before, choose again.')
                    else:
                        board[0][0] = 'X'
                        break
            case "a2":
                    if board[0][1] != '.':
                        print('This has been chosen before, choose again.')
                    else:
                        board[0][1] = 'X'
                        break
            case "a3":
                    if board[0][2] != '.':
                        print('This has been chosen before, choose again.')
                    else:
                        board[0][2] = 'X'
                        break

            case "b1":
                    if board[1][0] != '.':
                        print('This has been chosen before, choose again.')
                    else:
                        board[1][0] = 'X'
                        break
            case "b2":
                    if board[1][1] != '.':
                        print('This has been chosen before, choose again.')
                    else:
                        board[1][1] = 'X'
                        break
            case "b3":
                    if board[1][2] != '.':
                        print('This has been chosen before, choose again.')
                    else:
                        board[1][2] = 'X'
                        break
            case "c1":
                    if board[2][0] != '.':
                        print('This has been chosen before, choose again.')
                    else:
                        board[2][0] = 'X'
                        break
            case "c2":
                    if board[2][1] != '.':
                        print('This has been chosen before, choose again.')
                    else:
                        board[2][1] = 'X'
                        break
            case "c3":
                    if board[2][2] != '.':
                        print('This has been chosen before, choose again.')
                    else:
                        board[2][2] = 'X'
                        break
