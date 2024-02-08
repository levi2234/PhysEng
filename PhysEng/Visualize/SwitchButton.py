import pygame as pg
import time
class SwitchButton(): #a pygame button with 2 states
    
    def __init__(self, location=[0,0], linked_element=None, visualizer=None) -> None:
        
        self.location = location
        self.state = linked_element.active #False is off, True is on set to the state of the linked element
        self.linked_element = linked_element
        self.rect = pg.Rect(self.location, (80,40))
        self.visualizer = visualizer
        self.last_click = time.time()
        self.name = linked_element.name
        
    
    def draw(self):
        
        #rect
        
        if self.state:
            pg.draw.rect(self.visualizer.screen, (0,255,0), self.rect , width=2, border_radius=10)
        else:
            pg.draw.rect(self.visualizer.screen, (255,0,0),  self.rect, width=2, border_radius=10,)
            
        pos = pg.mouse.get_pos()
        if self.rect.collidepoint(pos) and time.time() - self.last_click > 0.3:
            if pg.mouse.get_pressed()[0]:
                self.state = not self.state
                self.linked_element.active = self.state
                self.last_click = time.time()
                pass
        font = pg.font.Font(None, 20)
        text_location = [self.location[0] + 8, self.location[1] + 10]  # Modify the location here
        self.visualizer.screen.blit(font.render(self.name, True, (255,255,255)), text_location)
        