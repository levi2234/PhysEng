import numpy as np

class Gravity():
    
    def __init__(self, environment, G=6.67430e-11, softening_length=0, name="Gravity", active=True) -> None:
        
        self.name = name
        self.environment = environment
        self.G = G
        self.softening_length = softening_length
        self.active = active
        
    def update(self):
        if self.active == False:
            return
        
        
        for i in self.environment.particles:
            for j in self.environment.particles:
                if i != j:
                    r = j.position - i.position
                    i.force = i.force + self.G * i.mass * j.mass * r / (np.linalg.norm(r) + self.softening_length)**3