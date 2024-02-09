import pygame as pg
import numpy as np
from PhysEng.Visualize.xytopygame import xy_to_topygame as xy
def velocity_to_color(velocity, max_velocity=1):
    
    try:
        color = [np.clip(int(255*velocity/max_velocity),0,254), 0, 0]
    except:
        color = [0, 0, 0]
    
    return color
class ShowVelocityVector():
    
    def __init__(self, visualize, environment) -> None:
        self.visualize = visualize
        self.environment = environment
        self.active = False
        self.name = "Velocity Vectors"
        self.max_velocity = 100
        pass
    
    def show(self):
        if self.active:
            for i in self.environment.particles:
                pg.draw.line(self.visualize.screen, (255, 0, 255), xy(self.visualize,i.position[0], i.position[1]), xy(self.visualize,i.position[0]+i.velocity[0], i.position[1]+i.velocity[1]), 3)
                #change color of particle to indicate velocity
                # vel_len = np.linalg.norm(i.velocity)
                # if vel_len > self.max_velocity:
                #     self.max_velocity = np.linalg.norm(i.velocity)
                #i.color = velocity_to_color(vel_len, max_velocity=self.max_velocity)
                
        pass