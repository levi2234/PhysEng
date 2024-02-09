import pygame as pg


from PhysEng.Visualize.Elements.ShowParticles import ShowParticles
from PhysEng.Visualize.Elements.ShowVelocityVector import ShowVelocityVector
from PhysEng.Visualize.Elements.ShowSprings import ShowSprings
from PhysEng.Visualize.Elements.ShowFPS import ShowFPS
from PhysEng.Visualize.Elements.ShowVelocityColor import ShowVelocityColor
from PhysEng.Visualize.Elements.ShowAxes import ShowAxes
from PhysEng.Visualize.Elements.ShowForceVector import ShowForces
from PhysEng.Visualize.pygametoxy import pygame_to_xy
from PhysEng.Visualize.Events.EventHandler import EventHandler
from PhysEng.Visualize.Menu.menubar import MenuBar

class Visualize():
    def __init__(self,environment, name="Simulation") -> None:
        self.environment = environment
        self.screenwidth, self.screenheight = 1500, 720
        self.simulationwidth, self.simulationheight = [0,60], [0,60] #dimensions of the simulation that are seen
        
        self.elements = [   ShowParticles(self, self.environment),
                            ShowSprings(self, self.environment),
                            ShowVelocityVector(self, self.environment),
                            ShowVelocityColor(self, self.environment),
                            ShowForces(self, self.environment),
                            
        ]
        
        self.viewport_elements = [  ShowFPS(self, self.environment),
                                    ShowAxes(self, self.environment)]
        self.screen = None
        self.camera_vector = [0,0,1] #unit vector pointing in the direction of the camera
        self.name = name
        self.drag = False
        self.running = True
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
        

# # ----------------ELEMENT TOGGLE Buttons----------------
#         elementbuttons = []
#         for val, count in enumerate(self.elements):
#             elementbuttons.append(SwitchButton( [self.screenwidth-100, 50 + 60*val], linked_element= self.elements[val], visualizer=self))
#             pass

            
# #-----------------FORCE TOGGLE BUTTONS----------------
#         forcebuttons = []
        
#         #add text label
#         font = pg.font.Font(None, 36)
#         text = font.render("Forces", True, (255, 255, 255))

#         #screen.blit(text, (self.screenwidth-100, 250))
        
#         for count, val in enumerate(self.environment.forces):
#             forcebuttons.append(SwitchButton([self.screenwidth-100, 410 + 60*count], linked_element= self.environment.forces[count], visualizer=self))
#             pass
        
        
#-------------MAIN LOOP----------------
        while self.running:
            
            screen.fill((0, 0, 0)) #reset screen
            #limit max fps to self.maxfps
            pg.time.Clock().tick(self.maxfps)

            self.Menubar.draw()

            #propagate simulation
            self.environment.step()
            
            #load all simulation elements (particles, forces, etc.)
            for i in self.elements:
                i.show()
                
            #load all viewport elements (fps, axes, etc.)
            for i in self.viewport_elements:
                i.show()
                
            
             
            

            #process events
            for event in pg.event.get():
                EventHandler(self, event)
    
            
            
            
            
            # #show all buttons
            # for i in elementbuttons:
            #     i.draw()
                
            # for i in forcebuttons:
            #     i.draw()  

            
            
            pg.display.flip()
            
        pg.quit()