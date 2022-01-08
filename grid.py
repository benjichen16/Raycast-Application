import pygame, sys, math
from square import Square

LENGTH = 650
GRIDSIZE = 50
GAPWIDTH = 12

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
n = 0

pygame.init()
surface = pygame.display.set_mode((LENGTH, LENGTH))
surface.fill(WHITE)
pygame.display.set_caption('Pathfinding Algorithm Visualizer')

class Grid:
    def __init__(self):
        self.gamegrid = []
        n = GAPWIDTH
        for i in range(1, GRIDSIZE+1):
            gap = GAPWIDTH
            self.gamegrid.append([])
            for j in range(1, GRIDSIZE+1):
                s = Square(x0, y0, math.trunc(x0/13), math.trunc(y0/13), 12)
                x0 = gap + j
                gap = gap + GAPWIDTH
                self.gamegrid.append(s)
            y0 = n + i
            n = n + GAPWIDTH


        
def run():
    for i in range(0, LENGTH, LENGTH//30):
        pygame.draw.line(surface, BLACK, (i, 0), (i, LENGTH))
    for i in range(0, LENGTH, LENGTH//30):
        pygame.draw.line(surface, BLACK, (0,i), (LENGTH, i))
        
    while True:
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()


    