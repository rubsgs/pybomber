import pygame
import random
import math
from core.Collidable import *

class Rock(Collidable):
  TYPES = [Collidable.WEAK,Collidable.MEDIUM,Collidable.STRONG,Collidable.UNBREAKABLE]
  
  HP = [0 for i in TYPES]
  HP[Collidable.WEAK] = 75
  HP[Collidable.MEDIUM] = 100
  HP[Collidable.STRONG] = 500
  HP[Collidable.UNBREAKABLE] = math.inf

  SPRITES_PATHS = [0 for i in TYPES]
  SPRITES_PATHS[Collidable.WEAK] = 'assets/sprites/environment/rocha_75.png'
  SPRITES_PATHS[Collidable.MEDIUM] = 'assets/sprites/environment/rocha_100.png'
  SPRITES_PATHS[Collidable.STRONG] = 'assets/sprites/environment/rocha_500.png'
  SPRITES_PATHS[Collidable.UNBREAKABLE] = 'assets/sprites/environment/rocha_unb.png'

  SPRITES = []
  
  #TODO - Desacoplar Rock de screen
  def __init__(self, type=Collidable.UNBREAKABLE, grid_x=0, grid_y=0, screen=None, size=(32,32)):
    Collidable.__init__(self, pygame.transform.scale(Rock.SPRITES[type], size), type, grid_x=grid_x, grid_y=grid_y, size=size)
    self.screen = screen
    self.hp = Rock.HP[self.type]

  @staticmethod
  def make_random_rock(random_state, screen, size=(32,32), grid_position=(0,0), allow_unbreakable=False):
    random.setstate(random_state)
    random_type = -1
    while random_type == -1 or (random_type == Collidable.UNBREAKABLE and not allow_unbreakable):
      random_type = random.randint(0, len(Rock.TYPES) -1)
    
    return Rock(random_type, grid_position[0], grid_position[1], screen, size)

  @staticmethod
  def load_sprites():
    for type in Rock.TYPES:
      path = Rock.SPRITES_PATHS[type]
      Rock.SPRITES.append(pygame.image.load(path))

  #TODO - Render
  def render(self):
    self.screen.blit(self.surface, (self.x, self.y))