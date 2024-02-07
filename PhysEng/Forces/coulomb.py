
import numpy as np

class Coulomb():
    
    def __init__(self, environment, k=8.9875517873681764e9, softening_length=0) -> None:
        self.__name__ = "Coulomb"
        self.environment = environment
        self.softening_length = softening_length
        self.k = k
        
    def update(self):
        for i in self.environment.particles:
            for j in self.environment.particles:
                if i != j:
                    r = j.position - i.position
                    i.force = i.force + self.k * -i.charge * j.charge * r / (np.linalg.norm(r) + self.softening_length)**3 