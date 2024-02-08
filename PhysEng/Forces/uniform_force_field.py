import numpy as np
class UniformForceField():
    
    def __init__(self, environment, F=[0,9.81,0], name ="Uniform Force Field", active=True) -> None:
        self.name = name
        self.environment = environment
        self.F = np.array(F)
        self.active = active
        
    def update(self):
        
        if self.active == False:
            return
        
        for i in self.environment.particles:
            i.force = i.force + self.F
