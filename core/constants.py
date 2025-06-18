import pygame
# Screen dimensions
WIDTH = 720
HEIGHT = 360

# Colors (R, G, B)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# Spaceship
SPACESHIP_WIDTH = 55
SPACESHIP_HEIGHT = 40

# Game properties
FPS = 60
VEL = 5
BORDER_WIDTH = 10

# Assets path
ASSETS_PATH = "assets"

# Font - remove this line
# HEALTH_FONT = pygame.font.SysFont("comicsans", 30)

# Create a function to get the font instead
def get_health_font():
    return pygame.font.SysFont("comicsans", 30)
