import numpy as np  
class Drag():
    
    def __init__(self, environment, density = 1) -> None:
        self.__name__ = "Drag"
        self.environment = environment
        self.density = density
        
        
    def update(self): 
        for i in self.environment.particles:
            i.force = i.force - 0.5 * i.drag_coeff * self.density * i.velocity * np.linalg.norm(i.velocity) * i.radius**2 * np.pi