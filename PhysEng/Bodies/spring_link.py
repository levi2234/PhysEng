import numpy as np

class Spring_link():
    def __init__(self, particle1, particle2, k=1, l0=1, damping=0) -> None:
        self.__name__ = "Spring Link"
        self.__version__ = "0.0.1"
        self.particle1 = particle1
        self.particle2 = particle2
        self.damping = damping
        self.k = k
        self.l0 = l0
        self.force = 0
        
        self.environment = None
        
    def update(self, softening_length=0):
        r = self.particle2.position - self.particle1.position
        v = self.particle2.velocity - self.particle1.velocity
        l = np.linalg.norm(r)
        F = -self.k * (l - self.l0) * (r / (l + softening_length)) - self.damping * v
        
        self.force = F
        self.particle1.force = self.particle1.force - F
        self.particle2.force = self.particle2.force + F