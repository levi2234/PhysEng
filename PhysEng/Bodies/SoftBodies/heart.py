
from PhysEng.Bodies.particle import Particle
from PhysEng.Bodies.spring_link import Spring_link
import numpy as np
import matplotlib.pyplot as plt
import numpy as np

class Heart():
    def __init__(self, position=[0,0,0], mass =1, velocity=[0,0,0], radius=100, charge =0,drag_coeff=0,elasticity=0, N_particles=20, damping=0.4, name="",environment=None)->None:
        
        self.environment = environment
        self.position = position
        self.radius = radius
        self.mass = mass
        self.elasticity = elasticity
        self.velocity = velocity
        self.force = [0, 0,0]
        self.drag = drag_coeff
        self.number_of_particles = N_particles
        self.name = name
        self.charge = charge
        self.damping = damping
        self.particles=[]
        self.spring_links=[]
        self.construct_heart()
        



    def heart_3d(self,x,y,z):
        return (x**2+(9/4)*y**2+z**2-1)**3-x**2*z**3-(9/80)*y**2*z**3
    
    def plot_implicit(self,fn, bbox=(-1.5, 1.5)):
        ''' create a plot of an implicit function
        fn  ...implicit function (plot where fn==0)
        bbox ..the x,y,and z limits of plotted interval'''
        xmin, xmax, ymin, ymax, zmin, zmax = bbox*3
        A = np.linspace(xmin, xmax, 30) # resolution of the contour
        B = np.linspace(xmin, xmax, 10) # number of slices
        A1, A2 = np.meshgrid(A, A) # grid on which the contour is plotted
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        coordinates = [] # list to save the coordinates

        for z in B: # plot contours in the XY plane
            X, Y = A1, A2
            Z = fn(X, Y, z)
            cset = ax.contour(X, Y, Z+z, [z], zdir='z', colors=('r',))
            # [z] defines the only level to plot for this contour for this value of z
            for seg in cset.allsegs[0]:
                coordinates.extend([(x, y, z) for x, y in zip(seg[:, 0], seg[:, 1])])

        for y in B:  # plot contours in the XZ plane
            X, Z = A1, A2
            Y = fn(X, y, Z)
            cset = ax.contour(X, Y+y, Z, [y], zdir='y', colors=('red',))
            for seg in cset.allsegs[0]:
                    coordinates.extend([(x, y, z) for z, x in zip(seg[:, 0], seg[:, 1])])

        for x in B: # plot contours in the YZ plane
            Y, Z = A1, A2
            X = fn(x, Y, Z)
            cset = ax.contour(X+x, Y, Z, [x], zdir='x',colors=('red',))
            for seg in cset.allsegs[0]:
                coordinates.extend([(x, y, z) for y, z in zip(seg[:, 0], seg[:, 1])])
        coordinates = np.array(coordinates)
        #make z axis the y axis
        coordinates[:,1], coordinates[:,2] = coordinates[:,2], coordinates[:,1].copy()
       #rotate heart 180 degrees in x and y plane
        coordinates[:,1] = coordinates[:,1] * -1
        return np.array(coordinates)
    
    def nearest_neighbours(self, particle, n=3):
        #find nearest neighbours
        distances = []
        for i in self.particles:
            distances.append((i, np.linalg.norm(particle.position - i.position)))
        distances = sorted(distances, key=lambda x: x[1])
        return distances[:n]
    
    def construct_heart(self):
        points = self.plot_implicit(self.heart_3d)
        for i in points:
            self.particles.append(Particle(position=i, mass=self.mass/self.number_of_particles, velocity=self.velocity, radius=2, charge=self.charge, drag_coeff=self.drag, name=self.name, environment=self.environment))
        
        for i in self.particles:
            for j in self.nearest_neighbours(i, 6):
                if i != j[0]:
                    l0 = np.linalg.norm(i.position - j[0].position)
                    self.spring_links.append(Spring_link(i, j[0], l0=l0, k=400, damping=0.5))
                    
        for i in self.particles:
            self.environment.add_particle(i)
        
        for i in self.spring_links:
            self.environment.add_spring_link(i)
        

            
            