import numpy as np

class ph4():
    
    def __init__(self, environment) -> None:
        self.environment = environment
        
        
    def update(self):
        for i in self.environment.particles:
            i.position = i.position + i.velocity * self.environment.dt
            i.velocity = i.velocity + i.force / i.mass * self.environment.dt
            i.force = np.array([0, 0, 0]) #reset force after update
        
    