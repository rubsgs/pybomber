import pygame
import random
import Rock
from math import floor

class Grid:
  #TODO - Desacoplar Grid de screen
  def __init__(self, screen, size=(768,768), total_columns=21, total_rows=21):
    self.screen = screen
    self.total_columns = total_columns
    self.total_rows = total_rows
    self.size = size
    self.cell_width = floor(self.size[0]/self.total_rows)
    self.cell_height = floor(self.size[1]/self.total_columns)
    self.element_matrix = self.init_matrix()
    self.seed = random.SystemRandom()
    print(f'Generated seed is {self.seed}')
    self.element_matrix = self.generate_level_matrix()


  def init_matrix(self):
    return [[0 for i in range(self.total_rows)] for j in range(self.total_columns)]

  def generate_level_matrix(self):
    #não gera rocha indestrutivel nas bordas do mapa
    #não gera rocha no [0, 1] e [1, 0] para não deixar o player preso
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
    #Rock.get_random_rock(self.seed, self.screen)

  #TODO - Render
  def render():
    return