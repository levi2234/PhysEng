import pygame as pg
import pygame_gui as pgui
import time
import numpy as np
from PhysEng.Visualize.ShowParticles import ShowParticles
from PhysEng.Visualize.ShowVelocities import ShowVelocities
from PhysEng.Visualize.ShowSprings import ShowSprings
from PhysEng.Visualize.ShowFPS import ShowFPS
from PhysEng.Visualize.SwitchButton import SwitchButton
from PhysEng.Visualize.ShowAxes import ShowAxes
from PhysEng.Visualize.ShowForces import ShowForces

class Visualize():
    def __init__(self,environment, name="Simulation") -> None:
        self.environment = environment
        self.screenwidth, self.screenheight = 1400, 700
        self.simulationwidth, self.simulationheight = [0,2000], [0,2000]
        self.elements = [   ShowParticles(self, self.environment),
                            ShowVelocities(self, self.environment),
                            ShowSprings(self, self.environment),
                            ShowFPS(self, self.environment),
                            ShowAxes(self, self.environment),
                            ShowForces(self, self.environment)
        ]
        self.screen = None
        self.name = name
        pass
    
    def show(self):
        
#-------------MAIN SETUP----------------
        pg.init()
        size = (self.screenwidth, self.screenheight)
        screen = pg.display.set_mode(size)
        self.screen = screen
        pg.display.set_caption(self.name)
        running = True
        
        #setup GUI
        self.manager = pgui.UIManager(size)
        

# ----------------ELEMENT TOGGLE Buttons----------------
        elementbuttons = []
        for val, count in enumerate(self.elements):
            elementbuttons.append(SwitchButton( [self.screenwidth-100, 50 + 60*val], linked_element= self.elements[val], visualizer=self))
            pass

            
#-----------------FORCE TOGGLE BUTTONS----------------
        forcebuttons = []
        
        #add text label
        font = pg.font.Font(None, 36)
        text = font.render("Forces", True, (255, 255, 255))

        #screen.blit(text, (self.screenwidth-100, 250))
        
        for count, val in enumerate(self.environment.forces):
            forcebuttons.append(SwitchButton([self.screenwidth-100, 410 + 60*count], linked_element= self.environment.forces[count], visualizer=self))
            pass
        
        
#-------------MAIN LOOP----------------
        while running:
            screen.fill((0, 0, 0)) #reset screen
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
            
            self.environment.step()
            
            #load all elements
            for i in self.elements:
                i.show()
            
            #show all buttons
            for i in elementbuttons:
                i.draw()
                
            for i in forcebuttons:
                i.draw()  

            
            
            pg.display.flip()
            
        pg.quit()