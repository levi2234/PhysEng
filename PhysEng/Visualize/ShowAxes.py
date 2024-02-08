import pygame as pg
from PhysEng.Visualize.xytopygame import xy_to_topygame as xy

class ShowAxes():
    
    def __init__(self, visualize, environment) -> None:
        self.visualize = visualize
        self.environment = environment
        self.prev_time = pg.time.get_ticks()
        self.active = False
        self.name = "Axes"
        
        pass
    
    def show(self):
        if not self.active:
            return
        
    #simulation width and height
        sw, sh = self.visualize.simulationwidth, self.visualize.simulationheight
        
    #screen width and height
        scw, sch = self.visualize.screenwidth, self.visualize.screenheight
        
    #draw line of x-axis
        pg.draw.line(self.visualize.screen, (255, 255, 255), xy(self.visualize, sw[0], sh[1]-10), xy(self.visualize,sw[1], sh[1]-10), 3)
        
    #draw ticks on x-axis
        for i in range(0, sw[1], 100):
            pg.draw.line(self.visualize.screen, (255, 255, 255), xy(self.visualize, i, sh[1]-10), xy(self.visualize, i, sh[1]-40), 3)
            #draw text on ticks in terms of simulation
            font = pg.font.Font(None, 20)
            text = font.render(str(i), True, (255, 255, 255))
            #draw text on screen
            self.visualize.screen.blit(text, xy(self.visualize, i-20, sh[1]-90))
            
    #draw line of y-axis
        pg.draw.line(self.visualize.screen, (255, 255, 255), xy(self.visualize, sw[0]+10, sh[0]), xy(self.visualize,sw[0]+10, sh[1]), 3)
        
    #draw ticks on y-axis
        for i in range(0, sh[1], 100):
            pg.draw.line(self.visualize.screen, (255, 255, 255), xy(self.visualize, sw[0]+10, i), xy(self.visualize, sw[0]+20, i), 3)
            #draw text on ticks in terms of simulation
            font = pg.font.Font(None, 20)
            text = font.render(str(i), True, (255, 255, 255))
            #draw text on screen
            self.visualize.screen.blit(text, xy(self.visualize, sw[0]+40, i-20))
        
        
        
        pass