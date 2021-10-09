import pygame
class Ball:
    def __init__(self, screen, padding):
        #self.speed = [0, 0]
        self.size = [32, 32]
        self.default_speed_value = 38
        self.vertical_speed = 0
        self.horizontal_speed = 0
        self.image = pygame.transform.scale(pygame.image.load("assets/sprites/intro_ball.gif"), self.size)
        self.rect = self.image.get_rect()
        self.screen = screen
        self.width_padding = padding[0]
        self.height_padding = padding[1]
        self.rect = self.rect.move(padding)

    def loop(self):
        can_move = True
        if(self.rect.left < 0 + self.width_padding and self.horizontal_speed < 0):
            self.horizontal_speed = 0
            can_move = False
        elif(self.rect.right > pygame.display.get_window_size()[0] - self.width_padding and self.horizontal_speed > 0):
            self.horizontal_speed = 0
            can_move = False

        if(self.rect.top < 0 + self.height_padding and self.vertical_speed < 0):
            self.vertical_speed = 0
            can_move = False
        elif(self.rect.bottom > pygame.display.get_window_size()[1] - self.height_padding and self.vertical_speed > 0):
            self.vertical_speed = 0
            can_move = False
        if(can_move):
            self.rect = self.rect.move([self.horizontal_speed, self.vertical_speed])

        

    def render(self):
        self.screen.blit(self.image, self.rect)

    def onKeyDown(self, keycode):
        if(keycode == pygame.K_UP):
            self.vertical_speed = -self.default_speed_value
        elif(keycode == pygame.K_DOWN):
            self.vertical_speed = self.default_speed_value
        elif(keycode == pygame.K_LEFT):
            self.horizontal_speed = -self.default_speed_value
        elif(keycode == pygame.K_RIGHT):
            self.horizontal_speed = self.default_speed_value
        

    def onKeyUp(self, keycode):
        if(keycode in [pygame.K_UP, pygame.K_DOWN]):
            self.vertical_speed = 0
        if(keycode in [pygame.K_LEFT, pygame.K_RIGHT]):
            self.horizontal_speed = 0