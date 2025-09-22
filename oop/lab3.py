import pygame
import math

pygame.init()
window = pygame.display.set_mode((400,400))
pygame.display.set_caption("Lab3")
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

    def goc(self):
        lst = []
        for i in range(self.points):
            x = math.cos(i * self.angle) * self.radius + self.center[0]
            y = math.sin(i * self.angle) * self.radius + self.center[1]
            lst.append((x,y))
        return lst
    
    def draw(self):
        pygame.draw.polygon(self.window, self.color, self.goc(), self.stroke_weight)

class Polygon(Hexagon):
    def __init__(self, center, radius, window, points, color=(179, 55, 113)):
        self.center = center
        self.points = points
        self.radius = radius
        self.window = window
        self.angle = math.radians(360 / self.points)
        self.color = color
        self.grow = 0
        self.stroke_weight = 3 


    def calculate_length(self):
        self.grow += 0.1
        length = abs(math.sin(self.grow)) * self.radius
        return length
    
    def goc(self):
        lst = []
        length = self.calculate_length()
        for i in range(self.points):
            x = math.cos(i * self.angle) * length + self.center[0]
            y = math.sin(i * self.angle) * length + self.center[1]
            lst.append((x,y))
        return lst
    
run = True
polygon = Polygon((200, 200), 140, window, 8, (255, 19, 30))

while run:
    
    window.fill((55, 55, 55))

    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            run = False

    polygon.draw()
    pygame.display.update()
    clock.tick(30)
pygame.quit()
