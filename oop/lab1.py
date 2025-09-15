import pygame

pygame.init()

window = pygame.display.set_mode((400,400))

pygame.display.set_caption("Ten cua so")

clock = pygame.time.Clock()

run = True
while run:
    pygame.time.delay(100)
    window.fill((12, 24, 186))

    pygame.draw.polygon(window, (231, 76, 60), [(200, 0), (400, 200), (200,400), (0, 200)])
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            run = False

    pygame.display.update()
    clock.tick(30)
  

pygame.quit   

