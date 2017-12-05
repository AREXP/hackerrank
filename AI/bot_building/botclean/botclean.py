#!/usr/bin/python
def next_move(posr, posc, board):
    if board[posr][posc] == 'd':
        print 'CLEAN'
        return
    dirty = {}
    n = len(board)
    for i in range(n):
        for j in range(n):
            if board[i][j] == 'd':
                dirty[(i, j)] = abs(posr - i) + abs(posc - j)

    next_to_clean = min(dirty.iterkeys(), key=lambda k: dirty[k])
    if next_to_clean[0] < posr:
        move = 'UP'
    elif next_to_clean[0] > posr:
        move = 'DOWN'
    elif next_to_clean[1] < posc:
        move = 'LEFT'
    else:
        move = 'RIGHT'
    print move


if __name__ == "__main__":
    pos = [int(i) for i in raw_input().strip().split()]
    board = [[j for j in raw_input().strip()] for i in range(5)]
    next_move(pos[0], pos[1], board)
