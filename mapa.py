import pygame as pg

_ = False

# Mapa do Jogo
miniMapa = [
    [ 1, 1, 1, 1, 1, 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1],
    [ 1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [ 1, _, _, 1, 1, 1, 1, _, _, _, 1, 1, 1, _, _, 1],
    [ 1, _, _, _, _, _, 1, _, _, _, _, _, 1, _, _, 1],
    [ 1, _, _, _, _, _, 1, _, _, _, _, _, 1, _, _, 1],
    [ 1, _, _, 1, 1, 1, 1, _, _, _, _, _, _, _, _, 1],
    [ 1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [ 1, _, _, 1, _, _, _, 1, _, _, _, _, _, _, _, 1],
    [ 1, 1, 1, 1, 1, 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1]
]


class Mapa:
    def __init__(self,game):
        self.game = game
        self.miniMapa = miniMapa
        self.mapaMundo = {}
        self.get_mapa()

    def get_mapa(self):
        for j,linha in enumerate(self.miniMapa):
            for i, valor in enumerate(linha):
                if valor:
                    self.mapaMundo[(i,j)] = valor

    def draw(self):
       [pg.draw.rect(self.game.tela, "darkgray", (pos[0] * 100, pos[1] * 100,100,100), 2)
        for pos in self.mapaMundo]