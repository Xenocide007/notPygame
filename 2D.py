mouseCO = "Mario.png"
running = True
import os

import random
import pygame, sys
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((800, 600))

mouseC = pygame.image.load(mouseCO).convert_alpha()

x, y = 0,0
movex, movey = 0, 0


lead_x = 400
lead_y = 300
lead_x_change = 0
lead_y_change = 0

clock = pygame.time.Clock()


gameExit = False
while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		if event.type == KEYDOWN:
			if event.key == K_LEFT:
				movex = -10
			elif event.key == K_RIGHT:
				movex = +10
			elif event.key == K_UP:
				movey = -10
			elif event.key == K_DOWN:
				movey = +10
		if event.type == KEYUP:
			if event.key == K_LEFT:
				movex = 0
			elif event.key == K_RIGHT:
				movex = 0
			elif event.key == K_UP:
				movey = 0
			elif event.key == K_DOWN:
				movey = 0
	

	while not gameExit:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				gameExit = True
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					lead_x_change = -5
					lead_y_change = 0
				if event.key == pygame.K_RIGHT:
					lead_x_change = 5
					lead_y_change = 0
				if event.key == pygame.K_UP:
					lead_y_change = -5
					lead_x_change = 0
				if event.key == pygame.K_DOWN:
					lead_y_change = 5
					lead_x_change = 0
	if lead_x > 800:
		lead_x_change = -5
	if lead_x < 0:
		lead_x_change = 5
	if lead_y > 600:
		lead_y_change = -5
	if lead_y < 0:
		lead_y_change = 5
	x+= movex
	y+= movey

	random = (180,40,180)
	screen.fill(random)
	screen.blit(screen, (0, 0))
	screen.blit(mouseC, (x, y))

	pygame.display.update()
