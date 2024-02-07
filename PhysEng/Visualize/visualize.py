import pygame as pg
import time
import numpy as np

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


class Visualize():
    
    def __init__(self, environment, name="Simulation") -> None:
        
        #pygame loop to plot a point
        self.environment = environment
        self.screenwidth, self.screenheight = 1400, 800
        self.simulationwidth, self.simulationheight = [0,2000], [0,2000]
        self.name = name
        
        
    def xy_to_topygame(self,x,y):
        #scale any range to 0-screenwidth and 0-screenheight
        
        x = (x - self.simulationwidth[0]) * (self.screenwidth / (self.simulationwidth[1] - self.simulationwidth[0]))
        y = (y - self.simulationheight[0]) * (self.screenheight / (self.simulationheight[1] - self.simulationheight[0]))
        return (x, y)
        
        
    def show(self, show_fps=True,Particles=True, Velocities=False, Forces=False, Springs=True):
        
        #main pygame loop to plot a point
        pg.init()
        size = (self.screenwidth, self.screenheight)
        screen = pg.display.set_mode(size)
        #set origin to bottom left

        pg.display.set_caption(self.name)
        running = True


        


        while running:
            current_fps = 0
            #keep time
            if show_fps:
                start = time.time()
            
            
            # clear the screen
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                    
            particle = self.environment.particles[0]
            
            
            screen.fill((0, 0, 0))
                

            #draw spring links
            if Springs:
                for i in self.environment.spring_links:
                    xy1 = self.xy_to_topygame(i.particle1.position[0], i.particle1.position[1])
                    xy2 = self.xy_to_topygame(i.particle2.position[0], i.particle2.position[1])
                    force = i.force

                    # Determine color based on force from gradient
                    color = force_to_color(force, 10, 0)

                    pg.draw.line(screen, color, xy1, xy2, 3)
                    
            #draw particles
            if Particles:
                for i in self.environment.particles:
                    pg.draw.circle(screen, (255, 255, 255), self.xy_to_topygame(i.position[0], i.position[1]), 5)
                    
            if Velocities:
                for i in self.environment.particles:
                    pg.draw.line(screen, (255, 0, 0), self.xy_to_topygame(i.position[0], i.position[1]), self.xy_to_topygame(i.position[0]+i.velocity[0], i.position[1]+i.velocity[1]), 3)

            self.environment.step()
            
            
            
            
            #draw text to lower left
            if show_fps:
                try:
                    current_fps = int((1/(time.time()-start)))
                except:
                    current_fps = 0
                font = pg.font.Font(None, 36)
                fps = font.render(f"{current_fps} FPS", True, (255, 255, 255) )
                TIME = font.render(f"{int(self.environment.time)} s", True, (255, 255, 255) )
                screen.blit(TIME, (0, 30))
                screen.blit(fps, (0, 0))
            
            pg.display.flip()

            
        pg.quit()


            
            
            
            
# x = pe.Environment()    