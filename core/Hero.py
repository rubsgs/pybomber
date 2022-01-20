import pygame
from core.Map import Map

from core.Spritesheet import *



class Hero:
  #TODO
  def __init__(self, screen, x=0, y=0, size=(64, 64), padding=[0, 0]):
    self.assets_root = 'assets/sprites/hero'
    self.sprite_json_path = f'{self.assets_root}/spritesheet_meta.json'
    self.spritesheet_path = f'{self.assets_root}/spritesheet.png'
    self.spritesheet = Spritesheet(
      self.sprite_json_path, self.spritesheet_path, 'Hero')
    self.default_speed_value = 10
    self.padding = padding

    self.screen = screen
    self.size = size
    self.x = x
    self.y = y
    self.horizontal_speed = 0
    self.vertical_speed = 0
    self.movement_keys = [0, 0, 0, 0]
    self.flip_blit = False
    self.transform_blit()

  def transform_blit(self):
    temp = pygame.image.fromstring(
      self.spritesheet.current_image.tobytes(), self.spritesheet.current_rect, 'RGBA')
    temp = pygame.transform.flip(temp, self.flip_blit, False)
    self.surface = pygame.transform.scale(temp, self.size)
    return self.surface

  def change_animation(self, animation_name):
    self.spritesheet.set_current_animation(animation_name)
    return self.transform_blit()

  def loop(self, map):
    self.spritesheet.loop()

    old_x = self.x
    old_y = self.y

    self.x += self.horizontal_speed
    self.y += self.vertical_speed

    #if self.check_collision(map):
    #  self.x = old_x
    #  self.y = old_y

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
    elif(keycode == pygame.K_ESCAPE):
      pygame.quit()

    if(not self.is_moving()):
      self.change_animation('idle')

  def is_moving(self):
    return self.movement_keys[0] or self.movement_keys[1] or self.movement_keys[2] or self.movement_keys[3]

  def check_collision(self, map: Map):
    tile_width = map.data.tilewidth
    tile_height = map.data.tileheight

    player_tile_fraction = .9

    walls = []

    for layer in map.data.layers:
      for tile in layer.tiles():
        if map.data.get_tile_properties(tile[0], tile[1], 0):
          walls.append(pygame.Rect(
            tile[0] * tile_width, tile[1]*tile_height, tile_width, tile_height))

    player_rect = pygame.Rect(
      self.x, self.y, self.size[0] * player_tile_fraction, self.size[1] * player_tile_fraction)

    collision_list = player_rect.collidelist(walls)

    return collision_list >= 0
