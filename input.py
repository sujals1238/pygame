import pygame
from pygame.draw import circle

pygame.init()

window_1 = pygame.display.set_mode((500,500))
clock_bhai = pygame.time.Clock()
dt = 1
speed = pygame.Vector2(0,30)  # Set horizontal speed to 0
player_pos = pygame.Vector2(window_1.get_width() / 2 , window_1.get_height() / 2)
running = True
circle_radius=20
while running:
    window_1.fill("black")
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    gola = pygame.draw.circle(window_1, "red", (int(player_pos.x), int(player_pos.y)), circle_radius)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
       player_pos.y -= 300*dt
    if keys[pygame.K_s]:
       player_pos.y += 300*dt
    if keys[pygame.K_a]:
       player_pos.x -= 300*dt
    if keys[pygame.K_d]:
       player_pos.x += 300*dt
    if keys[pygame.K_q]:
       running =False
     
    if player_pos.x >= (window_1.get_width() + (circle_radius)) :
        player_pos.x = 0 - circle_radius
    pygame.display.flip()
    dt = clock_bhai.tick(60) / 1000

pygame.quit()
