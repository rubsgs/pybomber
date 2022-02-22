import pygame
from pygame.sprite import Sprite, spritecollide, RenderPlain
from pygame.time import set_timer
from pygame import event
from core.Events import TICK_CLOCK, INVULNERABILITY_OVER, MOVEMENT_LOCK_OVER
from core.Grid import *
from core.AnimatedSprite import *
from core.Spritesheet import *
from core.Bomb import *



class Hero(AnimatedSprite):
  HANDLED_EVENTS = [
    TICK_CLOCK,
    MOVEMENT_LOCK_OVER,
    INVULNERABILITY_OVER,
    pygame.KEYDOWN,
    pygame.KEYUP
  ]

  ASSETS_ROOT = f'{SPRITES_ROOT}/hero'
  SPRITESHEET_PATH = f'{ASSETS_ROOT}/spritesheet.png'
  JSON_PATH = f'{ASSETS_ROOT}/spritesheet_meta.json'
  DEFAULT_INVULNERABILITY_TIME = 2000
  DEFAULT_MOVEMENT_LOCK_TIME = 1000
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
    self.placed_bombs = RenderPlain()
    self.max_bombs = 1
    self.current_bomb_type = Bomb.TYPES['WEAK']
    self.invunerable = False
    self.invunerable_frame_index = 0
    self.can_move = True
    self.hp = 5

  def update(self, group):
    self.remove_exploded_bombs()
    self.spritesheet.loop()

    old_x = self.rect.x
    old_y = self.rect.y
  
    self.rect.x += self.horizontal_speed
    self.rect.y += self.vertical_speed
    if len(spritecollide(self, group, dokill=False)) > 0 or not self.can_move:
       self.rect.x = old_x
       self.rect.y = old_y

    self.image = self.transform_image()
    if(self.invunerable):
      #imagem pisca se estiver invulneravel
      self.opacity = 0 if self.invunerable_frame_index > 1 else 255
      self.invunerable_frame_index = (self.invunerable_frame_index + 1)%4
      self.image.set_alpha(self.opacity)
    self.placed_bombs.update()

  def on_key_down(self, keycode, grid):
    if keycode in self.movement_keys:
      self.handle_movement(keycode, 1)
    elif(keycode == pygame.K_SPACE):
      self.handle_drop_bomb(grid)

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

  def handle_drop_bomb(self, grid):
    if(len(self.placed_bombs) < self.max_bombs):
      #bomb_position e bomb_coord serve para não spawnar bombas no meio de um tile
      bomb_position = grid.get_position_from_coord((self.rect.x, self.rect.y))
      bomb_coord = grid.get_coord_from_position(bomb_position)
      self.placed_bombs.add(Bomb(self.current_bomb_type, bomb_coord, self.size))
    return

  def on_key_up(self, keycode, grid):
    if keycode in self.movement_keys:
      self.handle_movement(keycode, 0)

    if(not self.is_moving()):
      self.change_animation('idle')

  def is_moving(self):
    return any([True for key, value in self.movement_keys.items() if value == 1])

  def get_rect(self):
    return self.image.get_rect(left=self.rect.x, top=self.rect.y)

  #TODO verificar colisão apenas de blocos próximos do player
  def check_collision(self, grid):
    collision_list = self.get_rect().collidelist(grid.collidables_rects)
    return collision_list >= 0

  def draw_bombs(self, screen):
    self.placed_bombs.draw(screen)

  def tick_bombs(self):
    for bomb in self.placed_bombs:
      bomb.tick()

  def handle_event(self, event, grid):
    if event.type == pygame.KEYDOWN:
      self.on_key_down(event.key, grid)
      return
    if event.type == pygame.KEYUP:
      self.on_key_up(event.key, grid)
      return
    if event.type == TICK_CLOCK and len(self.placed_bombs.sprites()) > 0:
      self.tick_bombs()
      return
    if event.type == MOVEMENT_LOCK_OVER:
      if event.id == id(self):
        self.can_move = True
      return
    if event.type == INVULNERABILITY_OVER:
      if event.id == id(self):
        self.invunerable = False
        self.opacity = 255
      return

  def handle_damage(self):
    if(self.invunerable):
      return
    self.hp -= 1
    self.invunerable = True
    self.can_move = False
    set_timer(event.Event(INVULNERABILITY_OVER, {'id': id(self)}), Hero.DEFAULT_INVULNERABILITY_TIME, 1)
    set_timer(event.Event(MOVEMENT_LOCK_OVER, {'id': id(self)}), Hero.DEFAULT_MOVEMENT_LOCK_TIME, 1)


  def remove_exploded_bombs(self):
    for bomb in self.placed_bombs:
      if(bomb.status == Bomb.STATUS['EXPLODED']):
        self.placed_bombs.remove(bomb)