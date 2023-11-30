# Example file showing a basic pygame "game loop"
import math

import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1200, 400))
clock = pygame.time.Clock()
running = True
pygame.display.set_caption('Space Invaders')
icon=pygame.image.load("spaceship.png")
pygame.display.set_icon(icon)
x_right=1100
x_left=50
y_top=20
y_bottom=340

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() *0.83)
   
def rectangle(position: pygame.Vector2, screen: pygame.Surface, *, color: pygame.Color, width: int, height:int):
     rect=pygame.Rect(position, (width, height))
     pygame.draw.rect(screen, color, rect)
     

t = 0
dt = 0.01
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and player_pos.y >y_top:
        player_pos.y -= 5
    if keys[pygame.K_DOWN]and player_pos.y <y_bottom:
        player_pos.y += 5
    if keys[pygame.K_LEFT] and player_pos.x >x_left:
        player_pos.x -= 5
    if keys[pygame.K_RIGHT] and player_pos.x <x_right:
        player_pos.x += 5
    screen.fill("black")

    rectangle(player_pos + pygame.Vector2(-40,20), screen,color= "red",height=40,width=15)
    rectangle(player_pos + pygame.Vector2(75,20), screen,color= "red",width=15,height=40)
    rectangle(player_pos + pygame.Vector2(-1,30), screen,color= "white",width=50,height=20)
    rectangle(player_pos + pygame.Vector2(40,30), screen,color= "red",width=50,height=20)
    rectangle(player_pos + pygame.Vector2(-40,30), screen,color= "red",width=50,height=20)
    
    pygame.display.flip()

    
    t += dt

pygame.quit()