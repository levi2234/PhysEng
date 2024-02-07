import numpy as np
class UniformForceField():
    
    def __init__(self, environment, F=[0,9.81,0]) -> None:
        self.__name__ = "Uniform Force Field"
        self.environment = environment
        self.F = np.array(F)
        
    def update(self):
        for i in self.environment.particles:
            i.force = i.force + self.F
