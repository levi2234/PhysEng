import numpy as np

class Gravity():
    """
    Represents a gravity force in a given environment.
    """

    def __init__(self, environment, G=6.67430e-11, softening_length=0, name="Gravity", active=True) -> None:
        """
        Initializes a Gravity object.

        Parameters:
        - environment: The environment in which the gravity force acts.
        - G: The gravitational constant. Default value is 6.67430e-11.
        - softening_length: The softening length used to avoid singularities. Default value is 0.
        - name: The name of the gravity force. Default value is "Gravity".
        - active: Specifies whether the gravity force is active or not. Default value is True.
        """
        self.name = name
        self.environment = environment
        self.G = G
        self.softening_length = softening_length
        self.active = active
        
    def update(self):
        """
        Updates the forces acting on the particles in the environment due to gravity.
        """
        if self.active == False:
            return
        
        for i in self.environment.particles:
            for j in self.environment.particles:
                if i != j:
                    r = j.position - i.position
                    i.force = i.force + self.G * i.mass * j.mass * r / (np.linalg.norm(r) + self.softening_length)**3