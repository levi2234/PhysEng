from PhysEng.Bodies.particle import Particle
from PhysEng.Bodies.spring_link import Spring_link
import numpy as np

class AnchoredCloth():
    """
    Represents an anchored cloth object in a physics simulation.
    Parameters:
        corner (list): The coordinates of the top-left corner of the cloth.
        mass (float): The mass of each particle in the cloth.
        k (float): The spring constant of the cloth's springs.
        damping (float): The damping coefficient of the cloth's springs.
        drag (float): The drag coefficient of the cloth's particles.
        charge (float): The charge of the cloth's particles.
        cell_size (float): The size of each cell in the cloth's mesh.
        N_width (int): The number of cells in the width direction of the cloth's mesh.
        N_length (int): The number of cells in the length direction of the cloth's mesh.
        environment (object): The environment in which the cloth exists.
    
    Attributes:
        All paramters are also attributes of the class
        particles (list): The list of particles in the cloth.
        spring_links (list): The list of spring links in the cloth.
        clothmesh (numpy.ndarray): The mesh representation of the cloth.
        springs (list): The list of springs in the cloth.
    """
    
    def __init__(self, corner=[0,0,0], mass=1, k=1, damping=0, drag=0.2, charge=0, cell_size=1, N_width=30, N_length=30, environment=None):
        self.__name__ = "Anchored Cloth"
        
        self.N_width = N_width
        self.N_length = N_length
        self.cell_size = cell_size
        self.corner = corner
        self.mass = mass
        self.k = k
        self.damping = damping
        self.charge = charge
        self.drag = drag
        self.particles = []
        self.spring_links = []
        self.environment = environment
        self.create_mesh()
        self.create_springs()
        
    def create_mesh(self):
        """
        Creates the mesh representation of the cloth by initializing particles and fixing the top row.
        """
        self.clothmesh = np.zeros((self.N_width, self.N_length), dtype=Particle)
        for i in range(self.N_width):
            for j in range(self.N_length):
                particle = Particle([self.corner[0] + i*self.cell_size, self.corner[1]+j*self.cell_size, self.corner[2]], mass=self.mass, color=[255,255,255] ,environment=self.environment)
                self.particles.append(particle)
                self.clothmesh[i,j] = particle
                
        # Fix top row
        for i in range(self.N_width):
            self.clothmesh[i,0].fixed = True
 
        for i in self.particles:
            self.environment.add_particle(i)
    
    def create_springs(self):
        """
        Creates the spring links between particles in the cloth's mesh.
        """
        self.springs = []
        for i in range(self.N_width):
            for j in range(self.N_length):
                tolinkparticle = self.clothmesh[i,j]
                
                # Link with left neighbour
                if i-1 >= 0:
                    spring_link = Spring_link(tolinkparticle,self.clothmesh[i-1,j], k=self.k, l0=self.cell_size, damping=self.damping)
                    self.spring_links.append(spring_link)
                
                # Link with top neighbour
                if j-1 >= 0:
                    spring_link = Spring_link(tolinkparticle,self.clothmesh[i,j-1], k=self.k, l0=self.cell_size, damping=self.damping)
                    self.spring_links.append(spring_link)
        
        for i in self.spring_links:
            self.environment.add_spring_link(i)
                    
