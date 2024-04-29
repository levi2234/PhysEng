import pygame as pg
from PhysEng.Visualize.xytopygame import xy_to_topygame as xy
from PhysEng.Integrators.rk4 import rk4

class EnableRK4():
    """
    A class that enables the Runge-Kutta 4th order integration method for visualization. 
    This class is used together with the menu to enable the Euler integration through a click

    Args:
        visualize (object): The visualization object.
        environment (object): The environment object.

    Attributes:
        visualize (object): The visualization object.
        environment (object): The environment object.
        active (bool): Indicates if the Euler integration is active.
        name (str): The name of the integration method.
    """
    
    def __init__(self, visualize, environment) -> None:
        self.visualize = visualize
        self.environment = environment
        self.active = False
        self.name = "Runge-Kutta 4th"
        pass
    
    def show(self):
        if self.active:
            self.environment.set_integrator(rk4())
        pass