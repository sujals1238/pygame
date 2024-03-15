import pygame
from pygame.draw import circle

pygame.init()

window_1 = pygame.display.set_mode((500,500))
clock_bhai = pygame.time.Clock()
dt = 1
speed = pygame.Vector2(0,30)
player_pos = pygame.Vector2(window_1.get_width() /2 , window_1.get_height()/2)
running = True

while running:
    window_1.fill("black")
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
 

    player_pos += speed*dt
    gola = pygame.draw.circle(window_1, "red",(int(player_pos.x),int(player_pos.y)), 20)
 
if player_pos.y > window_1.get_height() - 20 or player_pos.y < 20:
    speed.y *= -1

    # flip the damn screen
    pygame.display.flip()

    dt = clock_bhai.tick(60) / 60

pygame.quit()

