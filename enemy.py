import pygame

class Enemy
  imgs = []
  
  def __init__(self, x, y, width, height):
    self.x = x
    self.y = y
    self.width = 0
    self.height = 0
    self.animation_count = 0
    self.health = 1
    self.path = []
    self.img = none
    
  def draw(self, win):
    # draws the enemy with the given images
    # :param win: surface
    # :return: value
    self.animation_count += 1
    self.img = self.imgs[self.animation_count]
    if self.animation_count >= len(self.imgs):
        self.animation_count = 0
    win.blit(self.img, (self.x, self.y))
    self.move()
    
  def collide(self, X, Y):
    # returns if position has hit enemy
    # :param x: int
    # :param y: int
    # :return: bool
    if X <= self.x + self.width and X >= self.x:
      if Y <= self.y + self.height and Y >= self.y:
        return True
      
    return False
  
  def move(self x, y):
    #
    # :param x: int
    # :param y: int
    
  def hit(self):
    # if enemy has died and removes 1 health each call 
    # returns bool
    self.health -= 1
    if self.health <= 0:
      return True
    
  
