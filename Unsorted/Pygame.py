import pygame
import random

# Initialize Pygame
pygame.init()

# Set the window size
w, h = 1000, 800
window = pygame.display.set_mode((w,h))

# Set the window background color to black
window.fill((0, 0, 0))

# Set the circle properties

circle_color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
x,y =100,50

circle_position = (x, y)




circle_radius =50
circle_direction = 1
# Draw the circle on the window surface
pygame.draw.circle(window, circle_color, circle_position, circle_radius)

# Update the display
pygame.display.update()

# Run the game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    x +=0.75 * circle_direction


# Quit Pygame
pygame.quit()