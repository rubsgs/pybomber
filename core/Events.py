import pygame


from pygame import USEREVENT
TICK_CLOCK = USEREVENT + 0
EXPLODE_BOMB = USEREVENT + 1
INVULNERABILITY_OVER = USEREVENT + 2
ANIMATION_OVER = USEREVENT + 3
MOVEMENT_LOCK_OVER = USEREVENT + 4