import numpy as np


class Anchor():
    """
    Represents an anchor in a physical simulation.
    Like a particle, but with a fixed position and mass.
    However resetting the position, mass, velocity, force, radius, charge, and drag_coeff is not allowed but are still included.

    Paramters:
        position (list): The position of the anchor in 3D space.
        mass (float): The mass of the anchor.
        velocity (list): The velocity of the anchor in 3D space.
        radius (float): The radius of the anchor.
        charge (float): The charge of the anchor.
        drag_coeff (float): The drag coefficient of the anchor.
        name (str): The name of the anchor.
        environment (object): The environment in which the anchor exists.
    """

    def __init__(self, position=[0,0,0], mass=1, velocity=[0,0,0], radius=0, charge=0, drag_coeff=0, name="", environment=None, **kwargs):
        self.__name__ = "Anchor" 
        self.__version__ = "0.0.1"
        self._mass = mass
        self._position = np.array(position)
        self._velocity = np.array(velocity)
        self._radius = radius
        self._force = np.array([0, 0, 0])
        self.color = [0,0,0]    
        self.environment = environment
        self._charge = charge
        self._drag_coeff = drag_coeff

    # Rest of the code...
class Anchor():

    
    
    def __init__(self,position=[0,0,0], mass =1, velocity=[0,0,0], radius=0, charge =0,drag_coeff=0, name="", environment=None, **kwargs):
        self. __name__ = "Particle" 
        self. __version__ = "0.0.1"
        self._mass = mass
        self._position = np.array(position)
        self._velocity = np.array(velocity)
        self._radius = radius
        self._force = np.array([0, 0, 0])
        self.color = [0,0,0]    
        self.environment = environment
        self._charge = charge
        self._drag_coeff = drag_coeff
        


    @property
    def position(self):

        return self._position
    
    @position.setter #ignore attempts to change position
    def position(self, value):
        print("Position cannot be changed")
        pass
    
    @property
    def velocity(self):
        return self._velocity
    
    @velocity.setter #ignore attempts to change velocity
    def velocity(self, value):
        print("Velocity cannot be changed")
        pass
    
    @property
    def force(self):
        return np.array([0,0,0])
    
    @force.setter #ignore attempts to change force
    def force(self, value):
        print("Force cannot be changed")
        pass
    
    @property
    def mass(self):
        return self._mass
    
    @mass.setter #ignore attempts to change mass
    def mass(self, value):
        print("Mass cannot be changed")
        pass
    
    @property
    def radius(self):
        return self._radius
    
    @radius.setter #ignore attempts to change radius
    def radius(self, value):
        print("Radius cannot be changed")
        pass
    
    @property
    def charge(self):
        return self._charge
    
    @charge.setter #ignore attempts to change charge
    def charge(self, value):
        print("Charge cannot be changed")
        pass
    
    @property
    def drag_coeff(self):
        return self._drag_coeff
    
    @drag_coeff.setter #ignore attempts to change drag_coeff
    def drag_coeff(self, value):
        print("Drag coefficient cannot be changed")
        pass
    
    
    def __str__(self):
        return f'Anchor at {self.position} with mass {self.mass} and radius {self.radius}'
    