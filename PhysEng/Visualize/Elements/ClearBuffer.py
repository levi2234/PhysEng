
class ClearBuffer():
    """
    A class representing a buffer clearing element in a visualization.

    Attributes:
        visualize (Visualize): The visualization object.
        environment (Environment): The environment object.
        active (bool): Indicates if the clear buffer element is active.
        name (str): The name of the clear buffer element.
    """

    def __init__(self, visualize, environment) -> None:
        self.visualize = visualize
        self.environment = environment
        self.active = False
        self.name = f"Clear Buffer"
        pass
    
    def show(self):
        """
        Clears the frames in the renderer if the clear buffer element is active.
        """
        if self.active:
            self.visualize.renderer.clear_frames()
            self.active = False
            pass
