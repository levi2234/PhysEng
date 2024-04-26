import pygame as pg
class EnableRendering():
    
    def __init__(self, visualize, environment) -> None:
        self.visualize = visualize
        self.environment = environment
        self.active = False
        self.name = f"Enable Rendering"
        pass
    
    def show(self):
        if self.active:
            self.visualize.render_video = True
            
        if not self.active:
            self.visualize.render_video = False

            pass
