import numpy as np

class Spring_link():
    """
    Represents a spring link between two particles in a physics simulation.

    Paramters:
        particle1 (Particle Object or Anchor): The first particle connected to the spring link.
        particle2 (Particle Object or Anchor): The second particle connected to the spring link.
        k (float): The spring constant.
        l0 (float): The equilibrium length of the spring.
        damping (float): The damping coefficient.
        environment (Environment): The environment in which the spring link exists.
    """

    def __init__(self, particle1, particle2, k=1, l0=1, damping=0, environment=None) -> None:
        self.__name__ = "Spring Link"
        self.__version__ = "0.0.1"
        self.particle1 = particle1
        self.particle2 = particle2
        self.damping = damping
        self.k = k
        self.l0 = l0
        self.force = 0
        self.environment = environment
        
    def update(self, softening_length=0):
        """
        Updates the state of the spring link.

        Args:
            softening_length (float): The softening length used to prevent singularity when particles are too close.

        Returns:
            None
        """
        r = self.particle2.position - self.particle1.position
        v = self.particle2.velocity - self.particle1.velocity
        l = np.linalg.norm(r)
        F = -self.k * (l - self.l0) * (r / (l + softening_length)) - self.damping * v
        
        self.force = F
        self.particle1.force = self.particle1.force - F
        self.particle2.force = self.particle2.force + F