from PhysEng.Bodies.spring_link import Spring_link
from PhysEng.Integrators import euler
from  PhysEng.Collisions.ParticleParticleCollision import ParticleParticleCollision


class Environment():
    
    def __init__(self, particles=[], bodies=[], forces=[], spring_links=[], collision_resolvers=[], time=0, dt=0.01, dimensions=3, integrator=euler) -> None:
        """
        Initializes an instance of the Environment class.

        Args:
            particles (list, optional): List of particles. Defaults to an empty list.
            bodies (list, optional): List of bodies. Defaults to an empty list.
            forces (list, optional): List of forces. Defaults to an empty list.
            spring_links (list, optional): List of spring links between particles. Defaults to an empty list.
            collision_resolvers (list, optional): List of collision detectors. Defaults to an empty list.
            time (float, optional): Time in seconds. Defaults to 0.
            dt (float, optional): Time step in seconds. Defaults to 0.01.
            dimensions (int, optional): Number of dimensions. Defaults to 3.
            integrator (function, optional): Integrator function. Defaults to euler.

        Returns:
            None
        """
        self.__name__ = "Environment"
        self.__version__ = "0.1.1"
        
        self.particles = particles
        self.bodies = bodies
        self.forces = forces
        self.spring_links = spring_links
        self.collision_resolvers = collision_resolvers
        
        self.time = time
        self.dt = dt
        self.dimensions = dimensions
        self.integrator = integrator(self)
        
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
        """
        Adds a Particle Object to the environment.

        Args:
            particle (Particle): The particle to be added.

        Raises:
            ValueError: If the particle's position or velocity has a different number of dimensions than the environment.

        """
        if (len(particle.position) != self.dimensions or len(particle.velocity) != self.dimensions):
            raise ValueError("The particle's position and velocity must have the same number of dimensions as the environment")
        particle.environment = self
        self.particles.append(particle)
        
    def add_anchor(self, anchor):
        """
        Adds an anchor to the environment.
        Is a wrapper for the add_particle function to make the code more readable and intuitive.

        Parameters:
        anchor (Anchor article): The anchor particle to be added.

        Returns:
        None
        """
        anchor.environment = self
        self.particles.append(anchor)
        
    def add_body(self, body):
        """
        Adds a body to the environment.

        Parameters:
            body (Body): The body to be added.

        Returns:
            None
        """
        body.environment = self
        self.bodies.append(body)
        
    #set integrator functions ----------------------------------------
    def set_integrator(self, integrator):
        """
        Sets the integrator for the environment.

        Parameters:
            integrator (Integrator): The integrator to be set from PhysEng.Integrators.
            This can either be a premade integrator or a custom one 
            that adheres to the template of the premade integrators.

        Returns:
            None
        """
        integrator.environment = self
        self.integrator = integrator
        
    #add force functions ----------------------------------------
    def add_force(self, force, name=None):
        """
        Adds a force to the environment.

        Parameters:
            force (Force): The force to be added to the environment. These are objects that are either already provided in the Physeng.Forces folder
            or your own made forces that use a similar template.
            name (str, optional): The name of the force.

        Returns:
            None
        """
        force.environment = self
        if name:
            force.name = name
        self.forces.append(force)
        
    def add_spring(self, softening_length=0, active=True, name=None):
        from PhysEng.Forces.spring import Spring
        self.add_force(Spring(self, softening_length=softening_length, active=active), name=name)
        
    def add_uniform_force_field(self, F=[0,-981,0], active=True, name=None):
        """
        Adds a uniform force field to the environment.

        Parameters:
            F (list, optional): The force vector in Newtons. Defaults to [0, -981, 0].
            active (bool, optional): Specifies if the force field is active. Defaults to True.
            name (str, optional): The name of the force field. Defaults to None.
        """
        from PhysEng.Forces.uniform_force_field import UniformForceField
        self.add_force(UniformForceField(self, F, active=active), name=name)
        
    def add_uniform_acceleration_field(self, a=[0,-9.81,0], active=True, name=None):
        """
        Adds a uniform acceleration field to the environment.

        Parameters:
        - a: List of three numbers representing the acceleration vector in x, y, and z directions. Default is [0, -9.81, 0].
        - active: Boolean value indicating whether the field is active or not. Default is True.
        - name: Optional name for the field.

        Returns:
        None
        """
        from PhysEng.Forces.uniform_acceleration_field import UniformAccelerationField
        self.add_force(UniformAccelerationField(self, a, active=active), name=name)
        
    def add_gravity(self, G= 6.67430e-11, softening_length=0, active=True, name=None, use_gpu=False):
        
        if use_gpu:
            from PhysEng.Forces.gravity_cuda import Gravity_Cuda
            self.add_force(Gravity_Cuda(self, G, softening_length=softening_length, active=active), name=name)
            
        else:
            from PhysEng.Forces.gravity import Gravity
            self.add_force(Gravity(self, G, softening_length=softening_length, active=active), name=name)

        
    def add_coulomb(self, k=8.9875517873681764e9, active=True, name=None):
        from PhysEng.Forces.coulomb import Coulomb
        self.add_force(Coulomb(self, k, active=active),name=name)
        
    def add_drag(self, active=True, name=None):
        """
        Adds a drag force to the environment. The ammount of drag a particle experiences is set within the Particle Objects drag_coeff attribute.

        Parameters:
            active (bool): Whether the drag force is active or not. Default is True.
            name (str): Optional name for the drag force. Default is None.

        Returns:
            None
        """
        from PhysEng.Forces.drag import Drag
        self.add_force(Drag(self, active=active), name=name)
        
    # This needs to be made in pure python to keep true to the pure python approach
    # def add_gravity_KDtree(self, G=6.67430e-11, softening_length=0, active=True, name=None):
    #     from PhysEng.Forces.gravityKDtree import GravityKDTree
    #     self.add_force(GravityKDTree(self, G, softening_length=softening_length, active=active), name=name)
        
    def add_field(self, field_function, active=True, name=None, **kwargs): 
        """
        Add a custom field to the environment.

        Parameters:
            field_function (function): The function that defines the field. (See examples for custom field functions templates)
            active (bool, optional): Whether the field is active or not. Defaults to True.
            name (str, optional): The name of the field. Defaults to None.
            **kwargs: Additional keyword arguments to be passed to the CustomField constructor.
        """
        from PhysEng.Forces.custom_field import CustomField
        self.add_force(CustomField(field_function, active=active, **kwargs), name=name)
        
    def add_spring_link(self, Spring_link):
        """
        Adds a spring link to the environment.

        Args:
        - Spring_link: The spring link object to be added.

        Returns:
        None
        """
        Spring_link.environment = self
        self.spring_links.append(Spring_link)
        
    def add_springed_particles(self, particle1, particle2, k=1, l0=1, damping=0.1):
        """
        Adds a pair of particles connected by a spring link to the environment.

        Args:
            particle1 (Particle): The first particle in the spring link.
            particle2 (Particle): The second particle in the spring link.
            k (float, optional): The spring constant. Defaults to 1.
            l0 (float, optional): The equilibrium length of the spring. Defaults to 1.
            damping (float, optional): The damping coefficient of the spring. Defaults to 0.1.
        """
        spring_link = Spring_link(particle1, particle2, k, l0, damping=damping)
        self.add_spring_link(spring_link)
        self.add_particle(particle1)
        self.add_particle(particle2)
        
    #update force functions ----------------------------------------
    def update(self):
        """
        Updates the environment by updating the forces and the integrator.

        This method should be called to advance the simulation by one time step.

        Parameters:
            None

        Returns:
            None
        """
        self.last_state = None
        for i in self.forces:
            i.update()
        
        self.integrator.update()

        self.time += self.dt
        
        
    #run simulation functions ----------------------------------------

    def step(self):
        """
        Steps the simulation by one time step. Essentially is a wrapper around the Update function to comply with the naming conventions of similar libraries.
        """
        self.update()
        
    
    def run(self, steps):
        """
        Args: 
        Steps(int): The number of simulation steps of self.dt are to be run.

        Function:
        Applies the step function for the number of steps specified.
        """
        for i in range(steps):
            self.step()

    def __str__(self) -> str:
        return(self.__name__ + " " + self.__version__)
        
    
    