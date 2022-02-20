from abc import abstractclassmethod, abstractmethod
from pygame import image as pgimage, transform
from pygame.sprite import Sprite
from core.Spritesheet import *

SPRITES_ROOT = 'assets/sprites'
class AnimatedSprite(Sprite):
  def __init__(self, json_path, spritesheet_path, name, starting_position=(0,0), size=(32,32), default_animation='idle'):
    Sprite.__init__(self)
    self.spritesheet = Spritesheet(json_path, spritesheet_path, name, default_animation)
    self.size = size
    self.flip_blit = False
    self.image = self.transform_image()
    self.rect = self.image.get_rect(left=0, top=0)
    self.rect.x = starting_position[0]
    self.rect.y = starting_position[1]

  def transform_image(self):
    current_image = self.spritesheet.current_image.tobytes()
    temp = pgimage.fromstring(current_image, self.spritesheet.current_rect, 'RGBA')
    temp = transform.flip(temp, self.flip_blit, False)
    image = transform.scale(temp, self.size)
    return image

  def change_animation(self, animation_name):
    self.spritesheet.set_current_animation(animation_name)
    return self.transform_image()

  def get_center(self):
    center_x = round(self.rect.x + (self.size[0]/2))
    center_y = round(self.rect.y + (self.size[1]/2))
    return (center_x, center_y)

  @abstractmethod
  def update(self):
    pass