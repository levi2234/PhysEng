import pygame as pg
from PhysEng.Visualize.xytopygame import xy_to_topygame as xy
from PhysEng.Integrators.rk4 import rk4

class EnableRK4():
    
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