import pygame
import time
from Ball import *
from core.Hero import *
from core.Grid import *
from pygame.locals import *
from core.Map import Map

class App:
  def __init__(self):
    self._running = True
    self.screen = None
    self.padding = [96 , 96]
    self.map_size = [672, 672]
    self.size = [self.map_size[0], self.map_size[1]]
    self.ball = None
    self.background = pygame.image.load('assets/backgrounds/bg_lava.png')
    self.clock = pygame.time.Clock()

  def on_init(self):
    pygame.init()
    self.screen = pygame.display.set_mode(self.size, pygame.HWSURFACE)
    self.background = pygame.transform.scale(self.background, self.size)
    self.grid = Grid(self.screen, Map.LAVA1, self.map_size, self.padding, total_rocks=50)
    self.hero = Hero(self.screen, padding=self.padding, x=self.padding[0], y=self.padding[1])
    self._running = True

  def on_event(self, event):
    if event.type == pygame.QUIT:
      self._running = False
      return
    if event.type == pygame.KEYDOWN:
      self.hero.onKeyDown(event.key)
      return
    if event.type == pygame.KEYUP:
      self.hero.onKeyUp(event.key)
      return
      
    return

  def on_loop(self):
    self.hero.loop(self.grid)

  def on_render(self):
    self.grid.render()
    self.hero.render()
    pygame.display.flip()
    self.clock.tick(30)
    pass

  def on_cleanup(self):
    pygame.quit()

  def on_execute(self):
    if self.on_init() == False:
      self._running = False

    while self._running:
      for event in pygame.event.get():
        self.on_event(event)
      self.on_loop()
      self.on_render()
    self.on_cleanup()


if __name__ == "__main__":
  theApp = App()
  theApp.on_execute()