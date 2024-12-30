import pygame as pg
def playpausespacebar(viz, event):
    """
    Function to handle the play/pause functionality triggered by pressing the spacebar.

    Parameters:
    - viz: The visualization object.
    - event: The event object representing the key press event.

    Returns:
    None
    """
    if event.key == pg.K_SPACE:
        viz.simulating = not viz.simulating
        #find the play/pause button and change its state
        for i in viz.viewport_elements:
            if i.name == "Play/Pause":
                i.active = not i.active
        pass
    pass