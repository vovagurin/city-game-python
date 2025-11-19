import pygame
import helper

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((900, 660))
pygame.display.set_caption("приключения в городе")
pygame.display.set_icon(pygame.image.load(helper.resource_path('Pr/logo.png')).convert_alpha())
