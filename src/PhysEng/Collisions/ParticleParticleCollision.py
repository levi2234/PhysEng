
import numpy as np


class ParticleParticleCollision():
    
    def __init__(self, environment) :
            self.environment = environment
            
    def update(self):
        
        #update the collision detector
        for i in self.environment.particles:
            collision_partners = self.detect_collision(i)
            
            #resolve all collisions
            for j in collision_partners:
                self.resolve_collision(i, j)
            return False
        pass
    
    def detect_collision(self,particle1):
        collision_partners = []
        for j in self.environment.particles:
            if j == particle1:
                continue
            if np.linalg.norm(particle1.position - j.position) < particle1.radius + j.radius:
                collision_partners.append(j)
        return collision_partners
    
    def resolve_collision(self, particle1, particle2):
        
        #get the normal vector
        n = particle1.position - particle2.position
        n = n / np.linalg.norm(n)
        
        #get the relative velocity
        v = particle1.velocity - particle2.velocity
        
        #get the impulse
        j = -2 * np.dot(v, n) / (1/particle1.mass + 1/particle2.mass)
        
        #apply the impulse
        particle1.velocity += j * n / particle1.mass
        particle2.velocity -= j * n / particle2.mass
        pass    
