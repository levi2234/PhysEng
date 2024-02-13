import pygame as pg
from PhysEng.Visualize.xytopygame import xy_to_topygame as xy

class ShowFPS():
    
    def __init__(self, visualize, environment) -> None:
        self.visualize = visualize
        self.environment = environment
        self.prev_time = pg.time.get_ticks()
        self.active = True
        self.name = "FPS"
        
        pass
    
    def show(self):
        if self.active:
            current_time = pg.time.get_ticks()
            fps = 1000 / (current_time - self.prev_time)
            self.prev_time = current_time
            font = pg.font.Font(None, 20)
            text = font.render("FPS: "+str(int(fps)), True, (255, 255, 255))
            self.visualize.screen.blit(text, (480, 0))
            pg.display.set_caption(self.visualize.name + f"     FPS: {int(fps)}")
            pass
        else:
            pass