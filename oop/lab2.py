import pygame
import math

pygame.init()
window = pygame.display.set_mode((400,400))
pygame.display.set_caption("Ten cua so")
clock = pygame.time.Clock()

class Hexagon:
    def __init__(self, center, radius, window):
        self.center = center
        self.radius = radius
        self.window = window
        self.points = 6
        self.angle = math.radians(360 / self.points)
        self.color = (179, 55, 113)
        self.stroke_weight = 3

    def calculate_vertices(self):
        lst = []
        for i in range(self.points):
            x = math.cos(i * self.angle) * self.radius + self.center[0]
            y = math.sin(i * self.angle) * self.radius + self.center[1]
            lst.append((x,y))
        return lst
    
    def draw(self):
        pygame.draw.polygon(self.window, self.color, self.calculate_vertices(), self.stroke_weight)


run = True
hexagon = Hexagon((200,200), 125, window)

while run:
    pygame.time.delay(100)
    window.fill((55, 55, 55))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    hexagon.draw()
    pygame.display.update()

pygame.quit()
