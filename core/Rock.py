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
  
  HP = [0 for i in TYPES]
  HP[WEAK] = 75
  HP[MEDIUM] = 100
  #HP[STRONG] = 500
  HP[UNBREAKABLE] = math.inf

  SPRITES_PATHS = [0 for i in TYPES]
  SPRITES_PATHS[WEAK] = 'assets/sprites/environment/rocha_75.png'
  SPRITES_PATHS[MEDIUM] = 'assets/sprites/environment/rocha_100.png'
  #SPRITES[STRONG] = 'assets/sprites/environment/rocha_500.png'
  SPRITES_PATHS[UNBREAKABLE] = 'assets/sprites/environment/rocha_500.png'

  SPRITES = []
  
  #TODO - Desacoplar Rock de screen
  def __init__(self, screen=None, x=0, y=0, size=(32,32), type=UNBREAKABLE):
    self.screen = screen
    self.x = x
    self.y = y
    self.size = size
    self.type = type
    print(f'type is {self.type}')
    self.hp = Rock.HP[self.type]
    self.surface = pygame.transform.scale(Rock.SPRITES[self.type], self.size)

  @staticmethod
  def make_random_rock(random_state, screen, size=(32,32), grid_position=(0,0), allow_unbreakable=False):
    random.setstate(random_state)
    random_type = -1
    while random_type == -1 or (random_type == Rock.UNBREAKABLE and allow_unbreakable):
      random_type = random.randint(0, len(Rock.TYPES) -1)
    
    position_x = grid_position[0] * size[0]
    position_y = grid_position[1] * size[1]
    return Rock(screen, position_x, position_y, size, random_type)

  @staticmethod
  def load_sprites():
    for type in Rock.TYPES:
      path = Rock.SPRITES_PATHS[type]
      Rock.SPRITES.append(pygame.image.load(path))

  #TODO - Render
  def render(self):
    self.screen.blit(self.surface, (self.x, self.y))