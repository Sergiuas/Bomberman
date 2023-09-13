import pygame
import random
import math

# Initialize the pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((800,600))

#Background
background = pygame.image.load('background.png')

#Title and Icon
pygame.display.set_caption("Bomberman")
icon = pygame.image.load('bomberman.png')
pygame.display.set_icon(icon)

#blocks
barrel = pygame.image.load('barrel.png')
barrel = pygame.transform.scale(barrel, (45,45))
stone = pygame.image.load('stone.png')
stone = pygame.transform.scale(stone , (45,45))

#Back matrix
matrix = [[2, 2, 2, 2, 2, 2, 2 ,2 , 2, 2, 2, 2, 2],
        [2, 0, 0, 0, 0, 0, 0 ,0 ,0 , 0, 0, 0, 2],
        [2, 0, 2, 0, 2, 0, 2 ,0 , 2, 0, 2, 0, 2],
        [2, 0, 0, 0, 0, 0, 0 ,0 , 0, 0, 0, 0, 2],
        [2, 0, 2, 0, 2, 0, 2 ,0 , 2, 0, 2, 0, 2],
        [2, 0, 0, 0, 0, 0, 0 ,0 , 0, 0, 0, 0, 2],
        [2, 0, 2, 0, 2, 0, 2 ,0 , 2, 0, 2, 0, 2],
        [2, 0, 0, 0, 0, 0, 0 ,0 , 0, 0, 0, 0, 2],
        [2, 0, 2, 0, 2, 0, 2 ,0 , 2, 0, 2, 0, 2],
        [2, 0, 0, 0, 0, 0, 0 ,0 , 0, 0, 0, 0, 2],
        [2, 0, 2, 0, 2, 0, 2 ,0 , 2, 0, 2, 0, 2],
        [2, 0, 0, 0, 0, 0, 0 ,0 , 0, 0, 0, 0, 2],
        [2, 2, 2, 2, 2, 2, 2 ,2 , 2, 2, 2, 2, 2]]

#Players
number_of_players=2
Players = [pygame.image.load('red.png'), pygame.image.load('blue.png')]
for i in range(2):
    Players[i]=pygame.transform.scale(Players[i], (45,45))

PlayersX =[0,0]
PlayersY = [0,0]
playerX_change=[0,0]
playerY_change=[0,0]

playerX_counter=[0,0]
playerY_counter=[0,0]

#Putting players
counter=number_of_players
while counter > 0:
    line=random.randint(1,12)
    collumn=random.randint(1,12)
    if matrix[line][collumn]!=2 and matrix[line][collumn]<2:
        matrix[line][collumn]=counter-1+3
        PlayersX[counter-1]=line*40+280
        PlayersY[counter-1]=collumn*40+80
        counter-=1

# Putting barrels
# TREBUIE VERIFICAT SA NU FIE IN JURUL FIX AL JUCATORULUI!!
random_barrels=40
while random_barrels > 0:
    line=random.randint(1,12)
    collumn=random.randint(1,12)
    if matrix[line][collumn]!=2 and matrix[line][collumn]!=1 and matrix[line][collumn]<3:
        matrix[line][collumn]=1
        random_barrels=random_barrels-1


# GameShow
screen.blit(background, (0,0))

for i in range (13):
    for j in range (13):
        if matrix[i][j]==2:
            screen.blit(stone, (i*40+280, j*40+80))
        if matrix[i][j]==1:
            screen.blit(barrel, (i*40+280, j*40+80))
        if matrix[i][j]>2:
            screen.blit(Players[matrix[i][j]-3], (PlayersX[matrix[i][j]-3], PlayersY[matrix[i][j]-3]))


pygame.display.update()
running = True
i=0
while running:
     

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                playerX_change[0]=-1
            if event.key == pygame.K_d:
                playerX_change[0]=1
            if event.key == pygame.K_w:
                playerY_change[0]=-1
            if event.key == pygame.K_s:
                playerY_change[0]=1
            if event.key == pygame.K_LEFT:
                playerX_change[1]=-1
            if event.key == pygame.K_RIGHT:
                playerX_change[1]=1
            if event.key == pygame.K_UP:
                playerY_change[1]=-1
            if event.key == pygame.K_DOWN:
                playerY_change[1]=1
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key==pygame.K_DOWN:
                playerY_change[1]=0
            if event.key == pygame.K_LEFT or event.key==pygame.K_RIGHT:
                playerX_change[1]=0
            if event.key == pygame.K_w or event.key==pygame.K_s:
                playerY_change[0]=0
            if event.key == pygame.K_a or event.key==pygame.K_d:
                playerX_change[0]=0

    for i in range(number_of_players):

        PlayersX[i]+=playerX_change[i]
        playerX_counter[i]+=playerX_change[i]
   
         
        PlayersY[i]+=playerY_change[i]
        playerY_counter[i]+=playerY_change[i]

    
    screen.blit(background, (0,0))
    for i in range (13):
     for j in range (13):
        if matrix[i][j]==2:
            screen.blit(stone, (i*40+280, j*40+80))
        if matrix[i][j]==1:
            screen.blit(barrel, (i*40+280, j*40+80))    

    for i in range(number_of_players):
        screen.blit(Players[i], (PlayersX[i], PlayersY[i]))

    pygame.display.update()

