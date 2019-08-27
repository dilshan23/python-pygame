import pygame, sys
from pygame.locals import *

pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Hello World!')

x = 100
y = 100

while True: # main game loop
	for event in pygame.event.get():
		if event.type == QUIT:
 			pygame.quit()
			sys.exit()

	keys = pygame.key.get_pressed()
	
	if keys[pygame.K_LEFT]:

			x -= 2

	if keys[pygame.K_RIGHT]:

			x += 2




			
			
	if keys[pygame.K_UP]:

			y -= 2
			
			
	if keys[pygame.K_DOWN]:

			y += 2

	DISPLAYSURF.fill((0,0,0))



	pygame.draw.rect(DISPLAYSURF,(255,0,0),(x,y,40,60))
 	pygame.display.update()



