import pygame
from pygame.sprite import Sprite, spritecollide, RenderUpdates
from core.Grid import *
from core.AnimatedSprite import *
from core.Spritesheet import *
from core.Bomb import *



class Hero(AnimatedSprite):
  ASSETS_ROOT = 'assets/sprites/hero'
  SPRITESHEET_PATH = f'{ASSETS_ROOT}/spritesheet.png'
  JSON_PATH = f'{ASSETS_ROOT}/spritesheet_meta.json'
  #TODO
  def __init__(self, starting_position=(0,0), size=(32, 32)):
    AnimatedSprite.__init__(self, Hero.JSON_PATH, Hero.SPRITESHEET_PATH, 'Hero', starting_position, size)
    self.set_defaults()

  def set_defaults(self):
    self.default_speed_value = 16
    self.horizontal_speed = 0
    self.vertical_speed = 0
    self.movement_keys = [0, 0, 0, 0]
    self.placed_bombs = RenderUpdates()
    self.max_bombs = 1
    self.current_bomb_type = Bomb.TYPES['WEAK']

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
    self.placed_bombs.update()

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
    elif(keycode == pygame.K_SPACE):
      print(len(self.placed_bombs))
      if(len(self.placed_bombs) < self.max_bombs):
        self.placed_bombs.add(Bomb(self.current_bomb_type, (self.rect.x, self.rect.y), self.size))
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

  #TODO verificar colisão apenas de blocos próximos do player
  def check_collision(self, grid: Grid):
    collision_list = self.get_rect().collidelist(grid.collidables_rects)
    return collision_list >= 0

  def draw_bombs(self, screen):
    self.placed_bombs.draw(screen)