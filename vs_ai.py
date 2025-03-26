import random

from board import board
from board import check_for_winner
from board import display_board

def vs_ai():

    all_possible_moves = ["a1", "a2", "a3", "b1", "b2", "b3", "c1", "c2", "c3"]
    player_moves = []
    ai_moves = []
    is_first_turn = True

    while True:

        while True:

            check_for_winner()

            move_done = False

            if is_first_turn == False:

                if len(ai_moves) != len(player_moves):
                    
                    # check if can win

                    # horizontal
                    if "a1" in all_possible_moves and "a2" in ai_moves and "a3" in ai_moves:
                        board[0][0] = "O"
                        all_possible_moves.remove("a1")
                        move_done = True
                    elif "a1" in ai_moves and "a2" in all_possible_moves and "a3" in ai_moves:
                        board[0][1] = "O"
                        all_possible_moves.remove("a2")
                        move_done = True
                    elif "a1" in ai_moves and "a2" in ai_moves and "a3" in all_possible_moves:
                        board[0][2] = "O"
                        all_possible_moves.remove("a3")
                        move_done = True

                    elif "b1" in all_possible_moves and "b2" in ai_moves and "b3" in ai_moves:
                        board[1][0] = "O"
                        all_possible_moves.remove("b1")
                        move_done = True
                    elif "b1" in ai_moves and "b2" in all_possible_moves and "b3" in ai_moves:
                        board[1][1] = "O"
                        all_possible_moves.remove("b2")
                        move_done = True
                    elif "b1" in ai_moves and "a2" in ai_moves and "b3" in all_possible_moves:
                        board[1][2] = "O"
                        all_possible_moves.remove("b3")
                        move_done = True

                    elif "c1" in all_possible_moves and "c2" in ai_moves and "c3" in ai_moves:
                        board[2][0] = "O"
                        all_possible_moves.remove("c1")
                        move_done = True
                    elif "c1" in ai_moves and "c2" in all_possible_moves and "c3" in ai_moves:
                        board[2][1] = "O"
                        all_possible_moves.remove("c2")
                        move_done = True
                    elif "c1" in ai_moves and "c2" in ai_moves and "c3" in all_possible_moves:
                        board[2][2] = "O"
                        all_possible_moves.remove("c3")
                        move_done = True




                    # vertical
                    elif "a1" in all_possible_moves and "b1" in ai_moves and "c1" in ai_moves:
                        board[0][0] = "O"
                        all_possible_moves.remove("a1")
                        move_done = True
                    elif "a1" in ai_moves and "b1" in all_possible_moves and "c1" in ai_moves:
                        board[1][0] = "O"
                        all_possible_moves.remove("b1")
                        move_done = True
                    elif "a1" in ai_moves and "b1" in ai_moves and "c1" in all_possible_moves:
                        board[2][0] = "O"
                        all_possible_moves.remove("c1")
                        move_done = True

                    elif "a2" in all_possible_moves and "b2" in ai_moves and "c2" in ai_moves:
                        board[0][1] = "O"
                        all_possible_moves.remove("a2")
                        move_done = True
                    elif "a2" in ai_moves and "b2" in all_possible_moves and "c2" in ai_moves:
                        board[1][1] = "O"
                        all_possible_moves.remove("b2")
                        move_done = True
                    elif "a2" in ai_moves and "b2" in ai_moves and "c2" in all_possible_moves:
                        board[2][1] = "O"
                        all_possible_moves.remove("c2")
                        move_done = True

                    elif "a3" in all_possible_moves and "b3" in ai_moves and "c3" in ai_moves:
                        board[0][2] = "O"
                        all_possible_moves.remove("a3")
                        move_done = True
                    elif "a3" in ai_moves and "b3" in all_possible_moves and "c3" in ai_moves:
                        board[1][2] = "O"
                        all_possible_moves.remove("b3")
                        move_done = True
                    elif "a3" in ai_moves and "b3" in ai_moves and "c3" in all_possible_moves:
                        board[2][2] = "O"
                        all_possible_moves.remove("c3")
                        move_done = True




                    # diagonal
                    elif "a1" in all_possible_moves and "b2" in ai_moves and "c3" in ai_moves:
                        board[0][0] = "O"
                        all_possible_moves.remove("a1")
                        move_done = True
                    elif "a1" in ai_moves and "b2" in all_possible_moves and "c3" in ai_moves:
                        board[1][1] = "O"
                        all_possible_moves.remove("b2")
                        move_done = True
                    elif "a1" in ai_moves and "b2" in ai_moves and "c3" in all_possible_moves:
                        board[2][2] = "O"
                        all_possible_moves.remove("c3")
                        move_done = True

                    elif "a3" in all_possible_moves and "b2" in ai_moves and "c1" in ai_moves:
                        board[0][2] = "O"
                        all_possible_moves.remove("a3")
                        move_done = True
                    elif "a3" in ai_moves and "b2" in all_possible_moves and "c1" in ai_moves:
                        board[1][1] = "O"
                        all_possible_moves.remove("b2")
                        move_done = True
                    elif "a3" in ai_moves and "b2" in ai_moves and "c1" in all_possible_moves:
                        board[2][0] = "O"
                        all_possible_moves.remove("c1")
                        move_done = True

                    check_for_winner()

                    # check if player can win


                    # horizontal
                    if "a1" in all_possible_moves and "a2" in player_moves and "a3" in player_moves:
                        board[0][0] = "O"
                        all_possible_moves.remove("a1")
                        ai_moves.append("a1")
                        move_done = True
                    elif "a1" in player_moves and "a2" in all_possible_moves and "a3" in player_moves:
                        board[0][1] = "O"
                        all_possible_moves.remove("a2")
                        ai_moves.append("a2")
                        move_done = True
                    elif "a1" in player_moves and "a2" in player_moves and "a3" in all_possible_moves:
                        board[0][2] = "O"
                        all_possible_moves.remove("a3")
                        ai_moves.append("a3")
                        move_done = True

                    elif "b1" in all_possible_moves and "b2" in player_moves and "b3" in player_moves:
                        board[1][0] = "O"
                        all_possible_moves.remove("b1")
                        ai_moves.append("b1")
                        move_done = True
                    elif "b1" in player_moves and "b2" in all_possible_moves and "b3" in player_moves:
                        board[1][1] = "O"
                        all_possible_moves.remove("b2")
                        ai_moves.append("b2")
                        move_done = True
                    elif "b1" in player_moves and "a2" in player_moves and "b3" in all_possible_moves:
                        board[1][2] = "O"
                        all_possible_moves.remove("b3")
                        ai_moves.append("b3")
                        move_done = True

                    elif "c1" in all_possible_moves and "c2" in player_moves and "c3" in player_moves:
                        board[2][0] = "O"
                        all_possible_moves.remove("c1")
                        ai_moves.append("c1")
                        move_done = True
                    elif "c1" in player_moves and "c2" in all_possible_moves and "c3" in player_moves:
                        board[2][1] = "O"
                        all_possible_moves.remove("c2")
                        ai_moves.append("c2")
                        move_done = True
                    elif "c1" in player_moves and "c2" in player_moves and "c3" in all_possible_moves:
                        board[2][2] = "O"
                        all_possible_moves.remove("c3")
                        ai_moves.append("c3")
                        move_done = True




                    # vertical
                    elif "a1" in all_possible_moves and "b1" in player_moves and "c1" in player_moves:
                        board[0][0] = "O"
                        all_possible_moves.remove("a1")
                        ai_moves.append("a1")
                        move_done = True
                    elif "a1" in player_moves and "b1" in all_possible_moves and "c1" in player_moves:
                        board[1][0] = "O"
                        all_possible_moves.remove("b1")
                        ai_moves.append("b1")
                        move_done = True
                    elif "a1" in player_moves and "b1" in player_moves and "c1" in all_possible_moves:
                        board[2][0] = "O"
                        all_possible_moves.remove("c1")
                        ai_moves.append("c1")
                        move_done = True

                    elif "a2" in all_possible_moves and "b2" in player_moves and "c2" in player_moves:
                        board[0][1] = "O"
                        all_possible_moves.remove("a2")
                        ai_moves.append("a2")
                        move_done = True
                    elif "a2" in player_moves and "b2" in all_possible_moves and "c2" in player_moves:
                        board[1][1] = "O"
                        all_possible_moves.remove("b2")
                        ai_moves.append("b2")
                        move_done = True
                    elif "a2" in player_moves and "b2" in player_moves and "c2" in all_possible_moves:
                        board[2][1] = "O"
                        all_possible_moves.remove("c2")
                        ai_moves.append("c2")
                        move_done = True

                    elif "a3" in all_possible_moves and "b3" in player_moves and "c3" in player_moves:
                        board[0][2] = "O"
                        all_possible_moves.remove("a3")
                        ai_moves.append("a3")
                        move_done = True
                    elif "a3" in player_moves and "b3" in all_possible_moves and "c3" in player_moves:
                        board[1][2] = "O"
                        all_possible_moves.remove("b3")
                        ai_moves.append("b3")
                        move_done = True
                    elif "a3" in player_moves and "b3" in player_moves and "c3" in all_possible_moves:
                        board[2][2] = "O"
                        all_possible_moves.remove("c3")
                        ai_moves.append("c3")
                        move_done = True




                    # diagonal
                    elif "a1" in all_possible_moves and "b2" in player_moves and "c3" in player_moves:
                        board[0][0] = "O"
                        all_possible_moves.remove("a1")
                        ai_moves.append("a1")
                        move_done = True
                    elif "a1" in player_moves and "b2" in all_possible_moves and "c3" in player_moves:
                        board[1][1] = "O"
                        all_possible_moves.remove("b2")
                        ai_moves.append("b2")
                        move_done = True
                    elif "a1" in player_moves and "b2" in player_moves and "c3" in all_possible_moves:
                        board[2][2] = "O"
                        all_possible_moves.remove("c3")
                        ai_moves.append("c3")
                        move_done = True

                    elif "a3" in all_possible_moves and "b2" in player_moves and "c1" in player_moves:
                        board[0][2] = "O"
                        all_possible_moves.remove("a3")
                        ai_moves.append("a3")
                        move_done = True
                    elif "a3" in player_moves and "b2" in all_possible_moves and "c1" in player_moves:
                        board[1][1] = "O"
                        all_possible_moves.remove("b2")
                        ai_moves.append("b2")
                        move_done = True
                    elif "a3" in player_moves and "b2" in player_moves and "c1" in all_possible_moves:
                        board[2][0] = "O"
                        all_possible_moves.remove("c1")
                        ai_moves.append("c1")
                        move_done = True




                    if move_done == False:
                        if len(all_possible_moves) == 0:
                            check_for_winner()
                        else:
                            roll = random.randint(0, len(all_possible_moves) - 1)
                            ai_moves.append(all_possible_moves[roll])

                            if all_possible_moves[roll] == "a1":
                                board[0][0] = "O"
                            if all_possible_moves[roll] == "a2":
                                board[0][1] = "O"
                            if all_possible_moves[roll] == "a3":
                                board[0][2] = "O"
                            if all_possible_moves[roll] == "b1":
                                board[1][0] = "O"
                            if all_possible_moves[roll] == "b2":
                                board[1][1] = "O"
                            if all_possible_moves[roll] == "b3":
                                board[1][2] = "O"
                            if all_possible_moves[roll] == "c1":
                                board[2][0] = "O"
                            if all_possible_moves[roll] == "c2":
                                board[2][1] = "O"
                            if all_possible_moves[roll] == "c3":
                                board[2][2] = "O"
                                
                            all_possible_moves.pop(roll)

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
                            player_moves.append(answer)
                            all_possible_moves.remove("a1")
                            board[0][0] = 'X'
                            is_first_turn = False
                            break
                case "a2":
                        if board[0][1] != '.':
                            print()
                            print('-' * 43)
                            print('This has been chosen before, choose again.')
                            print('-' * 43)
                        else:
                            board[0][1] = 'X'
                            player_moves.append(answer)
                            all_possible_moves.remove("a2")
                            is_first_turn = False
                            break
                case "a3":
                        if board[0][2] != '.':
                            print()
                            print('-' * 43)
                            print('This has been chosen before, choose again.')
                            print('-' * 43)
                        else:
                            board[0][2] = 'X'
                            player_moves.append(answer)
                            all_possible_moves.remove("a3")
                            is_first_turn = False
                            break

                case "b1":
                        if board[1][0] != '.':
                            print()
                            print('-' * 43)
                            print('This has been chosen before, choose again.')
                            print('-' * 43)
                        else:
                            board[1][0] = 'X'
                            player_moves.append(answer)
                            all_possible_moves.remove("b1")
                            is_first_turn = False
                            break
                case "b2":
                        if board[1][1] != '.':
                            print()
                            print('-' * 43)
                            print('This has been chosen before, choose again.')
                            print('-' * 43)
                        else:
                            board[1][1] = 'X'
                            player_moves.append(answer)
                            all_possible_moves.remove("b2")
                            is_first_turn = False
                            break
                case "b3":
                        if board[1][2] != '.':
                            print()
                            print('-' * 43)
                            print('This has been chosen before, choose again.')
                            print('-' * 43)
                        else:
                            board[1][2] = 'X'
                            player_moves.append(answer)
                            all_possible_moves.remove("b3")
                            is_first_turn = False
                            break
                case "c1":
                        if board[2][0] != '.':
                            print()
                            print('-' * 43)
                            print('This has been chosen before, choose again.')
                            print('-' * 43)
                        else:
                            board[2][0] = 'X'
                            player_moves.append(answer)
                            all_possible_moves.remove("c1")
                            is_first_turn = False
                            break
                case "c2":
                        if board[2][1] != '.':
                            print()
                            print('-' * 43)
                            print('This has been chosen before, choose again.')
                            print('-' * 43)
                        else:
                            board[2][1] = 'X'
                            player_moves.append(answer)
                            all_possible_moves.remove("c2")
                            is_first_turn = False
                            break
                case "c3":
                        if board[2][2] != '.':
                            print()
                            print('-' * 43)
                            print('This has been chosen before, choose again.')
                            print('-' * 43)
                        else:
                            board[2][2] = 'X'
                            player_moves.append(answer)
                            all_possible_moves.remove("c3")
                            is_first_turn = False
                            break
                case _:
                        print()
                        print('-' * 43)
                        print(' ' * 9 + 'Invalid input! Try again!')
                        print('-' * 43)