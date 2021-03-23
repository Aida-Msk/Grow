#MY GAME
#Aida Meshkat

import pygame
import math
pygame.init()

WIDTH = 800
HEIGHT = 600
gameWindow = pygame.display.set_mode((WIDTH, HEIGHT))

BLACK = (0, 0, 0) 
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
WHITE = (255, 255, 255)
GREY = (128, 128, 128)
YELLOW = (255, 255, 100)
MAGENTA = (210, 0, 128)
DARKPURPLE = (128, 0, 128)

CENTREX = 400 #WIDTH // 2
CENTREY = 300 #HEIGHT // 2


objects = [[800, 10],[800, 100],[800, 200],[800, 150],[800, 500]]


while(True):
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    for i in range(len(objects)):
        objects[i][0] -=1
        pygame.draw.rect(gameWindow, RED, (objects[i][0], objects[i][1], +20, +20), 0)
    for i in range(len(objects)):
        if(objects[i][0] < -300):
            objects.pop(i)
    
    pygame.display.update()
    gameWindow.fill(WHITE)
    
    pygame.time.delay(10)

pygame.display.update()
