class Collidable:
  WEAK = 0
  MEDIUM = 1
  STRONG = 2
  UNBREAKABLE = 3
  ENEMY = 4
  MAP = 5
  
  #TYPES = [WEAK,MEDIUM,STRONG,UNBREAKABLE]
  TYPES = [WEAK,MEDIUM,STRONG,UNBREAKABLE,ENEMY,MAP]
  
  def __init__(self, surface, type, grid_x=0, grid_y=0, size=(32,32)):
    self.surface = surface
    self.type = type
    self.size = size
    self.grid_x = grid_x
    self.grid_y = grid_y
    self.x = self.size[0] * grid_x
    self.y = self.size[1] * grid_y

  def get_rect(self):
    return self.surface.get_rect(left=self.x, top=self.y)