from board import board
from board import check_for_winner
from board import display_board

def vs_human():

    while True:
        while True:

            check_for_winner()
            display_board()
            
            answer = input('Choose a spot for "X" (a1, a2, etc.): ')
            
            match answer:
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

        while True:

            check_for_winner()
            display_board()
                
            answer = input('Choose a spot for "O" (a1, a2, etc.): ')
                
            match answer:
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
                        print(' ' * 9 + 'Invalid input! Try again!')
                        print('-' * 43)