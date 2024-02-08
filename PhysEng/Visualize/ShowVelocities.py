import pygame as pg
from PhysEng.Visualize.xytopygame import xy_to_topygame as xy

class ShowVelocities():
    
    def __init__(self, visualize, environment) -> None:
        self.visualize = visualize
        self.environment = environment
        self.active = False
        self.name = "Velocities"
        pass
    
    def show(self):
        if self.active:
            for i in self.environment.particles:
                pg.draw.line(self.visualize.screen, (255, 0, 255), xy(self.visualize,i.position[0], i.position[1]), xy(self.visualize,i.position[0]+i.velocity[0], i.position[1]+i.velocity[1]), 3)

        pass