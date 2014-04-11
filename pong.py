import pygame
from pygame.locals import *
from sys import exit
import random

pygame.init()

screen = pygame.display.set_mode((1024, 800))
clock = pygame.time.Clock()
pygame.display.flip()

x_pos = 0
y_pos = 0

x_=10
y_=10
while True:
	for event in pygame.event.get():

		if event.type == pygame.QUIT:
			exit()
	screen.fill((0, 255, 0))	
	pygame.draw.rect(screen, (255,255,255), pygame.Rect(y_pos, x_pos, 50, 50))
	pygame.display.flip()

	x_pos += x_
	y_pos += y_

	if x_pos+50 >= 800:
        	x_ = -1
	if x_pos <= 0:
                x_ = 1
        
	if y_pos+50 >= 1024:
                y_ = -1
	if y_pos <= 0:
                y_ = 1
	clock.tick_busy_loop(10)
	pygame.display.set_caption("fps: " + str(clock.get_fps()))

