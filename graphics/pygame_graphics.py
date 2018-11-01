import pygame as pg

white = (255, 255, 255)
light_grey = (150, 150, 150)
dark_grey = (70, 70, 70)
black = (0, 0, 0)


class PygameGraphics:

    def __init__(self, x, y, snake_number, food_number, border_number
                 , resolution=(480, 480), framerate=5):
        pg.init()
        self.x = x
        self.y = y
        self.snake_numb = snake_number
        self.food_numb = food_number
        self.border_numb = border_number
        self.size_x = resolution[0] // x
        self.size_y = resolution[1] // y
        self.resolution = resolution
        self.framerate = framerate

        pg.display.set_caption("Neural_Snake")
        self.game_display = pg.display.set_mode(self.resolution)
        self.clock = pg.time.Clock()

    def display_frame(self, game_matrix):
        for i in range(self.x):
            for j in range(self.y):
                if game_matrix[i][j] == 0:
                    pg.draw.rect(self.game_display, white, [i * self.size_x, j * self.size_y, self.size_x, self.size_y])
                elif game_matrix[i][j] == self.border_numb:
                    pg.draw.rect(self.game_display, black, [i * self.size_x, j * self.size_y, self.size_x, self.size_y])
                elif game_matrix[i][j] == self.snake_numb:
                    pg.draw.rect(self.game_display, light_grey, [i * self.size_x, j * self.size_y, self.size_x, self.size_y])
                elif game_matrix[i][j] == self.food_numb:
                    pg.draw.rect(self.game_display, dark_grey, [i * self.size_x, j * self.size_y, self.size_x, self.size_y])

        pg.event.get()
        pg.display.update()
        self.clock.tick(self.framerate)

    def read_input(self, previous):
        for events in pg.event.get():
            if events.type == pg.KEYDOWN:
                if events.key == pg.K_w:
                    return 3
                elif events.key == pg.K_d:
                    return 0
                elif events.key == pg.K_s:
                    return 1
                elif events.key == pg.K_a:
                    return 2
            elif events.type == pg.QUIT:
                self.quit_game()
        return previous

    def quit_game(self):
        pg.quit()
        quit()
