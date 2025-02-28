import pygame
import time
import game_of_life as gol

# CONSTS #
WINDOW_X = 960
WINDOW_Y = 540

BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)
LIGHT_BLUE = pygame.Color(204, 224, 255)
DARK_BLUE = pygame.Color(85, 107, 140)
EDGE_COLOR = DARK_BLUE
BACKGROUND = LIGHT_BLUE

def main():
    # INIT #
    x_size, y_size = None, None
    pixel_size = 20
    while type(x_size) != int or type(y_size) != int:
        try:
            x_size = int(input("x size of grid: "))
            y_size = int(input("y size of grid: "))
        except:
            print("Return a valid integer input.")

    main_grid = gol.generate_main_grid(x_size, y_size)
    # ensures that x_size and y_size correspond to size of main_grid, even if parent function returns a default grid
    x_size, y_size = len(main_grid[0]), len(main_grid)
    pygame.init()
    pygame.display.set_caption('Game of Life')
    game_window = pygame.display.set_mode((WINDOW_X, WINDOW_Y))
    game_window.fill(BACKGROUND)

    sim_started = False
    
    while True:
        # centers x, y
        start_x = WINDOW_X/2-x_size*pixel_size/2
        start_y = WINDOW_Y/2-y_size*pixel_size/2
        x, y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and not sim_started:
                    try:
                        x, y = pygame.mouse.get_pos()
                        x -= start_x
                        y -= start_y
                        if (main_grid[int(y/pixel_size)][int(x/pixel_size)] == 1):
                            main_grid[int(y/pixel_size)][int(x/pixel_size)] = 0
                        else:
                            main_grid[int(y/pixel_size)][int(x/pixel_size)] = 1
                    except:
                        pass
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and not sim_started:
                    sim_started = True
                elif event.key == pygame.K_RETURN and sim_started:
                    sim_started = False
            if event.type == pygame.QUIT:
                pygame.quit()
                # sys.exit()
        pygame.draw.rect(game_window, EDGE_COLOR, pygame.Rect(start_x,start_y,pixel_size*x_size,pixel_size*y_size))
        for i in range(len(main_grid)):
            for j in range(len(main_grid[i])):
                if main_grid[i][j] == 1:
                    #print("■", end=" ")
                    pygame.draw.rect(game_window, EDGE_COLOR, pygame.Rect(start_x+pixel_size*j, start_y+pixel_size*i, pixel_size, pixel_size))
                elif main_grid[i][j] == 0:
                    #print("□", end=" ") # for editing/gameplay
                    #print(" ", end=" ") # for display
                    pygame.draw.rect(game_window, EDGE_COLOR, pygame.Rect(start_x+pixel_size*j, start_y+pixel_size*i, pixel_size, pixel_size))
                    pygame.draw.rect(game_window, BACKGROUND, pygame.Rect(start_x+pixel_size*j+1, start_y+pixel_size*i+1, 18, 18))
        
        if (sim_started):
            main_grid = gol.iterate(main_grid)
            time.sleep(0.2)
        
        pygame.display.update() # Refresh game screen

if __name__ == "__main__":
    main()
