import pygame

# pygame setup

pygame.init()
screen = pygame.display.set_mode((400, 800))
clock = pygame.time.Clock()
running = True

#SpaceShip image and its size

spaceship_img = pygame.image.load("spaceship.png")
spaceship_img = pygame.transform.scale(spaceship_img, (50, 60))
bg_img = pygame.image.load("spaceinvadersBG.png")

# Screen Name and Space Ship

pygame.display.set_caption('Space Invaders')

# SpaceShip Boundaries
x_right = 330
x_left = 30
y_top = 450
y_bottom = 720

# Key Press Speed (Number of pixels space ship moves on each press)

press_speed=5

# Space Ship position 

player_pos = pygame.Vector2(screen.get_width() / 2 -20, screen.get_height() * 0.9)

def rectangle(position: pygame.Vector2, screen: pygame.Surface, *, color: pygame.Color, width: int, height: int):
    rect = pygame.Rect(position, (width, height))
    pygame.draw.rect(screen, color, rect)
    
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and player_pos.y > y_top:
        player_pos.y -= press_speed
    if keys[pygame.K_DOWN] and player_pos.y < y_bottom:
        player_pos.y += press_speed
    if keys[pygame.K_LEFT] and player_pos.x > x_left:
        player_pos.x -= press_speed
    if keys[pygame.K_RIGHT] and player_pos.x < x_right:
        player_pos.x += press_speed

    screen.blit(bg_img, (0,0))
    screen.blit(spaceship_img, (player_pos.x, player_pos.y))
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
