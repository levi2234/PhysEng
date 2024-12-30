import pygame as pg

def quit(viz):
    """
    Stops the rendering process in the visualization on close of window or other closing actions

    Args:
        viz (Visualization): The visualization object.

    Returns:
        None
    """
    viz.rendering = False