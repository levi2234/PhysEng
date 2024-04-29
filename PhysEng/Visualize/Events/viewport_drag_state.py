import pygame as pg
def viewport_drag_state(viz, event):
    """
    Updates the drag state of the viewport based on the mouse events.

    Parameters:
    viz (object): The visualization object.
    event (object): The mouse event.

    Returns:
    None
    """
    if event.type == pg.MOUSEBUTTONDOWN:
        if event.button == 1:
            viz.drag = True
            viz.lastpos = pg.mouse.get_pos()
            
    if event.type == pg.MOUSEBUTTONUP:
        if event.button == 1:
            viz.drag = False
        
    