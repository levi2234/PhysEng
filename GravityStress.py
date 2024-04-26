import pygame as pg
import PhysEng as pe
from PhysEng.Visualize import Visualize
from astropy import constants as c
from astropy import units as u
import numpy as np



x = pe.Environment()
vis =Visualize(x, render=True)



for _  in range(100):
    #randomly place particles
    x.add_particle(pe.Particle(position=[np.random.uniform(0,20),np.random.uniform(0,20),0], mass=1, radius=3, color=[255,255,255], name="Particle", velocity=[0, 0, 0]))



#add the gravitational force to the environment
x.add_gravity(G=0.001, softening_length=0.1)
x.add_gravity_KDtree(G=0.011, softening_length=0.1)

vis.show()