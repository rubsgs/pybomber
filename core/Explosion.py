from core.AnimatedSprite import *
from pygame.sprite import RenderUpdates

class Explosion(AnimatedSprite):
  ASSETS_ROOT = f'{SPRITES_ROOT}/explosion'
  JSON_PATH = f'{ASSETS_ROOT}/spritesheet_meta.json'
  SPRITESHEET_PATH = f'{ASSETS_ROOT}/spritesheet.png'

  STATUS = {
    'EXPLODING': 0,
    'EXPLODED': 1
  }

  def __init__(self, starting_position=(0,0), size=(32,32)):
    AnimatedSprite.__init__(self, Explosion.JSON_PATH, Explosion.SPRITESHEET_PATH, 'Explosion', starting_position, size, default_animation='explosion')
    self.status = Explosion.STATUS['EXPLODING']

  def update(self):
    self.spritesheet.loop()
    self.image = self.transform_image()
    self.status = Explosion.STATUS['EXPLODED'] if self.spritesheet.animation_over else Explosion.STATUS['EXPLODING']

  @staticmethod
  def make_explosions_from_event(event, grid):
    explosion_center = (event.rect.x, event.rect.y)
    returned_explosions = [Explosion(explosion_center)]
    position_center = grid.get_position_from_coord(explosion_center)
    grid_x_range = range(position_center[0]-event.range, position_center[0]+event.range + 1)
    grid_y_range = range(position_center[1]-event.range, position_center[1]+event.range + 1)
    for x in grid_x_range:
      if x < 0 or x == position_center[0] or x > grid.total_columns-1:
        continue
      if grid.element_matrix[x][position_center[1]] != -1:
        continue

      explosion_position = grid.get_coord_from_position((x, position_center[1]))
      returned_explosions.append(Explosion(explosion_position))

    for y in grid_y_range:
      if y < 0 or y == position_center[1] or y > grid.total_columns-1:
        continue
      if grid.element_matrix[position_center[0]][y] != -1:
        continue

      explosion_position = grid.get_coord_from_position((position_center[0], y))
      returned_explosions.append(Explosion(explosion_position))
      
    return returned_explosions
