import pygame as pg
from PhysEng.Visualize.xytopygame import xy_to_topygame as xypg
from PhysEng.Visualize.pygametoxy import pygame_to_xy as pgxy


class ShowParticles():
    """
    A class for visualizing particles in a given environment through menu button toggle.
    
    Attributes:
        visualize (Visualize): The visualization object.
        environment (Environment): The environment object.
        active (bool): Flag indicating if the visualization is active.
        name (str): The name of the visualization element.
    """
    
    def __init__(self, visualize, environment) -> None:
        self.visualize = visualize
        self.environment = environment
        self.active = True
        self.name = "Particles"
        
    def show(self):
        """
        Display the particles on the visualization screen.
        """
        if self.active:
            for i in self.environment.particles:
                radius = i.radius
                pg.draw.circle(self.visualize.screen, i.color, xypg(self.visualize,i.position[0], i.position[1]), radius)
