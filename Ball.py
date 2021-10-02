import pygame
class Ball:
    def __init__(self, screen):
        self.speed = [1, 1]
        self.image = pygame.image.load("assets/sprites/intro_ball.gif")
        self.rect = self.image.get_rect()
        self.screen = screen


    def loop(self):
        self.rect = self.rect.move(self.speed)
        if(self.rect.left < 0 or self.rect.right > pygame.display.get_window_size()[0]):
            self.speed[0] = -self.speed[0]

        if(self.rect.top < 0 or self.rect.bottom > pygame.display.get_window_size()[1]):
            self.speed[1] = -self.speed[1]

    def render(self):
        self.screen.blit(self.image, self.rect)

