import numpy as np
from scipy.integrate import quad
from scipy.special import hermite

class hermite():
    
    def __init__(self, order) -> None:
        self.environment = None
        self.order = order
        
    def update(self):
        #update forces based on hermite integrator
        #update forces based on hermite integrator
        