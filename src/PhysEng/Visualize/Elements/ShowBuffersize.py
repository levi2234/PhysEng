import pygame as pg
class ShowBuffersize():
    """
    A class that displays the buffer size on the screen.

    Attributes:
    - visualize: The visualize object.
    - environment: The environment object.
    - active: A boolean indicating whether the buffer size display is active.
    - name: The name of the buffer size display.

    Methods:
    - show: Displays the buffer size on the screen.
    """
    
    def __init__(self, visualize, environment) -> None:
        self.visualize = visualize
        self.environment = environment
        self.active = True
        self.name = f"Buffer Size"
        pass
    
    def show(self):
        """
        Displays the buffer size on the screen.
        """
        if self.active:
            font = pg.font.Font(None, 20)
            text = font.render("Buffer Size: "+str(len(self.visualize.renderer.frames)), True, (255, 255, 255))
            self.visualize.screen.blit(text, (800, 0))

            pass
