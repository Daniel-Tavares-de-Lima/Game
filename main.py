#IMPORTS
import pygame as pg
import sys
from config import *
from mapa import *
from player import *


class Game:
    def __init__ (self):
        pg.init()
        self.tela = pg.display.set_mode(RESOLUCAO)
        self.clock = pg.time.Clock()
        self.delta_tempo = 1
        self.newGame()


    #Inicia o Jogp
    def newGame(self):
        self.mapa = Mapa(self)
        self.player = Player(self)

    #Atualiza o estado do jogo
    def update(self):
        self.player.update()
        pg.display.flip()
        self.delta_tempo = self.clock.tick(FPS)
        pg.display.set_caption(f"{self.clock.get_fps() :.1f}")

    #Desenha os elementos na tela
    def draw(self):
        self.tela.fill("black")
        self.mapa.draw()
        self.player.draw()
        
    #Verifica os eventos de entrada do usuário
    def checarEventos(self):
        for e in pg.event.get():
            if e.type == pg.QUIT or (e.type == pg.KEYDOWN and e.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()

    #Loop principal do jogo
    def run(self):
        while True:
            self.checarEventos()
            self.update()
            self.draw()

if __name__ == "__main__":
    game = Game()
    game.run()