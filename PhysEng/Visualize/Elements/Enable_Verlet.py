import pygame as pg
from PhysEng.Visualize.xytopygame import xy_to_topygame as xy
from PhysEng.Integrators.verlet import verlet

class EnableVerlet():
    
    def __init__(self, visualize, environment) -> None:
        self.visualize = visualize
        self.environment = environment
        self.active = False
        self.name = "Verlet"
        pass
    
    def show(self):
        if self.active:
            self.environment.set_integrator(verlet())
        pass