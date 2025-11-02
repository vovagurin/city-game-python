import pygame
pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((900, 660), pygame.RESIZABLE)
pygame.display.set_caption("приключения в городе")
pygame.display.set_icon(pygame.image.load('Pr/лого.png').convert_alpha())