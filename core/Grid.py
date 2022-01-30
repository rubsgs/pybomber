from cmath import inf
import pygame
from pygame.sprite import RenderPlain
import random
from core.Rock import * 
from core.Map import *
from core.Collidable import *
from math import floor

class Grid:
  #TODO - Desacoplar Grid de screen
  def __init__(self, map, size=(672,672), padding=(96,96), total_rocks=10):
    self.map = Map(map)
    self.total_columns = 0
    self.total_rows = 0
    self.size = size
    self.padding = padding
    self.collidables = RenderPlain()
    self.generated = RenderPlain()
    self.init_matrix()
    self.cell_width = floor(self.size[0]/self.total_rows)
    self.cell_height = floor(self.size[1]/self.total_columns)
    self.seed = random.SystemRandom().randint(-sys.maxsize, sys.maxsize)
    random.seed(self.seed)
    self.total_rocks = total_rocks
    Rock.load_sprites()
    print(f'Generated seed is {self.seed}')
    self.generate_level_matrix()


  def init_matrix(self):
    self.element_matrix = [[]]
    for layer in self.map.data:
      for (x, y, gid) in layer.iter_data():
        if(x >= len(self.element_matrix)): self.element_matrix.append([])
        if self.map.data.get_tile_properties_by_gid(gid):
          self.element_matrix[x].append(Collidable.MAP)
          img = self.map.data.get_tile_image_by_gid(gid)
          collidable = Collidable(img, Collidable.MAP, (x,y))
          self.collidables.add(collidable)
        else:
          self.element_matrix[x].append(-1)

    self.total_columns = len(self.element_matrix)
    self.total_rows = len(self.element_matrix[0])

  def generate_level_matrix(self):
    for i in range(self.total_rocks):
      #-3 é para: -2 por causa das paredes das bordas, -1 para pegar o último elemnto das listas
      random_column = random.randint(1, self.total_columns -3)
      random_row = random.randint(1, self.total_rows -3)
      is_bellow_spawn = random_column == 1 and random_row == 2
      is_right_spawn = random_column == 2 and random_row == 1
      if self.element_matrix[random_column][random_row] != -1 or (random_column == 1 and random_row == 1) or is_bellow_spawn or is_right_spawn:
        i -= 1
        continue
      
      rock = Rock.make_random_rock(random.getstate(), grid_position=(random_column, random_row), allow_unbreakable=True)
      self.element_matrix[random_column][random_row] = rock
      self.generated.add(rock)
      self.collidables.add(rock)

  def draw(self, surface):
    self.map.draw(surface)
    self.generated.draw(surface)
    return

  def check_collision(self, rect):
    return rect.collision_list(self.collidables)

  def get_position_coord(self, position=(1,1)):
    return (self.cell_width * position[0], self.cell_height * position[1])
