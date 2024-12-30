import numpy as np

class leapfrog():
    """
    The leapfrog class represents a leapfrog integrator for simulating particle motion in a physical environment.
    
        
    Args:
        environment (object): The environment object.
        name (str): The name of the integrator.
    
    """

    def __init__(self, environment=None, name="RLeapFrog") -> None:
        self.environment = None
        self.name = name

    def update(self):
        """
        Updates the positions and velocities of particles in the environment using the leapfrog integration method.
        """
        for i in self.environment.particles:
            k1 = i.velocity
            l1 = i.force / i.mass
            k2 = i.velocity + l1 * self.environment.dt / 2
            l2 = (i.force + k1 * self.environment.dt / 2) / i.mass
            k3 = i.velocity + l2 * self.environment.dt / 2
            l3 = (i.force + k2 * self.environment.dt / 2) / i.mass
            k4 = i.velocity + l3 * self.environment.dt
            l4 = (i.force + k3 * self.environment.dt) / i.mass

            i.position = i.position + (k1 + 2*k2 + 2*k3 + k4) * self.environment.dt / 6
            i.velocity = i.velocity + (l1 + 2*l2 + 2*l3 + l4) * self.environment.dt / 6
            i.previous_force = i.force
            i.force = np.array([0,0,0])
       