import pygame
from core.Spritesheet import *

class Hero:
  def __init__(self, screen, x=0, y=0, size=(200,200)):
    self.assets_root = 'assets/sprites/hero'
    self.sprite_json_path = f'{self.assets_root}/spritesheet_meta.json'
    self.spritesheet_path = f'{self.assets_root}/spritesheet.png'
    self.spritesheet = Spritesheet(self.sprite_json_path, self.spritesheet_path, 'Hero')

    self.screen = screen
    self.size = size
    self.x = x
    self.y = y
    self.surface = self.transform_blit()

  def transform_blit(self):
    return pygame.transform.scale(pygame.image.fromstring(self.spritesheet.current_image.tobytes(), self.spritesheet.current_rect, 'RGBA'), self.size)
  
  def loop(self):
    self.spritesheet.loop()
    self.surface = self.transform_blit()

  def render(self):
    self.screen.blit(self.surface, (self.x, self.y))