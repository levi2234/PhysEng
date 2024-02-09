import pygame as pg
import PhysEng as pe
from PhysEng.Visualize import Visualize

import PhysEng as pe
import numpy as np


def velocity_field_lorenz_centered(particle, sigma=10, rho=28, beta=8/3, center_x=0, center_y=0, active=True):
    # Adjust particle.position by subtracting the center coordinates before calculations
    if not active:
        return
    x, y, z = particle.position[0] - center_x, particle.position[1] - center_y, particle.position[2]
    
    # Lorenz attractor equations
    dx_dt = sigma * (y - x)
    dy_dt = x * (rho - z) - y
    dz_dt = x * y - beta * z
    
    # Apply the force adjustments, and then add the center offsets to x and y forces to recenter the effect
    particle.velocity[0] = (dx_dt + center_x - particle.position[0])
    particle.velocity[1] = dy_dt + center_y - particle.position[1]
    particle.velocity[2] = dz_dt  # Z doesn't need centering for 2D viewports; adjust if needed for 3D


x = pe.Environment()

#------- adding INTEGRATOR
x.set_integrator(pe.verlet())

#adding PARTICLES -------
for _ in range(2000):
    x.add_particle(pe.Particle(mass = np.random.randint(1,15), position = np.random.rand(3) * 60, radius=2)) 

x.add_field(velocity_field_lorenz_centered, active=True, name="Lorenz Attractor")


vis =Visualize(x)
vis.simulationheight = [-40, 40]
vis.simulationwidth = [-40, 40]
vis.show()
