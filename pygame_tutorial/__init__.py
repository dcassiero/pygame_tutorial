# Import a library of functions called 'pygame'
import pygame
import math

# Initialize the game engine
pygame.init()

# Define some colors. These are CONSTANT variables, so uppercase.
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

PI = math.pi

size = (320, 200)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Daniel's First Game with pygame!")

# Loop until the user clicks the close button.
done = False

# This is used to manage how fast the screen updates.
clock = pygame.time.Clock()

# -------- Main Program Loop --------
while not done:
    # --- Main Event Loop
    for event in pygame.event.get():  # The player did something
        if event.type == pygame.QUIT:  # If the player clicked close
            print("Player asked to quit.")
            done = True  # Flag that we are done so we exit this loop
        elif event.type == pygame.KEYDOWN:
            print("Player pressed a key.")
        elif event.type == pygame.KEYUP:
            print("Player let go of a key.")
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("Player pressed a mouse button.")

    # --- Game Logic Goes Here

    # --- Drawing Logic Goes Here

    # First, clear the screen to WHITE. Do not put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(WHITE)

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second (fps)
    clock.tick(60)
