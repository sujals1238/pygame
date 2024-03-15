import pygame
pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([500, 500])

# Set the initial position and velocity of the ball
x = 250
y = 250
vel_x = 0
vel_y = 0.25

# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the position of the ball
    # x += vel_x
    y += vel_y

    # Check if the ball hits the borders and adjust its velocity to bounce
    if x <= 75 or x >= 500-75:
        vel_x = -vel_x
    if y <= 75 or y >= 500-75:
        vel_y = -vel_y

    # Fill the background with white
    screen.fill((255, 255, 255))

    # Draw a solid blue circle in the center
    pygame.draw.circle(screen, (0, 0, 255), (x, y), 75)

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()
