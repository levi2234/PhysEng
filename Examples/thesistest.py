import pygame as pg
import PhysEng as pe
import numpy as np
from PhysEng.Environment import Environment
from PhysEng.Visualize import Visualize
from PhysEng.Visualize.pygametoxy import pygame_to_xy
import numpy as np
env = Environment()
new_visualization = Visualize(env, output="Demo2.gif", enable_rendering=True) #pass the environment

from PhysEng.Bodies import Particle
environment = env #Environment class           Default = None

coordinates = np.load('coordinates.npy') #MPC
velocities = np.load('velocities.npy') #KM/s 
#convert to MPC/s
velocities = velocities * 3.24078e-20

for c,v in zip(coordinates, velocities):
    particle = Particle(position=c, velocity=v,  mass=1, radius=1, color=(255, 0, 0))
    env.add_particle(particle)

#adding fields
# env.add_gravity_KDtree(name='gravity_KDtree', G=40.1)
env.add_uniform_acceleration_field(name='gravity_uniform', a=[0, 0.1, 0])
env.add_drag(name='drag')

new_visualization.simulationheight = [np.min(coordinates[:,1]), max(coordinates[:,1])]
new_visualization.simulationwidth = [np.min(coordinates[:,0]), max(coordinates[:,0])]

env.dt = 10e13
#run the simulation
new_visualization.show()