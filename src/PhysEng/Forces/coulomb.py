
import numpy as np

class Coulomb():
    """
    Represents the Coulomb force between charged particles in an environment.
    """

    def __init__(self, environment, k=8.9875517873681764e9, softening_length=0, name="Coulomb", active=True) -> None:
        """
        Initializes a Coulomb force object.

        Parameters:
        - environment: The environment containing the particles.
        - k: The Coulomb constant (default value is 8.9875517873681764e9).
        - softening_length: The softening length to prevent singularities (default value is 0).
        - name: The name of the Coulomb force (default value is "Coulomb").
        - active: Indicates whether the Coulomb force is active (default value is True).
        """
        self.__name__ = name
        self.environment = environment
        self.softening_length = softening_length
        self.k = k
        self.active = active
        
    def update(self):
        """
        Updates the forces acting on the particles in the environment due to the Coulomb force.
        """
        if self.active is False:
            return
        
        for i in self.environment.particles:
            for j in self.environment.particles:
                if i != j:
                    r = j.position - i.position
                    i.force = i.force + self.k * -i.charge * j.charge * r / (np.linalg.norm(r) + self.softening_length)**3
