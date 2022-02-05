import pygame
from pygame.sprite import Sprite
import random
import math
from core.Collidable import *
from core.AnimatedSprite import SPRITES_ROOT

class Rock(Collidable):
  TYPES = [Collidable.WEAK,Collidable.MEDIUM,Collidable.STRONG,Collidable.UNBREAKABLE]
  
  HP = [0 for i in TYPES]
  HP[Collidable.WEAK] = 75
  HP[Collidable.MEDIUM] = 100
  HP[Collidable.STRONG] = 500
  HP[Collidable.UNBREAKABLE] = math.inf

  SPRITES_PATHS = [0 for i in TYPES]
  SPRITES_PATHS[Collidable.WEAK] = f'{SPRITES_ROOT}/environment/rocha_75.png'
  SPRITES_PATHS[Collidable.MEDIUM] = f'{SPRITES_ROOT}/environment/rocha_100.png'
  SPRITES_PATHS[Collidable.STRONG] = f'{SPRITES_ROOT}/environment/rocha_500.png'
  SPRITES_PATHS[Collidable.UNBREAKABLE] = f'{SPRITES_ROOT}/environment/rocha_unb.png'

  SPRITES = []
  
  #TODO - Desacoplar Rock de screen
  def __init__(self, grid_position, type=Collidable.UNBREAKABLE, size=(32,32)):
    Collidable.__init__(self, pygame.transform.scale(Rock.SPRITES[type], size), type, grid_position, size=size)
    self.hp = Rock.HP[self.type]

  @staticmethod
  def make_random_rock(random_state, size=(32,32), grid_position=(0,0), allow_unbreakable=False):
    random.setstate(random_state)
    random_type = -1
    while random_type == -1 or (random_type == Collidable.UNBREAKABLE and not allow_unbreakable):
      random_type = random.randint(0, len(Rock.TYPES) -1)
    
    return Rock(grid_position, random_type, size)

  @staticmethod
  def load_sprites():
    for type in Rock.TYPES:
      path = Rock.SPRITES_PATHS[type]
      Rock.SPRITES.append(pygame.image.load(path))