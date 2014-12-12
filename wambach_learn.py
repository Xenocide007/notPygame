import pygame
import time

pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)

display_with = 800
display_hight = 600

gameDisplay = pygame.display.set_mode ((display_with, display_hight))
pygame.display.set_caption("Slither")

gameExit = False

lead_x = display_with/2
lead_y = display_hight/2

lead_x_change = 0
lead_y_change = 0

clock = pygame.time.Clock()

block_size = 10
FPS = 30

font = pygame.font.SysFont(None, 25)

def message_to_screen(msg,color):
	screen_text = font.render(msg, True, color)
	gameDisplay.blit(screen_text, [display_with/2, display_hight/2])



while not gameExit:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameExit = True 
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				lead_x_change = -block_size
				lead_y_change = 0
			elif event.key == pygame.K_RIGHT:
				lead_x_change = block_size
				lead_y_change = 0
			elif event.key == pygame.K_UP:
				lead_y_change = -block_size
				lead_x_change =0
			elif event.key == pygame.K_DOWN:
				lead_y_change = block_size
				lead_x_change = 0

		if lead_x >= display_with or lead_x < 0 or lead_y >= display_hight or lead_y < 0:
			gameExit = True



	lead_x += lead_x_change
	lead_y += lead_y_change
	gameDisplay.fill(white)
	pygame.draw.rect(gameDisplay, black, [lead_x,lead_y,block_size,block_size])
	pygame.display.update()

	clock.tick(FPS)
	
message_to_screen("You lose", red)
pygame.display.update()
time.sleep(2)
pygame.quit()
quit()