import pygame as pg
from PhysEng.Visualize.xytopygame import xy_to_topygame as xy
from PhysEng.Integrators.euler import euler
class EnableEuler():
    """
    A class that enables the Euler integration method for visualization. 
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
        self.active = True
        self.name = "Euler"
    
    def show(self):
        """
        Sets the integrator to Euler if it is active.
        """
        if self.active:
            self.environment.set_integrator(euler(self.environment))
