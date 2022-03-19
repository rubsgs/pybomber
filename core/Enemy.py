import pygame
from pygame.sprite import Sprite, spritecollide, RenderPlain
from core.Events import TICK_CLOCK
from core.Grid import *
from core.AnimatedSprite import *
from core.Spritesheet import *
from core.Bomb import *

class Enemy(AnimatedSprite):
  #TODO
  ASSETS_ROOT = f''
  SPRITES_PATH = f''
  JSON_PATH = f''

  # Ideia inicial:
  # O bot irá escolher um jogador/inimigo 
  # aleatório(inicialmente só 1 jogador existirá)
  # e irá calcular um caminho para chegar até ele,
  # a cada X turnos/tick(necessário definir O QUE é um turno)
  # ele irá recalcular essa rota baseado no jogador/inimigo mais próximo
  # 
  # Ainda é necessário pensar em uma estratégia para atacar/prender
  # os inimigos


  # Outra ideia - Fila de movimentos:
  # Bot pode fazer X ações predeterminadas,
  # A cada ação/tick, o bot avalia o grid inteiro
  # e escolhe uma ação para tomar.
  # Talvez seja possível pensar em formas de botar pesos
  # nessa ações a fim de possibilitar a escolha do melhor
  # caminho possível

  #TODO
  def __init__(self, starting_position=(0,0), size=(32,32)):
    return

  #Calcula o caminho a seguir no grid para chegar em destination
  def resolve_path(self, destination, grid):
    return

  #Verifica se está preso
  #Teoricamente a única forma de ficar preso é
  #se o jogador ou outro inimigo colocar uma bomba 
  #que faça com que o bot não consiga sair
  def is_stuck(self, grid):
    return

  #Se colocar uma bomba na localização atual
  #o bot irá se danificar?
  def bomb_self_damage(self, grid):
    return
  
  def update(self, group):
    return

  def get_rect(self):
    return

  def check_collision(self, grid):
    return
  
  def draw_bombs(self, screen):
    return

  def tick_bombs(self):
    return

  def handle_event(self, event, grid):
    return

  def remove_exploded_bombs(self):
    return