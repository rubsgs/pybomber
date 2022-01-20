import pygame
import random
from core.Rock import * 
from math import floor

class Grid:
  #TODO - Desacoplar Grid de screen
  def __init__(self, screen, size=(768,768), padding=(96,96), total_columns=21, total_rows=21, total_rocks=10):
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
    #não gerar rocha no [0, 1] e [1, 0] para não deixar o player preso
    self.generate_fixed_rocks()
    for i in range(self.total_rocks):
      random_column = random.randint(1, self.total_columns -1)
      print(f'random_column is {random_column}')
      random_row = random.randint(1, self.total_rows -1)
      print(f'random_row is {random_row}')
      if (random_column == 1 and random_row == 1) or self.element_matrix[random_column][random_row] != -1:
        i -= 1
        continue
      
      self.element_matrix[random_column][random_row] = Rock.make_random_rock(random.getstate(), self.screen, grid_position=(random_column, random_row), allow_unbreakable=False)

  def generate_fixed_rocks(self):
    #rochas indestrutiveis são geradas pulando 1 casa para a direita e para baixo
    iterator_x = 1
    iterator_y = 1
    
    while iterator_x < self.total_columns:
      while iterator_y < self.total_rows:
        position_x = self.cell_width * iterator_x
        position_y = self.cell_height * iterator_y
        self.element_matrix[iterator_x][iterator_y] = Rock(self.screen, position_x, position_y, (self.cell_width, self.cell_height))
        iterator_y += 2
      iterator_x += 2

  #TODO - Arrumar um jeito não quadratico de renderizar
  def render(self):
    if(not self.element_matrix): raise Exception('Matriz não iniciada')
    for column in self.element_matrix:
      for element in column:
        if element != -1:
          element.render()
    return