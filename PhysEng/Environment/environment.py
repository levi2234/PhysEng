from PhysEng.Bodies.spring_link import Spring_link
from matplotlib import pyplot as plt
from PhysEng.Integrators import euler
from  PhysEng.Collisions.ParticleParticleCollision import ParticleParticleCollision


class Environment():
    
    def __init__(self) -> None:
        self. __name__ = "Environment"
        self. __version__ = "0.0.7"
        
        self.particles = [] #particles
        self.bodies = [] #bodies
        self.forces = [] #forces	
        self.spring_links = [] #spring links between particles
        self.collision_resolvers = []#collision detectors
        
        self.time = 0 #seconds
        self.dt = 0.01 #seconds
        self.dimensions = 3 #dimensions
        self.integrator = euler(self) #integrator set to ph4 by default
        
        
        
        
        print(r"""
 ______ _                _____                       _                _                      _____    
| ___ \ |              |  ___|                     | |              (_)                    |  ___|   
| |_/ / |__  _   _ ___ | |__ _ __   __ _   ______  | |     _____   ___  __   ____ _ _ __   | |__ ___ 
|  __/| '_ \| | | / __||  __| '_ \ / _` | |______| | |    / _ \ \ / / | \ \ / / _` | '_ \  |  __/ __|
| |   | | | | |_| \__ \| |__| | | | (_| |          | |___|  __/\ V /| |  \ V / (_| | | | | | |__\__ \
\_|   |_| |_|\__, |___/\____/_| |_|\__, |          \_____/\___| \_/ |_|   \_/ \__,_|_| |_| \____/___/
              __/ |                 __/ |                                                           
""" + "\n" + f"Welcome to the PhysEng Environment Version {self.__version__}")
    


    def add_particle(self, particle):
        if (len(particle.position) != self.dimensions or len(particle.velocity) != self.dimensions):
            raise ValueError("The particle's position and velocity must have the same number of dimensions as the environment")
        particle.environment = self
        self.particles.append(particle)
        
    def add_anchor(self, anchor):
        anchor.environment = self
        self.particles.append(anchor)
        
    def add_body(self, body):
        body.environment = self
        self.bodies.append(body)
        
    #set integrator functions ----------------------------------------
    def set_integrator(self, integrator):
        integrator.environment = self
        self.integrator = integrator
        
    #add force functions ----------------------------------------
    def add_force(self, force, name=None):
        force.environment = self
        if name:
            force.name = name
        self.forces.append(force)
        
    def add_spring(self, softening_length=0, active=True, name=None):
        from PhysEng.Forces.spring import Spring
        self.add_force(Spring(self, softening_length=softening_length, active=active), name=name)
        
    def add_uniform_force_field(self, F=[0,-981,0], active=True, name=None):
        from PhysEng.Forces.uniform_force_field import UniformForceField
        self.add_force(UniformForceField(self, F, active=active), name=name)
        
    def add_uniform_acceleration_field(self, a=[0,-9.81,0], active=True, name=None):
        from PhysEng.Forces.uniform_acceleration_field import UniformAccelerationField
        self.add_force(UniformAccelerationField(self, a, active=active), name=name)
        
    def add_gravity(self, G= 6.67430e-11, softening_length=0, active=True, name=None):
        from PhysEng.Forces.gravity import Gravity
        self.add_force(Gravity(self, G, softening_length=softening_length, active=active), name=name)
        
    def add_coulomb(self, k=8.9875517873681764e9, active=True, name=None):
        from PhysEng.Forces.coulomb import Coulomb
        self.add_force(Coulomb(self, k, active=active),name=name)
        
    def add_drag(self, active=True, name=None):
        from PhysEng.Forces.drag import Drag
        self.add_force(Drag(self, active=active), name=name)
        
    def add_field(self, field_function, active=True, name=None, **kwargs): 
        from PhysEng.Forces.custom_field import CustomField
        self.add_force(CustomField(field_function, active=active, **kwargs), name=name)
        
    def add_spring_link(self, Spring_link):

        Spring_link.environment = self
        self.spring_links.append(Spring_link)
        
    def add_springed_particles(self, particle1, particle2, k=1, l0=1, damping=0.1):
        spring_link = Spring_link(particle1, particle2, k, l0, damping=damping)
        self.add_spring_link(spring_link)
        self.add_particle(particle1)
        self.add_particle(particle2)
        
    #update force functions ----------------------------------------
    def update(self):
        self.last_state =None
        for i in self.forces:
            i.update()
        
        self.integrator.update()
        

        #reset forces of all particles

        
        self.time += self.dt
        
        
    #run simulation functions ----------------------------------------

    def step(self):
        self.update()
        
    
    def run(self, steps):
        for i in range(steps):
            self.step()
    
    def show(self) -> None:
        for i in self.particles:
            plt.scatter(i.position[0], i.position[1], c="red")
        plt.show()

    def __str__(self) -> str:
        return(self.__name__ + " " + self.__version__)
        
    
    