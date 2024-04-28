import pygame as pg
import numpy as np


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

#rendering
from PhysEng.Visualize.Renderer import Renderer
from PhysEng.Visualize.Elements.ShowBuffersize import ShowBuffersize
from PhysEng.Visualize.Elements.ClearBuffer import ClearBuffer
from PhysEng.Visualize.Elements.Enable_Rendering import EnableRendering


#integrators 
from PhysEng.Visualize.Elements.Enable_Euler import EnableEuler
from PhysEng.Visualize.Elements.Enable_RK4 import EnableRK4
from PhysEng.Visualize.Elements.Enable_Verlet import EnableVerlet
from PhysEng.Visualize.Elements.Enable_Leapfrog import EnableLeapfrog


class Visualize():
    def __init__(self,environment, name="Simulation",enable_rendering=False, render_video=False, output_fps=30, output="output.mp4", output_codec="libx264", output_framelimit=300) -> None:
        self.environment = environment
        self.screenwidth, self.screenheight = 1500, 720
        self.simulationwidth, self.simulationheight = [0,60], [0,60] #dimensions of the simulation that are seen
        self.render_video = render_video
        self.enable_rendering = enable_rendering
        if self.enable_rendering:
            self.renderer = Renderer(output=output, fps=output_fps, codec=output_codec, framelimit=output_framelimit)

        
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
        if self.enable_rendering:
            self.recorders = [ShowBuffersize(self, self.environment),
                            ClearBuffer(self, self.environment),
                            EnableRendering(self, self.environment)
                            ]
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
            
            if self.enable_rendering:  
                for i in self.recorders:
                    i.show()

                
            
             
            

            #process events
            for event in pg.event.get():
                EventHandler(self, event)
            
            
            pg.display.flip()
            
            
            #render frame
            if self.render_video and self.simulating:
                
                imgdata = np.copy(pg.surfarray.pixels2d(screen))
                
                self.renderer.add_frame(imgdata)
                

            
            

        
        #render video
        if self.render_video:
            self.renderer.render()


            
        pg.quit()