import json
from PIL import Image
import pygame.image

class Spritesheet:
  meta_cache = {}
  image_cache = {}

  def __init__(self, json_path, spritesheet_path, name='none', default_animation='idle'):
    with open(json_path, 'r') as f:
      self.meta = json.load(f)
      
    self.spritesheet = pygame.image.load(spritesheet_path)
    self.set_current_animation(default_animation)
    self.name = name
    self.current_image = self.set_current_image()
    self.animation_over = False

  def set_current_rect(self, sprite_index = 0):
    self.current_rect = self.meta[self.current_animation_dict]['sprite_rects'][sprite_index]['rect']

  def set_current_animation(self, animation_name):
    if animation_name in self.meta:
      self.current_animation_dict = animation_name
      self.current_sprite_index = 0
      self.current_animation_length = self.meta[self.current_animation_dict]['animation_length']
      self.set_current_rect()
      return self.set_current_image()
    else:
      raise Exception(f'{animation_name} not found in SpriteAnimation {self.name}')

  def get_current_rect_start(self):
    current_start = self.meta[self.current_animation_dict]['sprite_rects'][self.current_sprite_index]['start']
    return (current_start[0], current_start[1])

  def get_current_rect_crop(self):
    left, top = self.get_current_rect_start()
    right = left + self.current_rect[0]
    bottom = top + self.current_rect[1]
    return (left, top, right, bottom)

  def set_current_image(self):
    self.set_current_rect(self.current_sprite_index)
    rect_start = self.get_current_rect_start()
    self.current_image = self.spritesheet.blit(self.spritesheet, (0,0), (rect_start[0], rect_start[1], self.current_rect[0], self.current_rect[1]))
    return self.current_image

  
  def loop(self):
    next_sprite = self.current_sprite_index + 1
    self.current_sprite_index = next_sprite % self.current_animation_length
    self.animation_over = True if next_sprite == self.current_animation_length else False
    return self.set_current_image()