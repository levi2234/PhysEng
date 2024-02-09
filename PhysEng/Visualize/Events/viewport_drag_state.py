import pygame as pg
def viewport_drag_state(viz, event):
    if event.type == pg.MOUSEBUTTONDOWN:
        if event.button == 1:
            viz.drag = True
            viz.lastpos = pg.mouse.get_pos()
            
    if event.type == pg.MOUSEBUTTONUP:
        if event.button == 1:
            viz.drag = False
        
    