import pygame as pg
from PhysEng.Visualize.xytopygame import xy_to_topygame as xypg
from PhysEng.Visualize.pygametoxy import pygame_to_xy as pgxy


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
                
                radius = 5#abs(xypg(self.visualize,i.radius, 0)[0])
                pg.draw.circle(self.visualize.screen, i.color, xypg(self.visualize,i.position[0], i.position[1]), radius)
        pass