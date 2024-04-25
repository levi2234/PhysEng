import PhysEng as pe
import numpy as np
from PhysEng.Bodies.spring_link import Spring_link


x = pe.Environment()
x.simulation_width = [0,2000]
x.simulation_height = [0,2000]


#adding PARTICLES -------

def velocity_field(particle):
    #sine wave 
    particle.force[0] += 100*np.sin((particle.position[0]))
    
    particle.force[1] += 100*np.sin(particle.position[0])
    pass

x.add_body(pe.AnchoredCloth(corner=[750,500,0], mass=20, k=900,damping=0.8, N_width=10,N_length=20, cell_size=40, environment=x))


x.add_field(velocity_field, active=False)

x.add_uniform_acceleration_field(a=[0.0, 98,0.0], active=False, name="Gravity")
x.add_uniform_force_field(F=[200, 400,0], active=False, name="Wind")
x.add_spring(softening_length=0)



vis =pe.Visualize(x)
vis.simulationheight = [0, 2000]
vis.simulationwidth = [0, 2000]
vis.show()
