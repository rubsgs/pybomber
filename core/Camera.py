import pygame

from enum import Enum
""" TODO(tulio) - refactor nas classes Hero e Camera para usar a mesma BaseClass """


class Direcoes(Enum):
    CIMA = 1
    BAIXO = 2
    ESQUERDA = 3
    DIREITA = 4


class Camera:

    CAMERA_SPEED = 10

    def __init__(self, screen, x=0, y=0):
        self.screen = screen
        self.x = x
        self.y = y
        self.width = screen.get_width()
        self.height = screen.get_height()
        self.velocidade_x = 0
        self.velocidade_y = 0
        self.is_moving = False
        self.moving_direction = None
        self.target_x = self.x
        self.target_y = self.y

    @property
    def position(self):
        return (self.x, self.y)

    def move(self):
        if not self.is_moving:
            return self.is_moving

        self.x += self.velocidade_x
        self.y += self.velocidade_y

        self.check_target()

        return self.is_moving

    def emit_camera_event(self, direction):
        self.moving_direction = direction
        self.is_moving = True
        if direction == Direcoes.BAIXO:
            self.target_y = self.y + self.height
            self.velocidade_y = self.CAMERA_SPEED
        elif direction == Direcoes.CIMA:
            self.target_y = self.y - self.height
            self.velocidade_y = -self.CAMERA_SPEED

    def check_target(self):
        if self.is_moving and self.moving_direction == Direcoes.BAIXO:
            if self.y >= self.target_y and self.is_moving:
                self.is_moving = False
                self.moving_direction = None
                self.target_y = self.y
                self.y = self.target_y
                print('finishing camera move baixo')
                finished_moving = pygame.event.Event(
                    pygame.USEREVENT, {'name': 'camera_moved'})
                pygame.event.post(finished_moving)
                print('event fired')
        elif self.is_moving and self.moving_direction == Direcoes.CIMA:
            if self.y <= self.target_y and self.is_moving:
                self.is_moving = False
                self.moving_direction = None
                self.target_y = self.y
                self.y = self.target_y
                print('finishing camera move cima')
                finished_moving = pygame.event.Event(
                    pygame.USEREVENT, {'name': 'camera_moved'})
                pygame.event.post(finished_moving)
                print('event fired')
