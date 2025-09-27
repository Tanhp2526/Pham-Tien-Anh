# Flappy Bird clone

import pygame
import sys
from game import Game

pygame.init()
screen = pygame.display.set_mode((400, 720))
clock = pygame.time.Clock()

game = Game('student_folder/flappy_bird/yellowbird-midflap.png', 'student_folder/flappy_bird/pipe-green.png', 'student_folder/flappy_bird/background-day.png', 'student_folder/flappy_bird/base.png')
game.resize_images()

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit() 

  game.show_background(screen)   
  
  pygame.display.update()
  clock.tick(120)