#!/usr/bin/python
import random
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

    if dirty:
        next_to_go = min(dirty.iterkeys(), key=lambda k: dirty[k])
    else:
        corners = [(1, 1), (1, n-2), (n-2, n-2), (n-2, 1)]
        path_to_corners = sorted([
            (abs(posr - i) + abs(posc-j), (i, j))
            for (i, j) in corners
        ])
        if path_to_corners[0][0] == 0:
            now_corner = path_to_corners[0][1]
            next_corner_idx = corners.index(now_corner)
            if next_corner_idx == len(corners) - 1:
                next_to_go = corners[0]
            else:
                next_to_go = corners[next_corner_idx+1]
        else:
            min_path = min([path for path, coor in path_to_corners])
            close_corners = [
                coor for path, coor in path_to_corners
                if path == min_path
            ]

            if len(close_corners) == len(corners):
                next_to_go = corners[0]
            elif len(close_corners) == 2:
                idx_1 = corners.index(close_corners[0])
                idx_2 = corners.index(close_corners[1])
                if sorted((idx_1, idx_2)) == [0, 3]:
                    next_to_go = corners[0]
                else:
                    next_to_go = corners[max(idx_1, idx_2)]
            else:
                next_to_go = close_corners[0]

    if next_to_go[0] < posr:
        move = 'UP'
    elif next_to_go[0] > posr:
        move = 'DOWN'
    elif next_to_go[1] < posc:
        move = 'LEFT'
    else:
        move = 'RIGHT'
    print move


if __name__ == "__main__":
    pos = [int(i) for i in raw_input().strip().split()]
    board = [[j for j in raw_input().strip()] for i in range(5)]
    next_move(pos[0], pos[1], board)
