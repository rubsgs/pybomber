from core.Enemy import *

class FemaleZombie(Enemy):

  ASSETS_ROOT = f'{Enemy.ASSETS_ROOT}/zombie_female'
  SPRITESHEET_PATH = f'{ASSETS_ROOT}/spritesheet.png'
  JSON_PATH = f'{ASSETS_ROOT}/spritesheet_meta.json'
  NAME = 'FemaleZombie'