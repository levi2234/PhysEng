import PhysEng as pe
import numpy as np
from PhysEng.Bodies.spring_link import Spring_link


x = pe.Environment()
x.simulation_width = [0,2000]
x.simulation_height = [0,2000]


#------- adding INTEGRATOR
x.set_integrator(pe.verlet())


#adding PARTICLES -------
# anchor = pe.Anchor(position=[1000, 1000, 0], mass = 0, radius=3)
# x.add_anchor(anchor)
# particles = [pe.Particle(mass = 30, position = np.array([1001, 700, 0]), velocity = np.array([0, 0, 0]),radius=2), pe.Particle(mass = 30, position = np.array([999, 500, 0]), velocity = np.array([0, 0, 0]), radius=2)]
# x.add_particle(particles[0])
# x.add_particle(particles[1])
# spring1 = Spring_link(particles[0], particles[1], l0=200, k=900, damping=1)
# spring2 = Spring_link(anchor, particles[0], l0=300, k=900, damping=1)

# x.add_spring_link(spring1)
# x.add_spring_link(spring2)
#x.add_body(pe.Ball(position=[1000, 1000, 0], mass = 20, velocity=[0,0,0], radius=300, charge =0,drag_coeff=3,elasticity=0, N_particles=200, damping=0.3, name="",environment=x))
#x.add_particle(pe.Particle(mass = 300, position = np.array([1000, 1000, 0]), velocity = np.array([20, 0, 0])))
#add springed particles
x.add_body(pe.Heart(position=[1000, 1000, 0], mass = 20, velocity=[0,0,0], radius=300, charge =0,drag_coeff=3,elasticity=0, N_particles=200, damping=0.4, name="",environment=x))   
def velocity_field(particle):
    #sine wave 
    particle.force[0] += 100*np.sin((particle.position[0]))
    
    particle.force[1] += 100*np.sin(particle.position[0])
    pass
x.add_field(velocity_field, active=False)
    
#x.add_gravity(G=100000, softening_length=5, active=False)
x.add_uniform_acceleration_field(a=[0.0, 98,0.0], active=False, name="Gravity")
x.add_uniform_force_field(F=[200, 400,0], active=False, name="Wind")
x.add_spring(softening_length=1)
# x.add_uniform_acceleration_field(a=[0.0, 98,0.0])


vis =pe.Visualize(x)
vis.simulationheight = [0, 2000]
vis.simulationwidth = [0, 2000]
vis.show()


#x.add_anchor(pe.Anchor(position=[500, 1000, 0], mass = 400))
#x.add_particle(pe.Particle(mass = 20, position = np.array([1000, 1500, 0]), velocity = np.array([20, 0, 0])))
# x.add_particle(pe.Particle(mass = 30, position = np.array([1000, 800, 0]), velocity = np.array([0, -40, 0])))
# x.add_particle(pe.Particle(mass = 20, position = np.array([900, 800, 0]), velocity = np.array([0, 40, 0])))
#x.add_spring_link(x.particles[0], x.particles[1], l0=80)


# s1 = pe.Particle(mass = 20, position = np.array([990, 800, 0]), velocity = np.array([0, 0, 0]))
# s2 = pe.Particle(mass = 30, position = np.array([1010, 800, 0]), velocity = np.array([0, 0, 0]))
# x.add_springed_particles(s1, s2, k=10, l0=50, damping=0.5)

#x.add_body(pe.Ball(position=[1000, 1000, 0], mass = 20, velocity=[0,0,0], radius=300, charge =0,drag_coeff=3,elasticity=0, N_particles=200, damping=0.4, name="",environment=x))
#x.add_body(pe.AnchoredCloth(corner=[750,500,0], mass=0.5, k=90,damping=0.8, N_width=10, N_length=20, cell_size=40, drag=0.2, environment=x))

#x.add_spring(softening_length=0)
#x.add_uniform_force_field(F=[30, 0,50])


#x.add_field(velocity_field, active=False)
#x.add_field(velocity_field_lorenz_centered, active=True)


#x.add_uniform_acceleration_field(a=[0.0, 98,0.0])
#x.add_drag()
# for _ in range(30):
#     x.add_particle(pe.Particle(mass = np.random.randint(1,15), position = np.random.rand(3) * 2000)) #, velocity = np.random.uniform(-1,1,3)*10
#x.add_body(pe.AnchoredCloth(corner=[500,500,0], mass=0.5, k=90,damping=0.8, N_width=10, N_length=20, cell_size=40, drag=0.2, environment=x))
#x.add_body(pe.Particle(mass = 1, position = np.array([0, 1, 1.05]), velocity = np.array([0, 0, 0])))
#add range of particles on left side with constant velocity to right