import pygame as pg
from PhysEng.Visualize.xytopygame import xy_to_topygame as xy

class ShowParticles():
    
    def __init__(self, visualize, environment) -> None:
        self.visualize = visualize
        self.environment = environment
        self.active = True
        self.name = "Particles"
        pass
    
    def show(self):
        if self.active:
            for i in self.environment.particles:
                pg.draw.circle(self.visualize.screen, (255, 255, 255), xy(self.visualize,i.position[0], i.position[1]), 5)
        pass