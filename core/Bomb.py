from core.AnimatedSprite import *
from core.Events import TICK_CLOCK
from pygame.time import set_timer
class Bomb(AnimatedSprite):
  ASSETS_ROOT = 'assets/sprites/bomb'
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
    'PLACED': 1,
    'EXPLODING': 2,
    'EXPLODED': 3
  }

  def __init__(self, type=TYPES['WEAK'], starting_position=(0,0), size=(32,32)):
    AnimatedSprite.__init__(self, Bomb.JSON_PATH[type], Bomb.SPRITESHEET_PATH[type], 'Bomb', starting_position, size, default_animation='bomb')
    self.type = type
    self.damage = Bomb.DAMAGES[self.type]
    self.range = Bomb.RANGES[self.type]
    self.time = Bomb.TIME[self.type]
    self.status = Bomb.STATUS['PLACED']
    set_timer(TICK_CLOCK, 1000, self.time)

  def tick(self):
    self.time -= 1
    if self.time <= 0:
      self.start_explosion()
  
  def start_explosion(self):
    if(self.status == Bomb.STATUS['EXPLODING']): return
    self.status = Bomb.STATUS['EXPLODING']
    self.change_animation('explosion')
    
  def update(self):
    if(self.spritesheet.current_animation_dict != 'bomb'):
      self.spritesheet.loop()
      self.status = Bomb.STATUS['EXPLODED'] if self.spritesheet.animation_over else self.status
    self.image = self.transform_image()
