from config import *
import pygame as pg
import math


class Player:
    def __init__(self,game):
        self.game = game
        self.x,self.y = JOGADORPOS
        self.angulo = ANGULO_JOGADOR
    
    def movimento(self):
        sen_a = math.sin(self.angulo)
        cos_a = math.cos(self.angulo)
        dx, dy =0,0
        velocidade = VELO_JOGADOR * self.game.delta_tempo
        velo_sen = velocidade * sen_a
        velo_cos = velocidade * cos_a

        teclas = pg.key.get_pressed()

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

        self.x += dx
        self.y += dy

        if teclas[pg.K_LEFT]:
            self.angulo -= ROTACAO_VELO_JOGADOR * self.game.delta_tempo
        elif teclas[pg.K_RIGHT]:
            self.angulo += ROTACAO_VELO_JOGADOR * self.game.delta_tempo
        
        self.angulo %= math.tau


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
