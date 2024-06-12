import pygame

pygame.init()
pygame.font.init()

white = (255, 255, 255)
black = (0, 0, 0)

fps = 500

width, height = 300, 400

rows = columns = 28

toolbar_height = height - width

pixel_size = width // columns

background = white

font_size = pygame.font.SysFont('arial', 22)