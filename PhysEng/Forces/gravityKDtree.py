import numpy as np
from scipy.spatial import KDTree

class GravityKDTree:
    def __init__(self, environment, G=6.67430e-11, softening_length=0, name="Gravity KDTree", active=True):
        self.name = name
        self.environment = environment
        self.G = G
        self.softening_length = softening_length
        self.active = active

    def calculate_forces(self):
        if not self.active:
            return

        # Create a list of particle positions
        positions = np.array([particle.position for particle in self.environment.particles])

        # Create a KDTree for efficient nearest neighbor search
        tree = KDTree(positions)

        for i, particle in enumerate(self.environment.particles):
            # Query the tree for the nearest neighbors of the current particle
            distances, indices = tree.query(particle.position, len(self.environment.particles))

            for distance, index in zip(distances, indices):
                if distance > 0:  # Ignore the particle itself
                    j = self.environment.particles[index]
                    r = j.position - particle.position
                    epsilon = 1e-6
                    denominator = np.linalg.norm(r) + self.softening_length + epsilon
                    particle.force = particle.force + self.G * particle.mass * j.mass * r / denominator**3

    def update(self):
        self.calculate_forces()
        # Additional update logic if needed
