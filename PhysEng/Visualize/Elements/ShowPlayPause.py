import pygame as pg


class ShowPlayPause():
    
    def __init__(self, visualize, environment) -> None:
        self.visualize = visualize
        self.environment = environment
        self.active = False
        self.name = "Play/Pause"
        
        
        pass
    
    def show(self):
        #eventlistener for play/pause with spacebar
        # for event in pg.event.get():
        #     if event.type == pg.KEYDOWN:
        #         if event.key == pg.K_SPACE:
        #             self.active = not self.active
        #             pass
        #         pass
        #     pass        

        if self.active:
            self.visualize.simulating = True
            
        if not self.active:
            self.visualize.simulating = False
        pass