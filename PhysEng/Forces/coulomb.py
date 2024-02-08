
import numpy as np

class Coulomb():
    
    def __init__(self, environment, k=8.9875517873681764e9, softening_length=0, name= "Coulomb", active=True) -> None:
        self.__name__ = name
        self.environment = environment
        self.softening_length = softening_length
        self.k = k
        self.active = active
        
    def update(self):
        if self.active == False:
            return
        
        for i in self.environment.particles:
            for j in self.environment.particles:
                if i != j:
                    r = j.position - i.position
                    i.force = i.force + self.k * -i.charge * j.charge * r / (np.linalg.norm(r) + self.softening_length)**3 