import pygame as pg
class EnableRendering():
    """
    This class represents an object that enables or disables rendering in a visualization by setting the 
    visualize.render_video to true

    Attributes:
        visualize (Visualize): The visualization object.
        environment (Environment): The environment object.
        active (bool): Indicates whether rendering is active or not.
        name (str): The name of the object.
    """

    def __init__(self, visualize, environment) -> None:
        self.visualize = visualize
        self.environment = environment
        self.active = False
        self.name = f"Enable Rendering"
        pass
    
    def show(self):
        """
        Here the show function is not a good discritptor but is what the menu class expects to change the state of render_video

        If active is True, rendering is enabled.
        If active is False, rendering is disabled.
        """
        if self.active:
            self.visualize.render_video = True
            
        if not self.active:
            self.visualize.render_video = False

            pass
