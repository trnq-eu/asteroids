from circleshape import *
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, PLAYER_RADIUS)
        
    
    def draw(self, screen):
        center = (self.position.x, self.position.y)
        pygame.draw.circle(screen, "white", center, self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt
        

