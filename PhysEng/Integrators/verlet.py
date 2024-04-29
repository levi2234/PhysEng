import numpy as np

class verlet():
    """
    Verlet integration class for simulating particle motion.
    
    Args:
        environment (object): The environment object containing the particles.
        name (str): The name of the integrator.
    """
    def __init__(self, environment=None, name="Verlet") -> None:
        self.environment = environment   
        self.name = name 

        
    def update(self):
        """
        Update the positions and velocities of particles using the Verlet integration method.
        """
        for i in self.environment.particles:
            i.position = i.position + i.velocity * self.environment.dt + 0.5 * i.force / i.mass * self.environment.dt**2
            i.velocity = i.velocity + 0.5 * (i.force / i.mass + i.force / i.mass) * self.environment.dt
            i.previous_force = i.force
            i.force = np.array([0,0,0])