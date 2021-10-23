import pygame
from core.Spritesheet import *

class Hero:
  def __init__(self, screen, x=0, y=0, size=(200,200)):
    self.assets_root = 'assets/sprites/hero'
    self.sprite_json_path = f'{self.assets_root}/spritesheet_meta.json'
    self.spritesheet_path = f'{self.assets_root}/spritesheet.png'
    self.spritesheet = Spritesheet(self.sprite_json_path, self.spritesheet_path, 'Hero')
    self.default_speed_value = 10

    self.screen = screen
    self.size = size
    self.x = x
    self.y = y
    self.horizontal_speed = 0
    self.vertical_speed = 0
    self.movement_keys = [0,0,0,0]
    self.flip_blit = False
    self.transform_blit()

  def transform_blit(self):
    temp = pygame.image.fromstring(self.spritesheet.current_image.tobytes(), self.spritesheet.current_rect, 'RGBA')
    temp = pygame.transform.flip(temp, self.flip_blit, False)
    self.surface = pygame.transform.scale(temp, self.size)
    return self.surface

  def change_animation(self, animation_name):
    self.spritesheet.set_current_animation(animation_name)
    return self.transform_blit()
  
  def loop(self):
    self.spritesheet.loop()
    self.x += self.horizontal_speed
    self.y += self.vertical_speed
    self.surface = self.transform_blit()

  def render(self):
    self.screen.blit(self.surface, (self.x, self.y))

  def onKeyDown(self, keycode):
    if(keycode == pygame.K_LEFT):
        self.horizontal_speed = -self.default_speed_value
        self.movement_keys[0] = 1
        self.flip_blit = True
    elif(keycode == pygame.K_UP):
        self.vertical_speed = -self.default_speed_value
        self.movement_keys[1] = 1
    elif(keycode == pygame.K_RIGHT):
        self.horizontal_speed = self.default_speed_value
        self.movement_keys[2] = 1
        self.flip_blit = False
    elif(keycode == pygame.K_DOWN):
        self.vertical_speed = self.default_speed_value
        self.movement_keys[3] = 1
    if(self.is_moving()):
      self.change_animation('run')

  def onKeyUp(self, keycode):
    if(keycode == pygame.K_LEFT):
        self.horizontal_speed = 0
        self.movement_keys[0] = 0
    elif(keycode == pygame.K_UP):
        self.vertical_speed = 0
        self.movement_keys[1] = 0
    elif(keycode == pygame.K_RIGHT):
        self.horizontal_speed = 0
        self.movement_keys[2] = 0
    elif(keycode == pygame.K_DOWN):
        self.vertical_speed = 0
        self.movement_keys[3] = 0
    if(not self.is_moving()):
      self.change_animation('idle')
    
  def is_moving(self):
    return self.movement_keys[0] or self.movement_keys[1] or self.movement_keys[2] or self.movement_keys[3]