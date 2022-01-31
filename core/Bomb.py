from core.AnimatedSprite import *
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
    TYPES['WEAK']: 2,
    TYPES['MEDIUM']: 4,
    TYPES['STRONG']: 8
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

  TIMER = {
    TYPES['WEAK']: 5,
    TYPES['MEDIUM']: 5,
    TYPES['STRONG']: 5
  }

  def __init__(self, type=TYPES['WEAK'], starting_position=(0,0), size=(32,32)):
    AnimatedSprite.__init__(self, Bomb.JSON_PATH[type], Bomb.SPRITESHEET_PATH[type], 'Bomb', starting_position, size, default_animation='bomb')
    self.type = type
    self.damage = Bomb.DAMAGES[self.type]
    self.range = Bomb.RANGES[self.type]
    self.timer = Bomb.TIMER[self.type]