import pygame

surface = pygame.display.set_mode((650, 650))

#Colors
WHITE = (255,255,255)
BLACK = (0, 0, 0)
RED = (222, 49, 99)
PURPLE = (106, 15, 142)
BLUE = (49, 172, 222)
ORANGE = (255, 154, 118)
DARK_BLUE = (51, 54, 255)

#Temp variables
x0 = 0
y0 = 0
x1 = 20
y1 = 20
spacing = 5
y = 0
n = 20

class Square:
    def __init__(self, x, y, col, row, width):
        self.x = x
        self.y = y
        self.col = col
        self.row = row
        self.width = width
        self.color = WHITE
    def draw(self):
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.width, self.width))

    def start_point(self):
        self.color = RED
    
    def end_point(self):
        self.color = PURPLE

    def create_barrier(self):
        self.color = BLACK
        
    def visited_cell(self):
        self.color = DARK_BLUE

    def backtrack(self):
        self.color = ORANGE

    def edge_color(self):
        self.color = BLUE

    def reset(self):
        self.color = WHITE

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y
    
    def get_row(self):
        return self.row

    def get_col(self):
        return self.col

    def get_width(self):
        return self.width
