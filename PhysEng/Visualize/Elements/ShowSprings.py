import pygame as pg
import numpy as np
from PhysEng.Visualize.xytopygame import xy_to_topygame as xy


def force_to_color(force, max_force, min_force):
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
    
    def __init__(self, visualize, environment) -> None:
        self.visualize = visualize
        self.environment = environment
        self.active = False  
        self.name = "Springs"
        pass
    
    def show(self):

        if self.active:
            for i in self.environment.spring_links:
                xy1 = xy(self.visualize,i.particle1.position[0], i.particle1.position[1])
                xy2 = xy(self.visualize,i.particle2.position[0], i.particle2.position[1])
                force = i.force

                # Determine color based on force from gradient
                color = force_to_color(force, 10, 0)

                pg.draw.line(self.visualize.screen, color, xy1, xy2, 3)
        pass