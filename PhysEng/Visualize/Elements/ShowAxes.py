import pygame as pg
import numpy as np
from PhysEng.Visualize.xytopygame import xy_to_topygame as xy

class ShowAxes():
    """
    Class for enabling axes visualization on screen through the menu.

    Parameters:
    - visualize: The visualization object.
    - environment: The environment object.

    Returns:
    None
    
    """

    def __init__(self, visualize, environment) -> None:

        self.visualize = visualize
        self.environment = environment
        self.prev_time = pg.time.get_ticks()
        self.active = False
        self.name = "Axes"
        
    def show(self):
        """
        Display the axes on the visualization screen.

        Parameters:
        None

        Returns:
        None
        """
        if not self.active:
            return
        
        #simulation width and height
        sw, sh = self.visualize.simulationwidth, self.visualize.simulationheight
        
        #screen width and height
        scw, sch = self.visualize.screenwidth, self.visualize.screenheight
        
        #draw line of x-axis
        pg.draw.line(self.visualize.screen, (255, 255, 255), [0, sch-3], [scw,sch-3], 3)
        
        #draw line of y-axis
        pg.draw.line(self.visualize.screen, (255, 255, 255), [3, 0], [3, sch], 3)
        
        number_of_ticks = 20
        
        tick_values_x = np.round(np.linspace(sw[0], sw[1], number_of_ticks), 1)
        tick_values_y = np.round(np.linspace(sh[0], sh[1], number_of_ticks), 1)


        tick_locations_x = np.linspace(0, scw, number_of_ticks)
        tick_locations_y = np.linspace(0, sch, number_of_ticks)
        
        
        #set font 
        font = pg.font.Font(None, 20)
        
        
        #draw x-axis
        for i in zip(tick_locations_x, tick_values_x):
            pg.draw.line(self.visualize.screen, (255, 255, 255), [i[0], sch-10], [i[0], sch+3], 3)
            text = font.render(str(i[1]), True, (255, 255, 255))
            self.visualize.screen.blit(text, [i[0]-10, sch-25])
            
        #draw y-axis
        for i in zip(tick_locations_y, tick_values_y):
            pg.draw.line(self.visualize.screen, (255, 255, 255), [3, i[0]], [10, i[0]], 3)
            text = font.render(str(i[1]), True, (255, 255, 255))
            self.visualize.screen.blit(text, [15, i[0]-5])
