import pygame
import random
from core.Rock import * 
from core.Map import *
from core.Collidable import *
from math import floor

class Grid:
  #TODO - Desacoplar Grid de screen
  def __init__(self, screen, map, size=(672,672), padding=(96,96), total_rocks=10):
    self.screen = screen
    self.map = Map(self.screen,map)
    self.total_columns = 0
    self.total_rows = 0
    self.size = size
    self.padding = padding
    self.collidables = []
    self.collidables_rects = []
    self.init_matrix()
    self.cell_width = floor((self.size[0] - self.padding[0])/self.total_rows)
    self.cell_height = floor((self.size[1] - self.padding[1])/self.total_columns)
    self.seed = random.SystemRandom()
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
          collidable = Collidable(img, Collidable.MAP, grid_x=x, grid_y=y)
          self.collidables.append(collidable)
          self.collidables_rects.append(collidable.get_rect())
        else:
          self.element_matrix[x].append(-1)
      self.element_matrix.append([])

    self.total_columns = len(self.element_matrix) - 2
    self.total_rows = len(self.element_matrix[0]) - 2

  def generate_level_matrix(self):
    for i in range(self.total_rocks):
      random_column = random.randint(1, self.total_columns -1)
      random_row = random.randint(1, self.total_rows -1)
      if self.element_matrix[random_column][random_row] != -1:
        i -= 1
        continue
      
      rock = Rock.make_random_rock(random.getstate(), self.screen, grid_position=(random_column, random_row), allow_unbreakable=True)
      self.element_matrix[random_column][random_row] = rock
      self.collidables.append(rock)
      self.collidables_rects.append(rock.get_rect())

  #TODO - Arrumar um jeito não quadratico de renderizar
  def render(self):
    self.map.render()
    if(not self.element_matrix): raise Exception('Matriz não iniciada')
    for column in self.element_matrix:
      for element in column:
        if element != -1 and element != Collidable.MAP:
          element.render()
    return

  def check_collision(self, rect):
    return rect.collision_list(self.collidables)