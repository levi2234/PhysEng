import PhysEng as pe
import numpy as np
from PhysEng.Bodies.spring_link import Spring_link


x = pe.Environment()
x.dt = 0.1


#------- adding INTEGRATOR
x.set_integrator(pe.verlet())


x.add_body(pe.Heart(position=[1000, 1000, 0], mass = 20, velocity=[0,0,0], radius=300, charge =0,drag_coeff=3,elasticity=0, N_particles=200, damping=0.4, name="",environment=x))   


def velocity_field(particle):
    # vortex field

    x, y, z = particle.position
    vx = y
    vy = -x
    vz = 0
    particle.velocity = 0.5*np.array([vx, vy, vz])
    

x.add_field(velocity_field, active=False)
    
#x.add_gravity(G=100000, softening_length=5, active=False)

x.add_uniform_force_field(F=[200, 400,0], active=False, name="Wind")
x.add_spring(softening_length=1)
# x.add_uniform_acceleration_field(a=[0.0, 98,0.0])


vis =pe.Visualize(x)
vis.simulationheight = [-3,3]
vis.simulationwidth = [-3,3]
vis.show()
