import os
import sys
from pygame import Surface
import pytmx
from pygame.sprite import Sprite

ROOT_PATH = os.path.dirname(sys.modules['__main__'].__file__)
MAPS_PATH = ROOT_PATH + '/assets/maps/'


class Map:
  ASSETS_ROOT = 'assets/maps/' if ROOT_PATH == '' else MAPS_PATH
  MAP1 = f'{ASSETS_ROOT}/map1/map1.tmx'
  LAVA1 = f'{ASSETS_ROOT}/lava1/lava1.tmx'

  def __init__(self, map) -> None:
    self.data = self.get_map_resource(map)

  def get_map_resource(self, map_path):
    if os.path.exists(map_path):
      return pytmx.load_pygame(map_path)
    elif os.path.exists(MAPS_PATH + map_path):
      return pytmx.load_pygame(MAPS_PATH + map_path)
    else:
      raise Exception('Mapa não encontrado')

  def draw(self, surface: Surface):
    for layer in self.data:
      for (x_pixel, y_pixel, tile) in layer.tiles():
        surface.blit(tile, (x_pixel * tile.get_width(), y_pixel * tile.get_height()))

