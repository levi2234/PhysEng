import pygame as pg
import PhysEng as pe
from PhysEng.Visualize import Visualize
from astropy import constants as c
from astropy import units as u



x = pe.Environment()
x.dt = 60*60*24
vis =Visualize(x)

vis.simulationheight = [-5e12, 5e12]
vis.simulationwidth = [-5e12, 5e12]

#create a particle as the sun

#orbital speed of solar system planets
#earth = 29.78 km/s
#jupiter = 13.07 km/s
#mars = 24.07 km/s
#venus = 35.02 km/s
#mercury = 47.87 km/s
#saturn = 9.69 km/s
#uranus = 6.81 km/s
#neptune = 5.43 km/s

sun = pe.Particle(position=[0,0,0], mass=1.989e30, radius=3, color=[255,255,0], name="Sun")
earth = pe.Particle(position=[1.496e11,0,0], mass=5.972e24, radius=3, color=[0,0,255], name="Earth", velocity=[0, 29780, 0]) 
jupiter = pe.Particle(position=[7.78e11,0,0], mass=1.898e27, radius=3, color=[255,165,0], name="Jupiter", velocity=[0, 13070, 0])   
# mars = pe.Particle(position=[2.28e11,0,0], mass=6.39e23, radius=3, color=[255,0,0], name="Mars", velocity=[0, 24070, 0])
# venus = pe.Particle(position=[1.08e11,0,0], mass=4.87e24, radius=3, color=[255,215,0], name="Venus", velocity=[0, 35020, 0])
mercury = pe.Particle(position=[5.79e10,0,0], mass=3.285e23, radius=3, color=[128,128,128], name="Mercury", velocity=[0, 47870, 0])
# saturn = pe.Particle(position=[1.43e12,0,0], mass=5.683e26, radius=3, color=[255,165,0], name="Saturn", velocity=[0, 9690, 0])
# uranus = pe.Particle(position=[2.87e12,0,0], mass=8.681e25, radius=3, color=[0,255,255], name="Uranus", velocity=[0, 6810, 0])
# neptune = pe.Particle(position=[4.5e12,0,0], mass=1.024e26, radius=3, color=[0,0,128], name="Neptune", velocity=[0, 5430, 0])

bodies = [sun, earth, jupiter, mercury]#, mars, venus, saturn, uranus, neptune]

for i in bodies:
    x.add_particle(i)   
    
    


#add the gravitational force to the environment
x.add_gravity(G=c.G.value, softening_length=0)
#x.add_gravity_oct(G=c.G.value, softening_length=0)

vis.show()