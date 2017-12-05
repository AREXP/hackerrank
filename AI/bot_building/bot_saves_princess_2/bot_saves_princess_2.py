#!/bin/python
def nextMove(n, r, c, grid):
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 'p':
                p_coor = (i, j)
                break
    if p_coor[0] < r:
        move = 'UP'
    elif p_coor[0] > r:
        move = 'DOWN'
    elif p_coor[1] < c:
        move = 'LEFT'
    else:
        move = 'RIGHT'
    return move


n = input()
r, c = [int(i) for i in raw_input().strip().split()]
grid = []
for i in xrange(0, n):
    grid.append(raw_input())

print nextMove(n, r, c, grid)
