from core.Enemy import *

class MaleZombie(Enemy):

  ASSETS_ROOT = f'{Enemy.ASSETS_ROOT}/zombie_male'
  SPRITESHEET_PATH = f'{ASSETS_ROOT}/spritesheet.png'
  JSON_PATH = f'{ASSETS_ROOT}/spritesheet_meta.json'
  NAME = 'MaleZombie'