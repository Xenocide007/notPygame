import pygame
from pygame.locals import *
pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)

displayWidth = 800
displayHeight = 600
speed = 5
rektWidth = 10
rektHeight = 10

gameDisplay = pygame.display.set_mode((displayWidth, displayHeight))
pygame.display.set_caption("Stuff")

lead_x = displayWidth/2
lead_y = displayHeight/2
lead_x_change = 0
lead_y_change = 0

clock = pygame.time.Clock()


gameExit = False

while not gameExit:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameExit = True
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				lead_x_change = -speed
				lead_y_change = 0
			if event.key == pygame.K_RIGHT:
				lead_x_change = speed
				lead_y_change = 0
			if event.key == pygame.K_UP:
				lead_y_change = -speed
				lead_x_change = 0
			if event.key == pygame.K_DOWN:
				lead_y_change = speed
				lead_x_change = 0
	if lead_x >= displayWidth:
		lead_x_change = -speed
	if lead_x <= 0:
		lead_x_change = speed
	if lead_y >= displayHeight:
		lead_y_change = -speed
	if lead_y <= 0:
		lead_y_change = speed		


	lead_x += lead_x_change
	lead_y += lead_y_change
	gameDisplay.fill(white)
	pygame.draw.rect(gameDisplay, black, [lead_x, lead_y, rektWidth, rektHeight])
	pygame.display.update()

	clock.tick(100)


pygame.quit()
quit()