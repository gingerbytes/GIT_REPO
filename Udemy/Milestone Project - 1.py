# Tic Tac Toe Game

import os

usrInput = ''
startgame = True
turn = 'X'
board = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
slot = '123456789'


def dispboard(message):
    # clears screen then displays the udpated board.
    os.system('cls')
    print(*board, sep='\n')
    print(message)


def iswinner(move):
    pattern1, pattern2, pattern3, pattern4 = "", "", "", ""

    for x in range(len(board)):
        for y in range(len(board)):
            pattern1 += board[x][y]  # check vertical pattern
            pattern2 += board[y][x]  # check horizontal pattern

        # check diagonal pattern
        pattern3 += board[x][x]  # backslash
        pattern4 += board[len(board) - x - 1][x]  # slash

        if move*3 in [pattern1, pattern2, pattern3, pattern4]:
            dispboard(f'\nCONGRATULATIONS "{move}" WINS!!!\n')
            return False

        pattern1, pattern2 = "", ""
    return True


while startgame:
    dispboard('')
    usrInput = input(
        f'"{turn}" turn.  Make your move, please choose a number ({slot}): ')
    if not usrInput in slot:
        continue

    a, b = 0, 0

    # get the usrInput index from board list as a and b.
    for item in board:
        if usrInput in item:
            b = item.index(usrInput)
            break
        a += 1

    board[a][b] = turn
    startgame = iswinner(turn)

    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'

    # Delete chosen slot, show remaining slot to choose from.
    slot = slot.replace(usrInput, '')
    if len(slot) == 0:
        dispboard('\nIt\'s a DRAW!')
        break
