import pygame
from pygame.sprite import Sprite, spritecollide
from core.Grid import *

from core.Spritesheet import *



class Hero(Sprite):
  ASSETS_ROOT = 'assets/sprites/hero'
  SPRITESHEET_PATH = f'{ASSETS_ROOT}/spritesheet.png'
  JSON_PATH = f'{ASSETS_ROOT}/spritesheet_meta.json'
  #TODO
  def __init__(self, starting_position=(0,0), size=(32, 32)):
    Sprite.__init__(self)
    self.spritesheet = Spritesheet(Hero.JSON_PATH, Hero.SPRITESHEET_PATH, 'Hero')
    self.size = size
    self.set_defaults()
    self.image = self.transform_image()
    self.rect = self.image.get_rect(left=starting_position[0], top=starting_position[0])

  def set_defaults(self):
    self.default_speed_value = 16
    self.flip_blit = False
    self.horizontal_speed = 0
    self.vertical_speed = 0
    self.movement_keys = [0, 0, 0, 0]

  def transform_image(self):
    current_image = self.spritesheet.current_image.tobytes()
    temp = pygame.image.fromstring(current_image, self.spritesheet.current_rect, 'RGBA')
    temp = pygame.transform.flip(temp, self.flip_blit, False)
    image = pygame.transform.scale(temp, self.size)
    return image

  def change_animation(self, animation_name):
    self.spritesheet.set_current_animation(animation_name)
    return self.transform_image()

  def update(self, group):
    self.spritesheet.loop()

    old_x = self.rect.x
    old_y = self.rect.y

    self.rect.x += self.horizontal_speed
    self.rect.y += self.vertical_speed
    if len(spritecollide(self, group, dokill=False)) > 0:
       self.rect.x = old_x
       self.rect.y = old_y

    self.image = self.transform_image()

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
    elif(keycode == pygame.K_ESCAPE):
      pygame.quit()

    if(not self.is_moving()):
      self.change_animation('idle')

  def is_moving(self):
    return self.movement_keys[0] or self.movement_keys[1] or self.movement_keys[2] or self.movement_keys[3]

  def get_rect(self):
    return self.image.get_rect(left=self.rect.x, top=self.rect.y)

  def check_collision(self, grid: Grid):
    collision_list = self.get_rect().collidelist(grid.collidables_rects)
    return collision_list >= 0
