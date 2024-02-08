# PhysEng


  ## Environment

  * **Environment Params**
       ```python
        from physeng.environment import Environment

        new_environment = Environment()
    ```

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


