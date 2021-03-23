#MY GAME
#Aida Meshkat
import random
import pygame
import math
pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)

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

playerCounter = 1
playerX = 200
playerY = CENTREY
playerList = []
playerLength = 9
playerScore = 0
pointsPerFood = 5
movement = False
straight = False

for i in range(10):
    playerList.append([200-i*5, CENTREY])
    
foodsLength = 20
foodsHeight = 20

#List of food coordinations
foods = [[800, 10],[800, 100],[800, 200],[800, 150],[800, 500]]
badFoods = []


def displayPlayer():
    global playerY, playerCounter, movement, straight
    playerList[playerCounter][1] = playerList[playerCounter-1][1]
    
    if(playerCounter == len(playerList)-1):
        if(not movement):
            straight = False
        movement = False
        playerCounter = 1
    else:
        if(movement or straight):
            playerCounter += 1
    
    for i in range(0, len(playerList)):
        pygame.draw.rect(gameWindow, BLUE, (playerList[i][0], playerList[i][1] , +5, +10), 0)


def spawnObjects():
    global foods, badFoods, foodsHeight, HEIGHT
    #In every 10 random integers that are given, the only time the foods will spawn is when the number is 1.
    if(random.randint(0, 10) == 1):
        foods.append([800, random.randint(foodsHeight, HEIGHT-foodsHeight )])
    if(random.randint(0, 10) == 1):
        badFoods.append([800, random.randint(foodsHeight, HEIGHT-foodsHeight )])
        
def checkCollision():
    global playerList, playerLength, foods, badFoods, foodsLength, foodsHeight, playerScore, pointsPerFood
    global myfont, gameWindow, playerCounter
    
    remove = False
    for i in range (len(playerList)):
        foodToPop = None
        for j in range(len(foods)):
            if(playerList[i][0] >= foods[j][0] and playerList[i][0] <= foods[j][0] + foodsLength):
                if(playerList[i][1] >= foods[j][1] and playerList[i][1] <= foods[j][1] + foodsHeight):
                    playerScore += pointsPerFood
                    playerList.append([200-playerLength*5, playerList[0][-1]])
                    playerLength += 1
                    foodToPop = j
        if foodToPop != None:
            foods.pop(foodToPop)
        foodToPop = None
        for j in range(len(badFoods)):
            if(playerList[i][0] >= badFoods[j][0] and playerList[i][0] <= badFoods[j][0] + foodsLength):
                if(playerList[i][1] >= badFoods[j][1] and playerList[i][1] <= badFoods[j][1] + foodsHeight):
                    foodToPop = j
                    remove = True            
        if foodToPop != None:
            badFoods.pop(foodToPop)
    if remove:
        if(playerLength > 8):
            playerList = playerList[0:len(playerList)-8]
            playerLength -= 8
            playerCounter = 0
            movement = True
        else:
             
            textsurface = myfont.render('GAME OVER :(', False, (0, 0, 0))
            gameWindow.blit(textsurface,(CENTREX-100,CENTREY-100))      
            pygame.display.update()
            pygame.time.delay(10000)
            pygame.quit()
            exit()  
    remove = False
    
def updateLocations():
    i = 0
    while (i < len(foods)):
        if(foods[i][0] < -300):
            foods.pop(i)
            i -= 1
        i+=1
    while (i < len(badFoods)):
        if(badFoods[i][0] < -300):
            badFoods.pop(i)
            i -= 1
        i+=1
   
def drawObjects():
    for i in range(len(badFoods)):
        badFoods[i][0] -=1
        pygame.draw.rect(gameWindow, RED, (badFoods[i][0], badFoods[i][1], +20, +20), 0)
    for i in range(len(foods)):
        foods[i][0] -=1
        pygame.draw.rect(gameWindow, GREEN, (foods[i][0], foods[i][1], +20, +20), 0)

def displayScore():
    global myfont, gameWindow
    textsurface = myfont.render('Score: ' + str(playerScore), False, (0, 0, 0))
    gameWindow.blit(textsurface,(0,0))

    
while(True):
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                movement = True
                straight = True 
                playerList[0][1] -= 5
            if event.key == pygame.K_DOWN:
                movement = True
                straight = True 
                playerList[0][1] += 5
        
    updateLocations()
    drawObjects()
    displayPlayer()
    checkCollision()
    spawnObjects()
    displayScore()
    
    pygame.display.update()
    gameWindow.fill(WHITE)
    pygame.time.delay(15)
