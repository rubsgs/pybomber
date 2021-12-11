import pygame
import time
from Ball import *
from core.Camera import Camera, Direcoes
from core.Hero import *
from pygame.locals import *

from core.Map import Map


class App:
    def __init__(self):
        self._running = True
        self.screen = None
        self.padding = [96, 96]
        self.size = self.weight, self.height = 672, 672
        self.ball = None
        self.background = pygame.image.load('assets/backgrounds/bg_lava.png')
        self.clock = pygame.time.Clock()

    def on_init(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.size, pygame.HWSURFACE)
        self.background = pygame.transform.scale(self.background, self.size)
        self.map = Map(self.screen, Map.MAP1)
        self.camera = Camera(self.screen)
        self.hero = Hero(self.screen, self.camera, padding=self.padding,
                         x=self.padding[0], y=self.padding[1])
        self._running = True
        self._paused = False

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
        if event.type == pygame.USEREVENT:
            self.handle_user_event(event)
            return

        return

    def on_loop(self):
        if self.camera.is_moving:
            self.camera.move()
            self.hero.horizontal_speed = self.camera.velocidade_x
            self.hero.vertical_speed = self.camera.velocidade_y
            self.hero.loop(self.map)
            return

        if not self._paused:
            self.check_map_change()

        self.hero.loop(self.map)

    def check_map_change(self):
        """ TODO(tulio) - Por esse magica number em uma constante """
        if self.hero.y - self.camera.y < -150 and not self._paused:
            self._paused = True
            self.camera.emit_camera_event(Direcoes.CIMA)
        if self.hero.y - self.camera.y + self.camera.height > 150 and not self._paused:
            self._paused = True
            self.camera.emit_camera_event(Direcoes.BAIXO)

    def on_render(self):
        self.screen.fill((0, 0, 0))
        self.map.render(self.camera)
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

    def handle_user_event(self, event: pygame.event.Event):
        if(not hasattr(event, 'name')):
            raise ValueError('User event must have a name')

        if(event.name == 'camera_moved'):
            self.hero.vertical_speed = 0
            self.hero.horizontal_speed = 0
            print((self.hero.x, self.hero.y))
            self.hero.y -= self.hero.size[1]
            print('acertou mizeravi')
            return
        else:
            raise ValueError('Invalid user event')


if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()
