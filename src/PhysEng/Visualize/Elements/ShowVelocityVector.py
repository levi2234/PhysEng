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
    """
    A class for visualizing velocity vectors of particles in an environment.

    Args:
        visualize (Visualize): The visualization object.
        environment (Environment): The environment object.

    Attributes:
        visualize (Visualize): The visualization object.
        environment (Environment): The environment object.
        active (bool): Indicates if the velocity vectors are active.
        name (str): The name of the velocity vectors.
        max_velocity (int): The maximum velocity value.
    """

    def __init__(self, visualize, environment) -> None:
        self.visualize = visualize
        self.environment = environment
        self.active = False
        self.name = "Velocity Vectors"
        self.max_velocity = 100
    
    def show(self):
        """
        Draws velocity vectors for each particle in the environment.
        """
        if self.active:
            for i in self.environment.particles:
                pg.draw.line(self.visualize.screen, (0, 0, 255), xy(self.visualize,i.position[0], i.position[1]), xy(self.visualize,i.position[0]+i.velocity[0], i.position[1]+i.velocity[1]), 3)
