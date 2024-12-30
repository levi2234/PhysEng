import numpy as np
class UniformForceField():
    """
    Represents a uniform force field in a physics simulation.
    
    Attributes:
        environment (Environment): The environment in which the force field operates.
        F (list): The force vector in the form [Fx, Fy, Fz].
        name (str): The name of the force field.
        active (bool): Indicates whether the force field is active or not.
    """
    
    def __init__(self, environment, F=[0,9.81,0], name="Uniform Force Field", active=True) -> None:
        self.name = name
        self.environment = environment
        self.F = np.array(F)
        self.active = active
        
    def update(self):
        """
        Updates the force applied to particles in the environment.
        """
        if self.active == False:
            return
        
        for i in self.environment.particles:
            i.force = i.force + self.F
