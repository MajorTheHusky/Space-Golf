import pygame

class Planet:
    def __init__(self, color, pos, rad):
        self.color = color
        self.pos = pos
        self.rad = rad
    
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.pos, self.rad)

    def get_rad(self):
        return self.rad

    def get_pos(self):
        return self.pos