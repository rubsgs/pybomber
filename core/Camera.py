import pygame

""" TODO(tulio) - refactor nas classes Hero e Camera para usar a mesma BaseClass """


class Camera:

    CAMERA_SPEED = 10

    def __init__(self, screen, x=0, y=0):
        self.screen = screen
        self.x = x
        self.y = y
        self.w = screen.get_width()
        self.h = screen.get_height()
        self.velocidade_x = 0
        self.velocidade_y = 0
        self.is_moving = False
        self.target_x = self.x
        self.target_y = self.y

    def move(self):
        if not self.is_moving:
            return self.is_moving

        self.x += self.velocidade_x
        self.y += self.velocidade_y

        if self.y >= self.target_y and self.is_moving:
            self.is_moving = False
            self.target_y = self.y
            self.y = self.target_y
            print('finishing camera move')
            finished_moving = pygame.event.Event(pygame.USEREVENT, {'name': 'camera_moved'})
            pygame.event.post(finished_moving)
            print('event fired')

        return self.is_moving

