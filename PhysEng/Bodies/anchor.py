import numpy as np


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
        pass
    
    @property
    def velocity(self):
        return self._velocity
    
    @velocity.setter #ignore attempts to change velocity
    def velocity(self, value):
        pass
    
    @property
    def force(self):
        return np.array([0,0,0])
    
    @force.setter #ignore attempts to change force
    def force(self, value):
        pass
    
    @property
    def mass(self):
        return self._mass
    
    @mass.setter #ignore attempts to change mass
    def mass(self, value):
        pass
    
    @property
    def radius(self):
        return self._radius
    
    @radius.setter #ignore attempts to change radius
    def radius(self, value):
        pass
    
    @property
    def charge(self):
        return self._charge
    
    @charge.setter #ignore attempts to change charge
    def charge(self, value):
        pass
    
    @property
    def drag_coeff(self):
        return self._drag_coeff
    
    @drag_coeff.setter #ignore attempts to change drag_coeff
    def drag_coeff(self, value):
        pass
    
    
    def __str__(self):
        return f'Anchor at {self.position} with mass {self.mass} and radius {self.radius}'
    