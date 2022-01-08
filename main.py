import pygame, sys
from pygame.locals import *

# Initialize program
pygame.init()

# Assign FPS a value
FPS = 30
FramePerSec = pygame.time.Clock()

# Setting up color objects
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Setup a 700 x 700 pixel display with caption
WIN_LENGTH = 700
WIN_HEIGHT = 700
DISPLAYSURF = pygame.display.set_mode((WIN_LENGTH,WIN_HEIGHT))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Raycasting...")

for i in range(0, WIN_LENGTH, WIN_HEIGHT//30):
    pygame.draw.line(DISPLAYSURF, BLACK, (i, 0), (i, WIN_HEIGHT))
for i in range(0, WIN_HEIGHT, WIN_HEIGHT//30):
    pygame.draw.line(DISPLAYSURF, BLACK, (0,i), (WIN_LENGTH, i))

# Beginning Game Loop
while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
  
    FramePerSec.tick(FPS)