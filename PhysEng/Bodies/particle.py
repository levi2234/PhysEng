
import numpy as np
class Particle():
    
    def __init__(self, position=[0,0,0], mass =0.5, velocity=[0,0,0], radius=0, charge =0,drag_coeff=0, name="", environment=None, **kwargs) -> None:
        self. __name__ = "Particle" 
        self. __version__ = "0.0.1"
        
        self.mass = mass
        self._position = np.array(position)
        self._velocity = np.array(velocity)
        self.radius = radius
        self.force = np.array([0, 0, 0])
        self.environment = environment
        self.charge = charge
        self.drag_coeff = drag_coeff
        self.fixed= False
        self.previous_force = np.array([0, 0, 0])
        self.color = (255, 255, 255)
        
        #self.jerk = (self.force - self.previous_force) / self.environment.dt

        
    def __str__(self) -> str:
        particle_discrtiption = f" Particle: {self.__name__} \n Version: {self.__version__} \n Mass: {self.mass} \n Position: {self.position} \n Velocity: {self.velocity} \n Force: {self.force}, \n Environment: {self.environment} "
        return particle_discrtiption

    #disable change in position of  particle  when fixed

    @property
    def position(self):
        return self._position
    
    @position.setter #ignore attempts to change position
    def position(self, value):
        if self.fixed:
            pass
        else:
            self._position = value
            
    @property
    def velocity(self):
        return self._velocity
    
    @velocity.setter #ignore attempts to change velocity
    def velocity(self, value):
        if self.fixed:
            pass
        else:
            self._velocity = value
        
    
        
        

    
