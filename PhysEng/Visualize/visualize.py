import pygame as pg


from PhysEng.Visualize.Elements.ShowParticles import ShowParticles
from PhysEng.Visualize.Elements.ShowVelocityVector import ShowVelocityVector
from PhysEng.Visualize.Elements.ShowSprings import ShowSprings
from PhysEng.Visualize.Elements.ShowFPS import ShowFPS
from PhysEng.Visualize.Elements.ShowVelocityColor import ShowVelocityColor
from PhysEng.Visualize.Elements.ShowAxes import ShowAxes
from PhysEng.Visualize.Elements.ShowForceVector import ShowForces
from PhysEng.Visualize.Elements.ShowTrail import ShowTrail
from PhysEng.Visualize.Elements.ShowPlayPause import ShowPlayPause
from PhysEng.Visualize.pygametoxy import pygame_to_xy
from PhysEng.Visualize.Events.EventHandler import EventHandler
from PhysEng.Visualize.Menu.menubar import MenuBar

#integrators 
from PhysEng.Visualize.Elements.Enable_Euler import EnableEuler
from PhysEng.Visualize.Elements.Enable_RK4 import EnableRK4
from PhysEng.Visualize.Elements.Enable_Verlet import EnableVerlet
from PhysEng.Visualize.Elements.Enable_Leapfrog import EnableLeapfrog


class Visualize():
    def __init__(self,environment, name="Simulation") -> None:
        self.environment = environment
        self.screenwidth, self.screenheight = 1500, 720
        self.simulationwidth, self.simulationheight = [0,60], [0,60] #dimensions of the simulation that are seen
        
        self.elements = [   ShowParticles(self, self.environment),
                            ShowTrail(self, self.environment),
                            ShowSprings(self, self.environment),
                            ShowVelocityVector(self, self.environment),
                            ShowVelocityColor(self, self.environment),
                            ShowForces(self, self.environment)
                            
                            
        ]
        
        self.viewport_elements = [ ShowPlayPause(self, self.environment), 
                                    ShowFPS(self, self.environment),
                                    ShowAxes(self, self.environment)]
        
        self.integrators = [ EnableEuler(self, self.environment),
                             EnableRK4(self, self.environment),
                             EnableVerlet(self, self.environment),
                             EnableLeapfrog(self, self.environment)]
        self.screen = None
        self.camera_vector = [0,0,1] #unit vector pointing in the direction of the camera
        self.name = name
        self.drag = False
        self.rendering = True
        self.simulating = False
        self.maxfps = 500
        
        
        pass
    
    def show(self):
        
#-------------MAIN SETUP----------------
        pg.init()
        size = (self.screenwidth, self.screenheight)
        screen = pg.display.set_mode(size, pg.RESIZABLE)
        self.screen = screen
        pg.display.set_caption(self.name)
        
        
        self.Menubar = MenuBar(self)
        
        
#-------------MAIN LOOP----------------
        while self.rendering:
            
            screen.fill((0, 0, 0)) #reset screen
            #limit max fps to self.maxfps
            pg.time.Clock().tick(self.maxfps)

            self.Menubar.draw()

            #propagate simulation
            if self.simulating:
                self.environment.step()
            
            #load all simulation elements (particles, forces, etc.)
            for i in self.elements:
                i.show()
                
            #load all viewport elements (fps, axes, etc.)
            for i in self.viewport_elements:
                i.show()
            
            # #load all integrators
            for i in self.integrators:
                i.show()

                
            
             
            

            #process events
            for event in pg.event.get():
                EventHandler(self, event)
            
            
            pg.display.flip()
            
        pg.quit()