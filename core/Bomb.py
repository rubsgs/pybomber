from core.AnimatedSprite import *
from core.Events import TICK_CLOCK, EXPLODE_BOMB
from pygame.time import set_timer
from pygame import event
class Bomb(AnimatedSprite):
  ASSETS_ROOT = f'{SPRITES_ROOT}/bomb'
  TYPES = {
    'WEAK': 0,
    'MEDIUM': 1,
    'STRONG': 2
  }
  
  DAMAGES = {
    TYPES['WEAK']: 80,
    TYPES['MEDIUM']: 200,
    TYPES['STRONG']: 500
  }

  RANGES = {
    TYPES['WEAK']: 1,
    TYPES['MEDIUM']: 2,
    TYPES['STRONG']: 4
  }

  SPRITESHEET_PATH = {
    TYPES['WEAK']: f'{ASSETS_ROOT}/spritesheet.png',
    TYPES['MEDIUM']: f'{ASSETS_ROOT}/spritesheet.png',
    TYPES['STRONG']: f'{ASSETS_ROOT}/spritesheet.png'
  }

  JSON_PATH = {
    TYPES['WEAK']: f'{ASSETS_ROOT}/spritesheet_meta.json',
    TYPES['MEDIUM']: f'{ASSETS_ROOT}/spritesheet_meta.json',
    TYPES['STRONG']: f'{ASSETS_ROOT}/spritesheet_meta.json'
  }

  TIME = {
    TYPES['WEAK']: 3,
    TYPES['MEDIUM']: 3,
    TYPES['STRONG']: 3
  }

  STATUS = {
    'PLACED': 0,
    'EXPLODED': 1
  }

  def __init__(self, bomb_type=TYPES['WEAK'], starting_position=(0,0), size=(32,32)):
    AnimatedSprite.__init__(self, Bomb.JSON_PATH[bomb_type], Bomb.SPRITESHEET_PATH[bomb_type], 'Bomb', starting_position, size, default_animation='bomb')
    self.bomb_type = bomb_type
    self.damage = Bomb.DAMAGES[self.bomb_type]
    self.range = Bomb.RANGES[self.bomb_type]
    self.time = Bomb.TIME[self.bomb_type]
    self.status = Bomb.STATUS['PLACED']
    set_timer(TICK_CLOCK, 1000, self.time)

  def tick(self):
    self.time -= 1
    if self.time <= 0:
      self.start_explosion()
  
  def start_explosion(self):
    self.status = Bomb.STATUS['EXPLODED']
    event.post(event.Event(EXPLODE_BOMB, self.__dict__))
    
  def update(self):
    self.status = Bomb.STATUS['EXPLODED'] if self.spritesheet.animation_over else self.status
    self.image = self.transform_image()
