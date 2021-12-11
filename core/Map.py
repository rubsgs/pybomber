import os
import sys
from pygame import Surface
import pytmx

ROOT_PATH = os.path.dirname(sys.modules['__main__'].__file__)
MAPS_PATH = ROOT_PATH + '/assets/maps/'


class Map:

    MAP1 = 'map1/map1.tmx'

    def __init__(self, screen, map) -> None:
        self.screen = screen
        self.data = self.get_map_resouce(map)

    def get_map_resouce(self, map_path):
        if os.path.exists(map_path):
            return pytmx.load_pygame(map_path)
        elif os.path.exists(MAPS_PATH + map_path):
            return pytmx.load_pygame(MAPS_PATH + map_path)
        else:
            raise Exception('Mapa não encontrado')

    def render(self,camera):
        aux_surface = Surface((self.screen.get_width(),self.screen.get_height()))
        for layer in self.data:
            for tile in layer.tiles():
                x_pixel = tile[0]
                y_pixel = tile[1]
                surface = tile[2]
                img = tile[2]
                aux_surface.blit(img, (camera.x + x_pixel * surface.get_width(),camera.y + y_pixel * surface.get_height()))

        self.screen.blit(aux_surface, (0,0))

