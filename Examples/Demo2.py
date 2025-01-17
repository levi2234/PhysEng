import PhysEng as pe
from PhysEng.Environment import Environment
from PhysEng.Visualize import Visualize
import numpy as np
env = Environment()
new_visualization = Visualize(env, output="Demo2.gif", enable_rendering=True) #pass the environment
environment = env #Environment class           Default = None

for _ in range(2000):
    env.add_particle(pe.Particle(mass = np.random.randint(1,15), position = np.random.rand(3) * 200 -100, radius=2)) 


#adding fields
env.add_uniform_acceleration_field(name='gravity', a=[0, 9.8, 0])
env.add_drag(name='drag')

new_visualization.simulationheight = [-100, 100]
new_visualization.simulationwidth = [-100, 100]


#run the simulation
new_visualization.show()