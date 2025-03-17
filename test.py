board = [
    [".", ".", "."],
    [".", ".", "."],
    [".", ".", "."],
    [".", ".", "."], 
    ]
valasz = input('Valasz egy mezot (a1, a2, stb)')

match valasz:
    case "a1":
        board[0][0] = 'X'

    case "a2":
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

