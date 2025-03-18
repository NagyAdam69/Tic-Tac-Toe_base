board = [
    [".", ".", "."],
    [".", ".", "."],
    [".", ".", "."]
    ]

while True:
    valasz = input('Valasz egy mezot (a1, a2, stb)')

    match valasz:
        case "a1"  :
            if board[0][0] == 'X':
                raise ValueError('This has been chosen before, choose again')
            else:
                board[0][0] = 'X'

        case "a2":
            if board[0][1] == 'X':
                raise ValueError('This has been chosen before, choose again')
            else:
                board[0][1] = 'X'

        case "a3":
            board[0][2] = 'X'

        case "b1":
            board[1][0] = 'X'

        case "b2":
            board[1][1] = 'X'

        case "b3":
            board[1][2] = 'X'

        case "c1":
            board[2][0] = 'X'

        case "c2":
            board[2][1] = 'X'

        case "c3":
            board[2][2] = 'X'
            
    print("   1   2   3")
    print(f"A   {board[0][0]} | {board[0][1]} | {board[0][2]}")
    print("   ---+---+---") 
    print(f"B   {board[1][0]} | {board[1][1]} | {board[1][2]}")
    print("   ---+---+---")
    print(f"C   {board[2][0]} | {board[2][1]} | {board[2][2]}")
    print("   ---+---+---")
    valasz = None


    for row in board:
        if row[0] ==  row[1] ==  row[2] :
            print(f"Winner is {row[1]}")
            exit()
            
    for i in board:
        column = 0
        if board[0][column] == "X" and board[1][column] == "X" and board[2][column] == "X":
            print("Winner is X")
            exit()
        elif board[0][column] == "O" and board[1][column] == "O" and board[2][column] == "O":
            print("Winner is O")
            exit()
        column += 1


