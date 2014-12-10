import pygame, time
from pygame.locals import *

pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)

displayWidth = 800
dispalyHeight = 600
speed = 5
rektWidth = 10
rektHeight = 10
fontSize = 25

gameDisplay = pygame.display.set_mode((displayWidth, displayHeight))
gameDisplay.fill(white)
pygame.display.set_caption("Stuff")

lead_x = displayWidth/2
lead_y = displayHeight/2
lead_x_change = 0
lead_y_change = 0

clock = pygame.time.Clock()

font = pygame.font.SysFont(None, fontSize)

def message_to_screen(msg, color):
	screen_text = font.render(msg, True, color)
	gameDisplay.blit(screen_text, [displayWidth/2, displayHeight/2])





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
		message_to_screen("boing", red)
	if lead_x <= 0:
		lead_x_change = speed
		message_to_screen("boing", red)
	if lead_y >= displayHeight:
		lead_y_change = -speed
		message_to_screen("boing", red)
	if lead_y <= 0:
		lead_y_change = speed
		message_to_screen("boing", red)		


	lead_x += lead_x_change
	lead_y += lead_y_change
	pygame.draw.rect(gameDisplay, black, [lead_x, lead_y, rektWidth, rektHeight])
	pygame.display.update()

	clock.tick(999)

pygame.quit()
quit()