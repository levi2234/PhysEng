import numpy as np

class verlet():
    def __init__(self) -> None:
        self.environment = None    
        
    def update(self):
        for i in self.environment.particles:
            i.position = i.position + i.velocity * self.environment.dt + 0.5 * i.force / i.mass * self.environment.dt**2
            i.velocity = i.velocity + 0.5 * (i.force / i.mass + i.force / i.mass) * self.environment.dt
            i.previous_force = i.force
            i.force = np.array([0,0,0])