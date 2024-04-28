# <img src="README/logo.png" width="100" height="100"> PhysEng - A 95% Python Physics Engine

PhysEng is a fully Python-based physics engine designed for simulating physical systems in 3D. It's user-friendly and highly flexible, enabling the creation of complex simulations with ease.

![A Simple Demonstration of Multiple Velocity and Force Fields](README/Demo.gif)


## Features

* **Particle Simulation**: Create and simulate particles with mass, charge, and velocity.
* **Soft Body Simulation**: Create and simulate soft bodies such as balls and anchored cloth.
* **Physics Fields**: Add physics fields such as gravity, drag, and electrostatic fields.
* **Collision Detection**: Detect and resolve collisions between particles and soft bodies.
* **Visualization**: Visualize and interact with the simulation in real-time.
* **Customization**: Customize the simulation with custom physics fields and soft bodies.




## Getting Started
  ### Installation

Follow these steps to install PhysEng:

1. **Clone the repository**.
2. **Install the library and dependencies** using pip:


  This library is verified to run on Python 3.10 and above. 
  While this library is a standalone library, it is recommended to install the following dependencies to ensure compatibility with the library. The phyiscs engine is completely written in python however it requires some dependancies to visualize and render the simulation.
  ```bash
  pip install ffmpeg-python==0.2.0
  pip install numpy==1.26.4
  pip install pygame==2.5.2
  pip install ffmpeg-python==0.2.0
  pip install scipy==1.10.1
  pip install matplotlib==3.5.1
  pip install imageio==2.33.1
  pip install imageio-ffmpeg==0.4.9
  
  ```	

## Usage

  ### First Simulation

  * Step 1: Create a new Python file and import the necessary libraries

  ```python
import pygame as pg
import PhysEng as pe
from PhysEng.Environment import Environment
from PhysEng.Visualize import Visualize
from PhysEng.Visualize.pygametoxy import pygame_to_xy
import numpy as np
  ```

  * Step 2: Create a new environment and add some particles

  ```python
#.....Previous code
env = Environment()
  ```

  * Step 3 : Create the visualization so we can see and interact with the simulation at runtime.

  ```python
#.....Previous code
new_visualization = Visualize(env) #pass the environment
  ```

  * Step 4:  ADD PARTICLES The Library has a few built in basic objects such as particles, balls and anchored cloth. You can create these objects and add them to the environment. As such we also have a few built in physics fields such as gravity, drag and electrostatic fields. 

  ```python
#.....Previous code 


 from PhysEng.Bodies import Particle
 

  #adding a few particle
  for _ in range(2000):
      env.add_particle(pe.Particle(mass = np.random.randint(1,15), position = np.random.rand(3) * 200 -100, radius=2)) 


  #adding fields
  env.add_uniform_acceleration_field(name='gravity', a=[0, 9.8, 0])
  env.add_drag(name='drag')
  
  ```

  * Step 5: Run the simulation

  ```python
  #.....Previous code
  new_visualization.simulationheight = [0, 50]
  new_visualization.simulationwidth = [-100, 100]
  new_visualization.show()
  ```

  * Step 6: Watch your simulation run!
  ![AA Simple Demonstration of Multiple Velocity and Force fields](README/Demo2.gif)


<!-- 

  ## Bodies & Particles

  * **Particle**
       ```python
        from PhysEng.Bodies import Particle
        
        position = [1,4,7] # [x,y,z] in meters          Default = [0,0,0]
        velocity = [0,0,0] # [vx,vy,vz] in m/s          Default = [0,0,0]
        radius = 0.1 # in meters                        Default = 0
        force = [0,0,0] # [fx,fy,fz] in Newtons         Default = [0,0,0]
        mass = 1 # in kg                                Default = 1
        charge = 0 # in Coulombs                        Default = 0
        drag_coefficient = 0.47 # dimensionless         Default = 0
        fixed = False #Boolean (fixes pos and vel)      Default = False
        environment = None #Environment class           Default = None

        new_particle = Particle(position, mass, velocity, radius=0, charge, drag_coeff, name, environment, **kwargs)
    ```
  * **Ball**
      ```python
      from PhysEng.Bodies.SoftBodies import Ball
      
      environment = None   
      position = [1,4,7] # [x,y,z] in meters          Default = [0,0,0]
      velocity = [0,0,0] # [vx,vy,vz] in m/s          Default = [0,0,0]
      radius = 0.1       # in meters                  Default = 100
      force = [0,0,0]    # [fx,fy,fz] in Newtons      Default = [0,0,0]
      elasticity = 0     # dimensionless              Default = 0
      force = [0, 0,0]   # [fx,fy,fz] in Newtons      Default = [0,0,0]
      drag = drag_coeff  # dimensionless              Default = 0
      number_of_particles = N_particles # int         Default = 200
      name = name        # string                     Default = 'Ball'
      charge = charge    # in Coulombs                Default = 0
      damping = damping  # dimensionless              Default = 0.4

      new_softbody_ball = Ball(position, mass, velocity, radius, charge,drag_coeff,elasticity, N_particles, damping, name,environment **kwargs)
      ```

  * **Anchored Cloth**
      ```python
      from PhysEng.Bodies.SoftBodies import AnchoredCloth

      N_width = N_width          #int                     #default = 10
      N_length = N_length        #int                     #default = 10
      cell_size = cell_size      #float in m              #default = 1
      corner = corner            #[x,y,z] in meters       #default = [0,0,0]
      mass = mass                #float in kg             #default = 1
      k =k                       #float in N/m            #default = 100
      damping = damping          #float dimensionless     #default = 0.4
      drag = drag                #float drag coefficient  #default = 0
      charge = charge            #float in Coulombs       #default = 0
      environment = environment  #Environment class       #default = None

      new_anchored_cloth = AnchoredCloth(corner, mass, k, damping, drag,charge, cell_size, N_width, N_length, environment)
      ``` 
    
  ## Physics

  * [N-body gravity]() (3D N body gravity simulation $N^2$) 

 -->
