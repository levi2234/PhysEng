
import numpy as np
class Particle():
    """
    Represents a particle in a physical simulation.

    Parameters:
        position (list): The position of the particle in 3D space.
        mass (float): The mass of the particle.
        velocity (list): The velocity of the particle in 3D space.
        radius (float): The radius of the particle.
        charge (float): The charge of the particle.
        drag_coeff (float): The drag coefficient of the particle.
        name (str): The name of the particle.
        color (list): The color of the particle as RGB values.
        environment (object): The environment in which the particle exists.
    """

    def __init__(self, position=[0,0,0], mass=0.5, velocity=[0,0,0], radius=0, charge=0, drag_coeff=0, name="Particle", color=[255,255,255], environment=None, **kwargs) -> None:
        self.__name__ = name
        self.__version__ = "0.0.1"
        
        self.mass = mass
        self._position = np.array(position)
        self._velocity = np.array(velocity)
        self.radius = radius
        self.force = np.array([0, 0, 0])
        self.environment = environment
        self.charge = charge
        self.drag_coeff = drag_coeff
        self.fixed = False #imoprtant for anchor
        self.previous_force = np.array([0, 0, 0])
        self.color = color
        
    def __str__(self) -> str:
        particle_description = f" Particle: {self.__name__} \n Version: {self.__version__} \n Mass: {self.mass} \n Position: {self.position} \n Velocity: {self.velocity} \n Force: {self.force}, \n Environment: {self.environment} "
        return particle_description

    # Disable change in position of particle when fixed
    @property
    def position(self):
        return self._position
    
    @position.setter # Ignore attempts to change position
    def position(self, value):
        if self.fixed:
            pass
        else:
            self._position = value
            
    @property
    def velocity(self):
        return self._velocity
    
    @velocity.setter # Ignore attempts to change velocity
    def velocity(self, value):
        if self.fixed:
            pass
        else:
            self._velocity = value
        
    
        
        

    
