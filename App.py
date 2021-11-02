import pygame
import time
from Ball import *
from core.Hero import *
from pygame.locals import *

class App:
    def __init__(self):
        self._running = True
        self.screen = None
        self.padding = [32,32]
        self.size = self.weight, self.height = 800, 800
        self.ball = None
        self.background = pygame.image.load('assets/backgrounds/bg_lava.png');
        self.clock = pygame.time.Clock()

    def on_init(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.size, pygame.HWSURFACE)
        self.background = pygame.transform.scale(self.background, self.size)
        self.hero = Hero(self.screen)
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
        self.hero.loop()
        pass

    def on_render(self):
        self.screen.blit(self.background, self.background.get_rect())
        self.hero.render()
        pygame.display.flip()
        self.clock.tick(25)
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