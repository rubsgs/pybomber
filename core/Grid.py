import pygame
import random
from core.Rock import * 
from math import floor

class Grid:
  #TODO - Desacoplar Grid de screen
  def __init__(self, screen, size=(672,672), padding=(96,96), total_columns=19, total_rows=19, total_rocks=10):
    self.screen = screen
    self.total_columns = total_columns
    self.total_rows = total_rows
    self.size = size
    self.padding = padding
    self.cell_width = floor((self.size[0] - self.padding[0])/self.total_rows)
    self.cell_height = floor((self.size[1] - self.padding[1])/self.total_columns)
    self.element_matrix = self.init_matrix()
    self.seed = random.SystemRandom()
    random.seed(self.seed)
    self.total_rocks = total_rocks
    Rock.load_sprites()
    print(f'Generated seed is {self.seed}')
    self.generate_level_matrix()


  def init_matrix(self):
    return [[-1 for i in range(self.total_rows)] for j in range(self.total_columns)]

  def generate_level_matrix(self):
    for i in range(self.total_rocks):
      random_column = random.randint(1, self.total_columns -1)
      print(f'random_column is {random_column}')
      random_row = random.randint(1, self.total_rows -1)
      print(f'random_row is {random_row}')

      if (random_column == 1 and random_row == 1) or self.element_matrix[random_column][random_row] != -1:
        i -= 1
        continue
      
      self.element_matrix[random_column][random_row] = Rock.make_random_rock(random.getstate(), self.screen, grid_position=(random_column, random_row), allow_unbreakable=True)

  #TODO - Arrumar um jeito não quadratico de renderizar
  def render(self):
    if(not self.element_matrix): raise Exception('Matriz não iniciada')
    for column in self.element_matrix:
      for element in column:
        if element != -1:
          element.render()
    return