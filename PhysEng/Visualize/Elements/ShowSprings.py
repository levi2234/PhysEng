import pygame as pg
import numpy as np
from PhysEng.Visualize.xytopygame import xy_to_topygame as xy


def force_to_color(force, max_force, min_force):
    """
    Converts a force value to a corresponding color to display stresses in the springs

    Parameters:
    force (float): The force value to be converted.
    max_force (float): The maximum force value.
    min_force (float): The minimum force value.

    Returns:
    numpy.ndarray: The color corresponding to the given force value.
    """
    # Normalize the force to a value between 0 and 1
    normalized_force = (force - min_force) / (max_force - min_force)
    normalized_force = np.clip(normalized_force, 0, 1)

    # Define the colors for the maximum and minimum forces
    min_color = np.array([0, 0, 255])  # Blue for the minimum force
    max_color = np.array([255, 0, 0])  # Red for the maximum force

    # Calculate the color for the given force
    color = (1 - normalized_force) * min_color + normalized_force * max_color

    return color.astype(int)


class ShowSprings():
    """
    A class for visualizing springs in a physics simulation.

    Attributes:
        visualize (Visualize): The visualization object.
        environment (Environment): The environment object.
        active (bool): Indicates if the springs should be shown or not.
        name (str): The name of the springs.
    """
    
    def __init__(self, visualize, environment) -> None:
        self.visualize = visualize
        self.environment = environment
        self.active = False  
        self.name = "Springs"
        pass
    
    def show(self):
        """
        Show the springs on the visualization screen.

        This method draws lines between the particles connected by springs,
        with the color of the lines determined by the force applied on the springs.
        """
        if self.active:
            for i in self.environment.spring_links:
                xy1 = xy(self.visualize,i.particle1.position[0], i.particle1.position[1])
                xy2 = xy(self.visualize,i.particle2.position[0], i.particle2.position[1])
                force = i.force

                # Determine color based on force from gradient
                color = force_to_color(force, 10, 0)

                pg.draw.line(self.visualize.screen, color, xy1, xy2, 3)
        pass