import pygame as pg
from PhysEng.Visualize.xytopygame import xy_to_topygame as xy
from PhysEng.Integrators.euler import euler
class EnableEuler():
    
    def __init__(self, visualize, environment) -> None:
        self.visualize = visualize
        self.environment = environment
        self.active = True
        self.name = "Euler"
        pass
    
    def show(self):
        if self.active:
            self.environment.set_integrator(euler(self.environment))
        pass