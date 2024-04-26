import PhysEng as pe
import numpy as np
from PhysEng.Bodies.spring_link import Spring_link


env = pe.Environment()
env.simulation_width = [0,2000]
env.simulation_height = [0,2000]


#adding PARTICLES -------

def velocity_field(particle):
    #sine wave 
    particle.force[0] += 100*np.sin((particle.position[0]))
    
    particle.force[1] += 100*np.sin(particle.position[0])
    pass

env.add_body(pe.AnchoredCloth(corner=[750,500,0], mass=20, k=900,damping=0.8, N_width=10,N_length=20, cell_size=40, environment=env))


env.add_field(velocity_field, active=False)

env.add_uniform_acceleration_field(a=[0.0, 98,0.0], active=False, name="Gravity")
env.add_uniform_force_field(F=[200, 400,0], active=False, name="Wind")
env.add_spring(softening_length=0)



vis =pe.Visualize(env, render_video=True, output="test.mp4", output_fps=30, output_framelimit=900)
vis.simulationheight = [0, 2000]
vis.simulationwidth = [0, 2000]
vis.show()
