import numpy as np

class UniformAccelerationField():
    """
    Represents a uniform acceleration field in a physics simulation.
    
    Attributes:
        environment (Environment): The environment in which the field exists.
        a (list): The acceleration vector [ax, ay, az].
    """
    
    def __init__(self, environment, a=[0, 9.81, 0], name="Uniform Acceleration Field", active=True) -> None:
        """
        Initializes a UniformAccelerationField object.
        
        Args:
            environment (Environment): The environment in which the field exists.
            a (list, optional): The acceleration vector [ax, ay, az]. Defaults to [0, 9.81, 0].
        """
        self.name = name
        self.environment = environment
        self.a = np.array(a)
        self.active = active
        
    def update(self):
        """
        Updates the forces acting on particles in the environment based on the acceleration field.
        """
        if self.active == False:
            return
        
        
        for i in self.environment.particles:
            i.force = i.force + (i.mass * self.a)
            