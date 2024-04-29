import pygame as pg


class ShowPlayPause():
    """
    Class for controlling the play/pause functionality in a visualization.
    
    Args:
        visualize (Visualize): The visualization object.
        environment (Environment): The environment object.
    """
    
    def __init__(self, visualize, environment) -> None:
        self.visualize = visualize
        self.environment = environment
        self.active = False
        self.name = "Play/Pause"
        
    def show(self):
        """
        Show the play/pause functionality.
        """
        if self.active:
            self.visualize.simulating = True
            
        if not self.active:
            self.visualize.simulating = False
