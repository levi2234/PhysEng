import pygame as pg
from PhysEng.Visualize.xytopygame import xy_to_topygame as xy

class ShowForces():
    """
    A class for visualizing force vectors in a physics simulation.

    Args:
        visualize (Visualize): The visualization object.
        environment (Environment): The environment object.
    """

    def __init__(self, visualize, environment) -> None:
        self.visualize = visualize
        self.environment = environment
        self.active = False
        self.name = "Force Vectors"
        pass
    
    def show(self):
        """
        Display the force vectors on the screen.
        """
        if self.active:
            for i in self.environment.particles:
                force = i.previous_force
                pg.draw.line(self.visualize.screen, (0, 255, 0), xy(self.visualize,i.position[0], i.position[1]), xy(self.visualize,i.position[0]+force[0], i.position[1]+force[1]), 3)
                
        pass