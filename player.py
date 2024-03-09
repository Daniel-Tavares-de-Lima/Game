from config import *
import pygame as pg
import math
from pynput.mouse import Listener, Controller


class Player:
    def __init__(self,game):
        self.game = game
        self.x,self.y = JOGADORPOS
        self.angulo = ANGULO_JOGADOR
        self.mouse_controller = Controller()
    
    def movimento(self):
        sen_a = math.sin(self.angulo)
        cos_a = math.cos(self.angulo)
        dx, dy = 0,0
        velocidade = VELO_JOGADOR * self.game.delta_tempo
        velo_sen = velocidade * sen_a
        velo_cos = velocidade * cos_a

        #Posição do mouse(VISTA DO JOGADOR)
        if self.mouse_controller.position != (0,0):
            mouseX, mouseY = self.mouse_controller.position
            relX = mouseX - self.x * 75
            relY = mouseY - self.y * 75
            self.angulo = math.atan2(relY,relX)


        teclas = pg.key.get_pressed()
        #(Controlando o jogador)
        if teclas[pg.K_w]:
            dx += velo_cos
            dy += velo_sen
        elif teclas[pg.K_s]:
            dx += -velo_cos
            dy += -velo_sen
        elif teclas[pg.K_a]:
            dx += velo_sen
            dy += -velo_cos
        elif teclas[pg.K_d]:
            dx += -velo_sen
            dy += velo_cos

      
        self.colisaoParede(dx,dy)
 
        # if teclas[pg.K_LEFT]:
        #     self.angulo -= ROTACAO_VELO_JOGADOR * self.game.delta_tempo
        # elif teclas[pg.K_RIGHT]:
        #     self.angulo += ROTACAO_VELO_JOGADOR * self.game.delta_tempo

       
        # self.angulo %= math.tau

    #Colisao das paredes
    def colisao(self, x,y):
        return(x,y) not in self.game.mapa.mapaMundo
    
    def colisaoParede(self, dx,dy):
        if self.colisao(int(self.x + dx), int(self.y)):
            self.x += dx
        if self.colisao(int(self.x), int(self.y + dy)):
            self.y += dy
    
    def draw(self):
        pg.draw.line(self.game.tela, "yellow", (self.x * 100, self.y * 100),
                     (self.x * 100 + WIDTH * math.cos(self.angulo),
                     self.y * 100 + WIDTH * math.sin(self.angulo)), 2)
        pg.draw.circle(self.game.tela, "green", (self.x * 100, self.y * 100), 15)


    def update(self):
        self.movimento()

    @property
    def pos(self):
        return self.x, self.y
    
    @property
    def mapa_pos(self):
        return int(self.x), int(self.y)
