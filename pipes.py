import pygame
import numpy as num
import random as rand
# Initialize Pygame
pygame.init()

# Set up display
width, height = 900, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("My First Pygame Program")
Running = True

game_speed = 1

def generating_pipes():
    x_up = 500
    x_down = x_up
    y_up = rand.randint(0,100)
    y_down = y_up + 100 + 250
    
    #draw rectangles
    rectUpp1 = pygame.Rect(x_up, y_up, 50, 250)
    rectDown1 = pygame.Rect(x_down, y_down, 50 , 250)

    y_up = rand.randint(0,100)
    y_down = y_up + 100 + 250
    rectUpp2 = pygame.Rect(x_up+300, y_up, 50, 250)
    rectDown2 = pygame.Rect(x_down+300, y_down, 50 , 250)

    return [rectUpp1,rectDown1,rectUpp2,rectDown2]

    



list = generating_pipes()


# Main game loop
while Running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False
    
    # background color of the screen
    screen.fill((0,0,0))

    
    list[0].x -= game_speed
    list[1].x -= game_speed

    list[2].x -= game_speed
    list[3].x -= game_speed

    if list[0].x < 0:
        list[0].x = 900
        list[1].x = 900
    elif list[2].x < 0:
        list[2].x = 900
        list[3].x = 900

    pygame.draw.rect(screen,(250,250,250),list[0])
    pygame.draw.rect(screen,(250,250,250),list[1])

    pygame.draw.rect(screen,(250,250,250),list[2])
    pygame.draw.rect(screen,(250,250,250),list[3])
    #pygame.Rect.move(rectUpp,game_speed,0)

    pygame.display.update()
            