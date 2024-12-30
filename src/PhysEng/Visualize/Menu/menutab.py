import pygame as pg
import time
import numpy as np
import pygame as pg
import numpy as np
import time

class MenuTab():
    """
    Represents a tab in a menu.

    Args:
        pos (list, optional): The position of the tab. Defaults to [0, 0, 0].
        width (int, optional): The width of the tab. Defaults to 100.
        visualizer (object, optional): The visualizer object. Defaults to None.
        active (bool, optional): Indicates if the tab is active. Defaults to True.
        color (list, optional): The color of the tab. Defaults to [255, 255, 255].
        linked_elements (list, optional): List of linked elements. Defaults to None.
        name (str, optional): The name of the tab. Defaults to "Newtab".
    """

    def __init__(self, pos=[0,0,0], width=100, visualizer=None, active=True, color=[255,255,255], linked_elements:list=None, name="Newtab") -> None:
        """
        Initializes a new instance of the MenuTab class.

        Args:
            pos (list, optional): The position of the tab. Defaults to [0, 0, 0].
            width (int, optional): The width of the tab. Defaults to 100.
            visualizer (object, optional): The visualizer object. Defaults to None.
            active (bool, optional): Indicates if the tab is active. Defaults to True.
            color (list, optional): The color of the tab. Defaults to [255, 255, 255].
            linked_elements (list, optional): List of linked elements. Defaults to None.
            name (str, optional): The name of the tab. Defaults to "Newtab".
        """
        self.visualizer = visualizer
        self.linked_elements = linked_elements
        self.screen = visualizer.screen

        self.name = name
        self.pos = pos
        self.width = width
        self.last_click = time.time()
        self.active = active
        self.rect = pg.Rect(self.pos, (self.width, 20))
        self.color = color

    def draw(self):
        """
        Draws the menu tab on the screen.
        """
        pos = pg.mouse.get_pos()

        # DRAWING BUTTONS
        if self.active:
            if self.rect.collidepoint(pos):  # highlight if mouse over
                pg.draw.rect(self.screen, np.array(self.color)/2, (self.pos[0], self.pos[1], self.width, 20))
            elif self.linked_elements[0].active:  # highlight if linked element is active
                pg.draw.rect(self.screen, np.array(self.color)/2, (self.pos[0], self.pos[1], self.width, 20))
            else:  # draw normal
                pg.draw.rect(self.screen, self.color, (self.pos[0], self.pos[1], self.width, 20))
        else:  # draw nothing if menutab not active
            pg.draw.rect(self.screen, (0, 0, 0), (self.pos[0], self.pos[1], self.width, 20))

        font = pg.font.Font(None, 20)
        text = font.render(self.name, True, (0, 0, 0))
        self.screen.blit(text, (self.pos[0]+10, self.pos[1]+2))

        # BUTTON CLICK LOGIC
        if self.rect.collidepoint(pos) and time.time() - self.last_click > 0.2:
            if pg.mouse.get_pressed()[0]:
                for i in self.linked_elements:
                    i.active = not i.active
                    self.last_click = time.time()

        # draw linked elements
        for i in self.linked_elements:
            if isinstance(i, MenuTab):
                i.draw()
