import pygame
import random
import math

class Rock:
  WEAK = 0
  MEDIUM = 1
  #STRONG = 2
  UNBREAKABLE = 2
  
  #TYPES = [WEAK,MEDIUM,STRONG,UNBREAKABLE]
  TYPES = [WEAK,MEDIUM,UNBREAKABLE]
  
  HP = []
  HP[WEAK] = 75
  HP[MEDIUM] = 100
  #HP[STRONG] = 500
  HP[UNBREAKABLE] = math.inf

  SPRITES = []
  SPRITES[WEAK] = 'assets/sprites/environment/rocha_75.png'
  SPRITES[MEDIUM] = 'assets/sprites/environment/rocha_100.png'
  #SPRITES[STRONG] = 'assets/sprites/environment/rocha_500.png'
  SPRITES[UNBREAKABLE] = 'assets/sprites/environment/rocha_500.png'
  
  #TODO - Desacoplar Rock de screen
  def __init__(self, screen=None, x=0, y=0, size=(32,32), type=UNBREAKABLE):
    self.screen = screen
    self.x = x
    self.y = y
    self.size = size
    self.type = type
    self.hp = Rock.HP[self.type]

  @staticmethod
  def make_random_rock(seed, screen, size=(32,32), grid_position=(0,0), allow_unbreakable=False):
    random_type = -1
    while random_type == -1 or (random_type == Rock.UNBREAKABLE and allow_unbreakable):
      random_type = random.randint(0, len(Rock.TYPES))
    
    position_x = grid_position[0] * size[0]
    position_y = grid_position[1] * size[1]
    return Rock(screen, (position_x, position_y), size, random_type)

  #TODO - Render
  def render():
    return