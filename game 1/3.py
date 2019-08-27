import pygame, sys
from pygame.locals import *

pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Hello World!')

x = 100
y = 100

isJump = False
jumpcount = 10

while True: # main game loop
	for event in pygame.event.get():
		if event.type == QUIT:
 			pygame.quit()
			sys.exit()

	keys = pygame.key.get_pressed()
	
	if keys[pygame.K_LEFT]:

			x -= 2

			if x == 0 :
				x += 2

	if keys[pygame.K_RIGHT]:

			x += 2

			if x == 360:

				x -= 2

	if not isJump:

		if keys[pygame.K_UP]:

			y -= 2

			if y == 0:
				y += 2
			
			
		if keys[pygame.K_DOWN]:

			y += 2

			if y == 240:

				y -=2
		if keys[pygame.K_SPACE]:
			isJump = True


	else:

		if jumpcount >= -10:
			y -= (jumpcount ** 2) * 0.5
			jumpcount -= 1


		
		else:
			isJump = False
			jumpcount = 10




    	










			
			
	
	
	DISPLAYSURF.fill((0,0,0))



	pygame.draw.rect(DISPLAYSURF,(255,0,0),(x,y,40,60))
 	pygame.display.update()



