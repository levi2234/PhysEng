import cupy as cp

class Gravity_Cuda:
    """
    Represents a gravity force in a given environment with GPU acceleration.
    """

    def __init__(self, environment, G=6.67430e-11, softening_length=0, name="Gravity_Cuda", active=True):
        """
        Initializes a Gravity_Cuda object.

        Parameters:
        - environment: The environment in which the gravity force acts.
        - G: The gravitational constant. Default value is 6.67430e-11.
        - softening_length: The softening length used to avoid singularities. Default value is 0.
        - name: The name of the gravity force. Default value is "Gravity_Cuda".
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
        if not self.active:
            return

        particles = self.environment.particles

        # Extract positions and masses from the particles
        positions = cp.array([p.position for p in particles], dtype=cp.float32)
        masses = cp.array([p.mass for p in particles], dtype=cp.float32)

        # Number of particles
        n = len(particles)

        # Compute pairwise differences
        diff = positions[:, cp.newaxis, :] - positions[cp.newaxis, :, :]  # Shape: (n, n, 3)

        # Compute distances with softening
        distances = cp.linalg.norm(diff, axis=2) + self.softening_length  # Shape: (n, n)

        # Avoid division by zero or self-interaction
        mask = cp.eye(n, dtype=cp.bool_)
        distances[mask] = cp.inf

        # Compute gravitational force magnitudes
        force_magnitudes = -self.G * masses[:, cp.newaxis] * masses[cp.newaxis, :] / distances**3  # Add negative sign for attraction

        # Compute force vectors
        forces = (force_magnitudes[:, :, cp.newaxis] * diff).sum(axis=1)  # Shape: (n, 3)


        # Update particle forces
        for i, particle in enumerate(particles):
            particle.force = particle.force.astype(cp.float64)  # Ensure float64 for consistency
            particle.force += cp.asnumpy(forces[i])

