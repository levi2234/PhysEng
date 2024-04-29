import pygame as pg


from PhysEng.Environment import Environment
from PhysEng.Visualize import Visualize
from PhysEng.Visualize.pygametoxy import pygame_to_xy

import PhysEng as pe
import numpy as np
x = Environment()
vis =Visualize(x, render_video=True, output="test.gif", output_fps=30, output_framelimit=900, enable_rendering=True)

def velocity_field_lorenz_centered(particle, sigma=10, rho=28, beta=8/3, center_x=0, center_y=0, active=True,**kwargs):
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
    

def apply_mobius_strip_force(particle, strip_width=4, center=[0, 0, 0], radius=40, strength=100, active=True, **kwargs):
    """
    Applies a force to a particle to simulate movement along a Möbius strip.

    Parameters:
    - particle: The particle object, which must have a position and force attributes.
    - strip_width: The width of the Möbius strip.
    - center: The center point of the Möbius strip in 3D space.
    - radius: The radius from the center to the middle of the strip.
    - strength: The strength of the force applied to keep the particle on the strip.
    - active: If False, the force field is not applied.
    """
    if not active:
        return

    # Calculate the particle's position relative to the center
    x, y, z = particle.position[0] - center[0], particle.position[1] - center[1], particle.position[2] - center[2]
    
    # Convert Cartesian coordinates to cylindrical coordinates
    rho, phi = np.sqrt(x**2 + y**2), np.arctan2(y, x)

    # Calculate the height adjustment based on the phi angle, to introduce the twist of the Möbius strip
    twist_factor = np.sin(phi / 2) * strip_width

    # Determine the target position on the Möbius strip
    target_x = (radius + twist_factor * np.cos(phi / 2)) * np.cos(phi)
    target_y = (radius + twist_factor * np.cos(phi / 2)) * np.sin(phi)
    target_z = twist_factor * np.sin(phi / 2)

    # Calculate the force needed to move the particle towards its target position
    force_x = strength * (target_x - x)
    force_y = strength * (target_y - y)
    force_z = strength * (target_z - z)

    # Apply the force to the particle
    particle.force[0] += force_x
    particle.force[1] += force_y
    particle.force[2] += force_z

    
def velocity_field_rossler_centered(particle, a=0.2, b=0.2, c=5.7, center_x=0, center_y=0, active=True,**kwargs):
    # Adjust particle.position by subtracting the center coordinates before calculations
    if not active:
        return
    x, y, z = particle.position[0] - center_x, particle.position[1] - center_y, particle.position[2]
    
    # Rössler attractor equations
    dx_dt = -y - z
    dy_dt = x + a * y
    dz_dt = b + z * (x - c)
    
    # Apply the force adjustments, and then add the center offsets to x and y forces to recenter the effect
    particle.velocity[0] = dx_dt + center_x - particle.position[0]
    particle.velocity[1] = dy_dt + center_y - particle.position[1]
    particle.velocity[2] = dz_dt  # Z doesn't need centering for 2D viewports; adjust if needed for 3D

def velocity_field_sine_wave(particle, amplitude=100, frequency=4, wavespeed=40, center_x=0, center_y=0, active=True,**kwargs):
    if not active:
        return
    particle.position[0] += center_x
    particle.position[1] += center_y
    particle.velocity[0] = amplitude * np.sin(frequency * particle.position[1]) + wavespeed
    particle.velocity[1] = amplitude * np.sin(frequency * particle.position[0]) + wavespeed
    particle.position[0] -= center_x
    
import numpy as np

    

def apply_gravitational_well_force(particle, center=[20, 20, 20], strength=0.1, damping=0.1, active=True, **kwargs):
    """
    Applies a gravitational well force to a particle, attracting it towards a central point,
    with an optional damping force to simulate friction or resistance, enhancing stability.

    Parameters:
    - particle: The particle object, which must have a position and velocity attributes.
    - center: The coordinates of the gravitational well's center in 3D space.
    - strength: The strength of the gravitational attraction. Higher values pull particles more strongly.
    - damping: The damping factor applied to the particle's velocity, simulating friction to stabilize motion.
    - active: If False, the force field is not applied.
    """
    if not active:
        return

    # Calculate the vector from the particle to the center
    vector_to_center = np.array(center) - np.array(particle.position)

    # Calculate the distance to the center to scale the gravitational force
    distance = np.linalg.norm(vector_to_center)

    # Normalize the vector to center
    if distance > 0:
        direction = vector_to_center / distance
    else:
        direction = np.array([0, 0, 0])

    # Calculate the gravitational force towards the center
    force_magnitude = strength * particle.mass
    gravitational_force = direction * force_magnitude

    # Apply damping to the particle's velocity to prevent excessive acceleration and ensure stability
    damping_force = -np.array(particle.velocity) * damping

    # Update the particle's force attribute
    particle.force = particle.force +  gravitational_force + damping_force




def apply_gravitational_well_force_cursor(particle, center=[20, 20, 0], strength=100, damping=0.1, active=True, **kwargs):
    """
    Applies a gravitational well force to a particle, attracting it towards a central point,
    with an optional damping force to simulate friction or resistance, enhancing stability.

    Parameters:
    - particle: The particle object, which must have a position and velocity attributes.
    - center: The coordinates of the gravitational well's center in 3D space.
    - strength: The strength of the gravitational attraction. Higher values pull particles more strongly.
    - damping: The damping factor applied to the particle's velocity, simulating friction to stabilize motion.
    - active: If False, the force field is not applied.
    """
    center[0], center[1] = pygame_to_xy(vis, pg.mouse.get_pos()[0], pg.mouse.get_pos()[1])
    if not active:
        return

    # Calculate the vector from the particle to the center
    vector_to_center = np.array(center) - np.array(particle.position)

    # Calculate the distance to the center to scale the gravitational force
    distance = np.linalg.norm(vector_to_center)

    # Normalize the vector to center
    if distance > 0:
        direction = vector_to_center / distance
    else:
        direction = np.array([0, 0, 0])

    # Calculate the gravitational force towards the center
    force_magnitude = strength * particle.mass
    gravitational_force = direction * force_magnitude

    # Apply damping to the particle's velocity to prevent excessive acceleration and ensure stability
    damping_force = -np.array(particle.velocity) * damping

    # Update the particle's force attribute
    particle.force = particle.force +  gravitational_force + damping_force
    
    
x.dt = 0.01

#------- adding INTEGRATOR
x.set_integrator(pe.verlet())

#adding PARTICLES -------
for _ in range(2000):
    x.add_particle(pe.Particle(mass = np.random.randint(1,15), position = np.random.rand(3) * 200 -100, radius=2)) 


x.add_field(velocity_field_lorenz_centered, active=False, name="Lorenz Attractor")
x.add_field(velocity_field_rossler_centered, active=False, name="Rossler Map")
x.add_field(velocity_field_sine_wave, active=False, name="Sine Wave")
x.add_field(apply_mobius_strip_force, active=False, name="Mobius Strip")
x.add_field(apply_gravitational_well_force, active=False, name="Grav Well")
x.add_field(apply_gravitational_well_force_cursor, active=False, name="Grav Well Cursor")



vis.simulationheight = [-100, 100]
vis.simulationwidth = [-100, 100]
vis.show()
