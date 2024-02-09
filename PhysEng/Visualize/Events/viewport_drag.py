from PhysEng.Visualize.pygametoxy import pygame_to_xy
import pygame as pg
def viewport_drag(viz, event):
    if viz.drag:
        x, y = pg.mouse.get_pos()
        x,y = pygame_to_xy(viz, x, y)
        lastpos = pygame_to_xy(viz, viz.lastpos[0], viz.lastpos[1])
        
        new_width_x_left = viz.simulationwidth[0] - (x - lastpos[0])
        new_width_x_right = viz.simulationwidth[1] - (x - lastpos[0])
        new_height_y_top = viz.simulationheight[0] - (y - lastpos[1])
        new_height_y_bottom = viz.simulationheight[1] - (y - lastpos[1])
        

        
        viz.simulationwidth = [new_width_x_left, new_width_x_right]
        viz.simulationheight = [new_height_y_top, new_height_y_bottom]
        viz.lastpos = pg.mouse.get_pos()