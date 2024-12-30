import numpy as np  
class Drag():
    """
    Represents a drag force acting on particles in an environment.
    
    Attributes:
        environment (Environment): The environment in which the particles are present.
        density (float): The density of the medium through which the particles are moving.
        name (str): The name of the drag force.
        active (bool): Indicates whether the drag force is active or not.
    """
    
    def __init__(self, environment, density=1, name="Drag", active=True) -> None:
        self.__name__ = name
        self.environment = environment
        self.density = density
        self.active = active
        
    def update(self): 
        """
        Updates the forces acting on the particles due to drag.
        """
        if self.active is False:
            return
        
        for i in self.environment.particles:
            i.force = i.force - 0.5 * i.drag_coeff * self.density * i.velocity * np.linalg.norm(i.velocity) * i.radius**2 * np.pi