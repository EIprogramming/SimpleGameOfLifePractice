import copy
import time

def main():
    main_grid = generate_main_grid(3,3)
    print_grid(main_grid)
    input("")
    while True:
        print("\033c", end='')
        time.sleep(0.6)
        main_grid = iterate(main_grid)
        print_grid(main_grid)

def generate_main_grid(x: int, y: int):
    #return [[0 for j in range(x)] for i in range(y)]
    return [[0, 0, 0, 0, 0,  0, 0, 0, 0, 0,  0, 0, 0, 0, 0,  0, 0], # 1
            [0, 0, 0, 0, 0,  0, 0, 0, 0, 0,  0, 0, 0, 0, 0,  0, 0], # 2
            [0, 0, 0, 0, 1,  1, 1, 0, 0, 0,  1, 1, 1, 0, 0,  0, 0], # 3
            [0, 0, 0, 0, 0,  0, 0, 0, 0, 0,  0, 0, 0, 0, 0,  0, 0], # 4
            [0, 0, 1, 0, 0,  0, 0, 1, 0, 1,  0, 0, 0, 0, 1,  0, 0], # 5
            [0, 0, 1, 0, 0,  0, 0, 1, 0, 1,  0, 0, 0, 0, 1,  0, 0], # 6
            [0, 0, 1, 0, 0,  0, 0, 1, 0, 1,  0, 0, 0, 0, 1,  0, 0], # 7
            [0, 0, 0, 0, 1,  1, 1, 0, 0, 0,  1, 1, 1, 0, 0,  0, 0], # 8
            [0, 0, 0, 0, 0,  0, 0, 0, 0, 0,  0, 0, 0, 0, 0,  0, 0], # 9
            [0, 0, 0, 0, 1,  1, 1, 0, 0, 0,  1, 1, 1, 0, 0,  0, 0], # 10
            [0, 0, 1, 0, 0,  0, 0, 1, 0, 1,  0, 0, 0, 0, 1,  0, 0], # 11
            [0, 0, 1, 0, 0,  0, 0, 1, 0, 1,  0, 0, 0, 0, 1,  0, 0], # 12
            [0, 0, 1, 0, 0,  0, 0, 1, 0, 1,  0, 0, 0, 0, 1,  0, 0], # 13
            [0, 0, 0, 0, 0,  0, 0, 0, 0, 0,  0, 0, 0, 0, 0,  0, 0], # 14
            [0, 0, 0, 0, 1,  1, 1, 0, 0, 0,  1, 1, 1, 0, 0,  0, 0], # 15
            [0, 0, 0, 0, 0,  0, 0, 0, 0, 0,  0, 0, 0, 0, 0,  0, 0], # 16
            [0, 0, 0, 0, 0,  0, 0, 0, 0, 0,  0, 0, 0, 0, 0,  0, 0], # 17
            ]

def print_grid(grid: list):
    for i in grid:
        for j in i:
            if j == 1:
                print("■", end=" ")
            elif j == 0:
                #print("□", end=" ") # for editing/gameplay
                print(" ", end=" ") # for display
            elif j == -1:
                print(" ", end =" ")
        print("")
    print("--"*len(grid[0]))

def search_grid_neighbours(grid, x_pos, y_pos, live_requested):
    n_grid = [[0, 0, 0],
              [0, 0, 0],
              [0, 0, 0]]
    live = 0 # counts live neighbours
    for j in range(len(n_grid)): # y traversal
        for i in range(len(n_grid[j])): # x traversal
            grid_y = y_pos - 1 + j
            grid_x = x_pos - 1 + i
            if (grid_y < 0 or grid_x < 0) or grid_y >= len(grid) or grid_x >= len(grid[0]):
                n_grid[j][i] = -1
            else:
                n_grid[j][i]=grid[grid_y][grid_x]
                if (i != 1 or j != 1): # prevents counting itself
                    live += n_grid[j][i] # adds the number of live cells to the live count
                    if (n_grid[j][i]==1):
                        True
    if live_requested: # could be separated into two functions later?
        return live
    else:
        return n_grid

def iterate(grid):
    # Any live cell with less than two neighbours dies:
    # Any live cell with two or three neighbours survives:
    # Any live cell with more than three neighbours dies:
    # Any dead cell with exactly three neighbours becomes a live cell:
    new_grid = copy.deepcopy(grid)
    for j in range(len(grid)):
        for i in range(len(grid[j])):
            live = search_grid_neighbours(grid, i, j, True)
            if live < 2 or live > 3:
                new_grid[j][i] = 0 # death by over/underpopulation
            elif live == 3:
                new_grid[j][i] = 1 # birth
    return new_grid

if __name__ == "__main__":
    main()
