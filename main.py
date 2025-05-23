import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from circleshape import *
import sys


def main():
    pygame.init()
    clock = pygame.time.Clock() # create a Clock object
    dt = 0
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    

    x =SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    

    # create groups
    shots = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)

    player = Player(x,y, shots)

    asteroids = pygame.sprite.Group()
    

    Asteroid.containers = (asteroids, updatable, drawable)

    AsteroidField.containers = (updatable,)

    Shot.containers = (shots, updatable, drawable)

    asteroidfield = AsteroidField()

    while True: # infinite while loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black")
        for d in drawable:
            d.draw(screen)
        updatable.update(dt)
        shots.update(dt)

        for asteroid in asteroids:
            if player.collide(asteroid):
                print("Game over!")
                sys.exit()
        
        for asteroid in asteroids:
            for shot in shots:
                if shot.collide(asteroid):
                    shot.kill()
                    asteroid.split()
                    break


        pygame.display.flip()

        

        dt = clock.tick(60) / 1000 # convert from milliseconds to seconds

        

if __name__== "__main__":
    main()