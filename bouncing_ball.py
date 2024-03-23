import pygame

pygame.init()

WHITE = (255,255,255)
BLACK =(0,0,0)
RED =(255,0,0)

display = pygame.display.set_mode((1000,500))
clock = pygame.time.Clock()
FPS = 60

class Ball():
    def __init__(self):
        self.y =0
        self.velocity =1

    def draw(self):
        pygame.draw.circle(display,RED, (500,400),15)

    def game():
        ball = Ball()
    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        display.fill((WHITE))
        pygame.draw.line(display,BLACK,(0,500),(1000,500),10)
        ball.draw()
        pygame.display.update()
        clock.tick(FPS)

game()
pygame.quit