import pygame
from constants import *


def main():
    pygame.init()
    clock = pygame.time.Clock() # create a Clock object
    dt = 0
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    while True: # infinite while loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black")
        pygame.display.flip()

        dt = clock.tick(60) / 1000 # convert from milliseconds to seconds



if __name__== "__main__":
    main()