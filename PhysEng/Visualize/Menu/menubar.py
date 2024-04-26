import pygame as pg
from PhysEng.Visualize.Menu.menutab import MenuTab

class MenuBar():
    
    def __init__(self, visualizer):
        self.visualizer = visualizer
        
        self.tabs =[]
        self.active = True
        
        self.initialize() #initialize 
        
    def initialize(self):
        
        
        viewportlinks = []
        for count,val in enumerate(self.visualizer.viewport_elements):
            Viewport_pos = [0, (count+1) * 20]
            viewport_tab = MenuTab(visualizer=self.visualizer, pos=Viewport_pos, name=val.name, width=120, active=False, linked_elements=[val])
            viewportlinks.append(viewport_tab)

            
        forcelinks = []
        for count,val in enumerate(self.visualizer.environment.forces):
            Forces_pos = [120, (count+1) * 20]
            force_tab = MenuTab(visualizer=self.visualizer, pos=Forces_pos, name=val.name, width=120, active=False, linked_elements=[val])
            forcelinks.append(force_tab)
            
        #show particles
        elementlinks = []
        for count,val in enumerate(self.visualizer.elements):
            Elements_pos = [240, (count+1) * 20]
            Elements_tab = MenuTab(visualizer=self.visualizer, pos=Elements_pos, name=val.name, width=120, active=False, linked_elements=[val])
            elementlinks.append(Elements_tab)
            
        integratorlinks = []
        for count,val in enumerate(self.visualizer.integrators):
            Integrator_pos = [360, (count+1) * 20]
            integrator_tab = MenuTab(visualizer=self.visualizer, pos=Integrator_pos, name=val.name, width=120, active=False, linked_elements=[val])
            integratorlinks.append(integrator_tab)
        
        
        recorderlinks = []
        for count,val in enumerate(self.visualizer.recorders):
            Recorder_pos = [480, (count+1) * 20]
            recorder_tab = MenuTab(visualizer=self.visualizer, pos=Recorder_pos, name=val.name, width=120, active=False, linked_elements=[val])
            recorderlinks.append(recorder_tab)
        
        
        Elements_pos = [240, 0]
        element_tab = MenuTab(visualizer=self.visualizer, pos=Elements_pos, name="Elements", width=120, color=[200,200,200], active=True, linked_elements=elementlinks)
        self.tabs.append(element_tab)
        
        Forces_pos = [120, 0]
        force_tab = MenuTab(visualizer=self.visualizer, pos=Forces_pos, name="Forces", width=120,color=[200,200,200], linked_elements=forcelinks, active=True)
        self.tabs.append(force_tab)
        
        Simulation_pos = [0, 0]
        simulation_tab = MenuTab(visualizer=self.visualizer, pos=Simulation_pos, name="View", width=120,color=[200,200,200], linked_elements=viewportlinks, active=True)
        self.tabs.append(simulation_tab)
        
        Integrator_pos = [360, 0]
        integrator_tab = MenuTab(visualizer=self.visualizer, pos=Integrator_pos, name="Integrators", width=120,color=[200,200,200], linked_elements=integratorlinks, active=True)
        self.tabs.append(integrator_tab)
        
        Recorder_pos = [480, 0]
        recorder_tab = MenuTab(visualizer=self.visualizer, pos=Recorder_pos, name="Recorder", width=120,color=[200,200,200], active=True, linked_elements=recorderlinks)
        self.tabs.append(recorder_tab)

     
    def draw(self):
        for i in self.tabs:
            i.draw()
        
        pass