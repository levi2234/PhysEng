import pygame as pg
import numpy as np
from PhysEng.Visualize.xytopygame import xy_to_topygame as xy
import matplotlib.pyplot as plt


def velocity_to_color(velocity, reference_width): #velocity is in terms of pygame pixels per second
    #map velocity to color where half the reference width is the maximum velocity color
    # velocity_len = velocity
    # if velocity_len > reference_width/2:
    #     print("Velocity exceeds maximum velocity")
    #     velocity_len = reference_width/2
    # color = (int(255 * (velocity_len/(reference_width))),0, 0)
    
    return [255,255,255]

    
    
    




    
    
class ShowVelocityColor():
    """
    A class that visualizes the velocity of particles by changing their color.
    
    Attributes:
        visualize (Visualize): The visualization object.
        environment (Environment): The environment object.
        active (bool): Indicates if the visualization is active.
        name (str): The name of the visualization.
        max_velocity (int): The maximum velocity value.
    """
    
    def __init__(self, visualize, environment) -> None:
        self.visualize = visualize
        self.environment = environment
        self.active = False
        self.name = "Velocity Color"
        self.max_velocity = 100
        pass
    
    def show(self):
        """
        Updates the color of particles based on their velocity.
        """
        if self.active:
            
            referencewidth = self.visualize.screenwidth
            
            for i in self.environment.particles:
    
                #change color of particle to indicate velocity
                vel_len = np.linalg.norm(i.velocity)
                pygame_len = xy(self.visualize, 0, vel_len)[0]
                color = velocity_to_color(pygame_len, referencewidth)
                i.color = color
        pass