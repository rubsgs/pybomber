from pygame.sprite import Sprite
class Collidable(Sprite):
  WEAK = 0
  MEDIUM = 1
  STRONG = 2
  UNBREAKABLE = 3
  ENEMY = 4
  MAP = 5
  
  TYPES = [WEAK,MEDIUM,STRONG,UNBREAKABLE,ENEMY,MAP]
  
  def __init__(self, surface, type, grid_position, size=(32,32)):
    Sprite.__init__(self)
    self.type = type
    self.size = size
    self.grid_x = grid_position[0]
    self.grid_y = grid_position[1]
    x = self.size[0] * grid_position[0]
    y = self.size[1] * grid_position[1]
    self.rect = surface.get_rect(left=x, top=y)
    self.image = surface

  def handle_damage(self, damage):
    if self.type == Collidable.UNBREAKABLE or self.type == Collidable.MAP: return False
    self.hp -= damage
    if self.hp <= 0:
      self.kill()
      return True
    return False