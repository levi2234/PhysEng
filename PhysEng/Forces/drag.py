import numpy as np  
class Drag():
    
    def __init__(self, environment, density = 1, name="Drag", active=True) -> None:
        self.__name__ = name
        self.environment = environment
        self.density = density
        self.active = active
        
        
    def update(self): 
        if self.active == False:
            return
        
        for i in self.environment.particles:
            i.force = i.force - 0.5 * i.drag_coeff * self.density * i.velocity * np.linalg.norm(i.velocity) * i.radius**2 * np.pi