import pygame
import os

class Game
  def __init__(self):
      self.width = 1000
      self.height = 700
      self.win = pygame.display.set_mode((self.width, self.height))
      self.enemys = []
      self.towers = []
      self.lives = 1
      self.money = 100
      
  def run(self):
    run = True
    while run:
      for event in pygame.event.get():
          if event.type == pygame.QUIT:
              run = False
  pygame.quit
    