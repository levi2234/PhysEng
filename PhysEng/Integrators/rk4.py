import numpy as np
class rk4():
    
    def __init__(self) -> None:
        self.environment = None
        
        
    def update(self):
        for i in self.environment.particles:
            k1 = i.velocity
            l1 = i.force / i.mass
            k2 = i.velocity + l1 * self.environment.dt / 2
            l2 = i.force / i.mass
            k3 = i.velocity + l2 * self.environment.dt / 2
            l3 = i.force / i.mass
            k4 = i.velocity + l3 * self.environment.dt
            l4 = i.force / i.mass
            
            i.position = i.position + (k1 + 2*k2 + 2*k3 + k4) * self.environment.dt / 6
            i.velocity = i.velocity + (l1 + 2*l2 + 2*l3 + l4) * self.environment.dt / 6
            i.previous_force = i.force
            i.force = np.array([0,0,0])