def displayPathtoPrincess(n, grid):
    possible_positions = [(0, 0), (0, n-1), (n-1, 0), (n-1, n-1)]
    p_coor = [(i, j) for i, j in possible_positions if grid[i][j] == 'p'][0]
    b_steps = n/2
    if p_coor[0] == 0:
        vert = 'UP'
    else:
        vert = 'DOWN'
    if p_coor[1] == 0:
        horiz = 'LEFT'
    else:
        horiz = 'RIGHT'
    moves = [vert for _ in range(b_steps)] + [horiz for _ in range(b_steps)]
    print '\n'.join(moves)


m = input()

grid = []
for i in xrange(0, m):
    grid.append(raw_input().strip())

displayPathtoPrincess(m, grid)
