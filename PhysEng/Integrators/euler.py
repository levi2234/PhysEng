import numpy as np

class euler():
    
    def __init__(self, environment,name="Euler") -> None:
        self.environment = environment
        self.name = name

        
    def update(self):
        for i in self.environment.particles:
            i.position = i.position + i.velocity * self.environment.dt
            i.velocity = i.velocity + i.force / i.mass * self.environment.dt
            i.previous_force = i.force
            i.force = np.array([0,0,0])
        
    