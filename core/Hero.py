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
    self.movement_keys = {
      pygame.K_LEFT: 0,
      pygame.K_UP: 0,
      pygame.K_RIGHT: 0,
      pygame.K_DOWN: 0
    }
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

  def on_key_down(self, keycode):
    if keycode in self.movement_keys:
      self.handle_movement(keycode, 1)
    elif(keycode == pygame.K_SPACE):
      self.handle_drop_bomb()

    if(self.is_moving()):
      self.change_animation('run')

  def handle_movement(self, keycode, moving):
    self.movement_keys[keycode] = moving
    if(self.movement_keys[pygame.K_LEFT]):
      self.horizontal_speed = -self.default_speed_value
      self.flip_blit = True
    elif(self.movement_keys[pygame.K_RIGHT]):
      self.horizontal_speed = self.default_speed_value
      self.flip_blit = False
    else:
      self.horizontal_speed = 0

    if(self.movement_keys[pygame.K_UP]):
      self.vertical_speed = -self.default_speed_value
    elif(self.movement_keys[pygame.K_DOWN]):
      self.vertical_speed = self.default_speed_value
    else:
      self.vertical_speed = 0
    return

  def handle_drop_bomb(self):
    if(len(self.placed_bombs) < self.max_bombs):
      self.placed_bombs.add(Bomb(self.current_bomb_type, (self.rect.x, self.rect.y), self.size))
    return

  def on_key_up(self, keycode):
    if keycode in self.movement_keys:
      self.handle_movement(keycode, 0)
    elif(keycode == pygame.K_ESCAPE):
      pygame.quit()

    if(not self.is_moving()):
      self.change_animation('idle')

  def is_moving(self):
    return any([True for key, value in self.movement_keys.items() if value == 1])

  def get_rect(self):
    return self.image.get_rect(left=self.rect.x, top=self.rect.y)

  #TODO verificar colisão apenas de blocos próximos do player
  def check_collision(self, grid: Grid):
    collision_list = self.get_rect().collidelist(grid.collidables_rects)
    return collision_list >= 0

  def draw_bombs(self, screen):
    self.placed_bombs.draw(screen)