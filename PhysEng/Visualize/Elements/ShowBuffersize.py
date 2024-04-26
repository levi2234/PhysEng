import pygame as pg
class ShowBuffersize():
    
    def __init__(self, visualize, environment) -> None:
        self.visualize = visualize
        self.environment = environment
        self.active = True
        self.name = f"Buffer Size"
        pass
    
    def show(self):
        if self.active:
            font = pg.font.Font(None, 20)
            text = font.render("Buffer Size: "+str(len(self.visualize.renderer.frames)), True, (255, 255, 255))
            self.visualize.screen.blit(text, (800, 0))

            pass
