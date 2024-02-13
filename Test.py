import pygame
import math

def lerp_color(start_color, end_color, lerp):
    """Interpolate between two colors."""
    return [start_color[i] + (end_color[i] - start_color[i]) * lerp for i in range(3)]

def draw_radial_gradient(surface, center, inner_color, outer_color, radius):
    """Draw a radial gradient."""
    for y in range(surface.get_height()):
        for x in range(surface.get_width()):
            # Distance from the center
            dist = math.sqrt((center[0] - x) ** 2 + (center[1] - y) ** 2) / radius

            if dist <= 1.0:
                # Calculate interpolated color
                color = lerp_color(inner_color, outer_color, dist)
                surface.set_at((x, y), color)
            else:
                # Outside the specified radius, fill with the outer color
                surface.set_at((x, y), outer_color)

pygame.init()

# Screen setup
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
pygame.display.set_caption("Radial Gradient Background")

# Gradient settings
center_position = (screen_width // 2, screen_height // 2)
inner_color = (10, 10, 10)  # White
outer_color = (0, 0, 0)  # Blue
gradient_radius = min(screen_width, screen_height) // 2 

# Create a surface for the gradient
gradient_surf = pygame.Surface((screen_width, screen_height))

# Draw the gradient
draw_radial_gradient(gradient_surf, center_position, inner_color, outer_color, gradient_radius)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Blit the gradient surface onto the screen
    screen.blit(gradient_surf, (0, 0))
    pygame.display.flip()

pygame.quit()
