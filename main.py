import pygame

displayWidth, displayHeight, displayFrame = 1280, 720, 50

pygame.init()
win = pygame.display.set_mode((displayWidth, displayHeight))

pygame.display.set_caption('Test Game')

walkRight = [
pygame.image.load('sprites/R2.png'), pygame.image.load('sprites/R3.png'), pygame.image.load('sprites/R4.png'),
pygame.image.load('sprites/R5.png'), pygame.image.load('sprites/R6.png'), pygame.image.load('sprites/R7.png'),
pygame.image.load('sprites/R8.png'), pygame.image.load('sprites/R9.png'),pygame.image.load('sprites/R10.png')]

walkLeft = [
pygame.image.load('sprites/L2.png'), pygame.image.load('sprites/L3.png'), pygame.image.load('sprites/L4.png'), 
pygame.image.load('sprites/L5.png'), pygame.image.load('sprites/L6.png'), pygame.image.load('sprites/L7.png'), 
pygame.image.load('sprites/L8.png'), pygame.image.load('sprites/L9.png'), pygame.image.load('sprites/L10.png')]

playerStandRight = pygame.image.load('sprites/R0.png')
playerStandLeft = pygame.image.load('sprites/L0.png')

clock = pygame.time.Clock()

width = 50
height = 50

x = displayFrame
y = displayHeight - height - displayFrame
speed = 8

left, right = False, False
animCount = 0
standRight, standLeft = True, False

isJump = False
jumpCount = 10

def drawWindow():
	global animCount, standRight, standLeft 

	win.fill((0, 0, 0))

	if animCount + 1 >= len(walkRight) * 3:
		animCount = 0

	if right:
		win.blit(walkRight[animCount // 3], (x, y))	
		animCount +=1
		standRight, standLeft = True, False
	elif left:
		win.blit(walkLeft[animCount // 3], (x, y))	
		animCount +=1	
		standRight, standLeft = False, True	
	else:
		if standRight:
			win.blit(playerStandRight, (x, y))
		elif standLeft:
			win.blit(playerStandLeft, (x, y))		

		
	#pygame.draw.rect(win, (0, 150, 0), (x, y, width, height))	
	pygame.display.update()	

run = True
while run:
	clock.tick(30)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	keys = pygame.key.get_pressed()
	if keys[pygame.K_ESCAPE]:
		run = False		

	if keys[pygame.K_LEFT] and x > displayFrame:
		x -= speed		
		left = True
		right = False
	elif keys[pygame.K_RIGHT] and x < displayWidth - displayFrame - width:
		x += speed
		left = False
		right = True
	else:
		left = False
		right = False
		animCount = 0 	

	if not(isJump):	
		if keys[pygame.K_SPACE]:
			isJump = True		
	else:
		if jumpCount >= -10:
			if jumpCount < 0:
				y += (jumpCount ** 2) / 2
			else:	
				y -= (jumpCount ** 2) / 2
			jumpCount -= 1
		else:
			isJump = False
			jumpCount = 10	

	drawWindow()		

pygame.quit()			