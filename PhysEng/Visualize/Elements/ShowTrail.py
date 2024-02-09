import pygame as pg
import numpy as np
from PhysEng.Visualize.xytopygame import xy_to_topygame as xy
def velocity_to_color(velocity, max_velocity=1):
    
    try:
        color = [np.clip(int(255*velocity/max_velocity),0,254), 0, 0]
    except:
        color = [0, 0, 0]
    
    return color
class ShowTrail(
):
    
    def __init__(self, visualize, environment) -> None:
        self.visualize = visualize
        self.environment = environment
        self.active = False
        self.name = "Trail"
        self.max_velocity = 100
        pass
    
    def show(self):
        if self.active:
            dt = self.environment.dt
            for i in self.environment.particles:
                pg.draw.line(self.visualize.screen, (255, 255, 255), xy(self.visualize,i.position[0], i.position[1]), xy(self.visualize,i.position[0]+i.velocity[0]* dt, i.position[1]+i.velocity[1]* dt), i.radius)
        pass