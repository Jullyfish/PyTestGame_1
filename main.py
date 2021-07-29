import pygame

displayWidth, displayHeight, displayFrame = 1280, 720, 50

pygame.init()
win = pygame.display.set_mode((displayWidth, displayHeight))

pygame.display.set_caption('Test Game')

walkRight = [pygame.image.load('sprites/1.png'), pygame.image.load('sprites/2.png'), 
pygame.image.load('sprites/3.png'), pygame.image.load('sprites/4.png'), pygame.image.load('sprites/5.png'),
pygame.image.load('sprites/6.png'), pygame.image.load('sprites/7.png'), pygame.image.load('sprites/8.png'),
pygame.image.load('sprites/9.png'), pygame.image.load('sprites/10.png'), pygame.image.load('sprites/11.png')]

playerStand = pygame.image.load('sprites/0.png')

clock = pygame.time.Clock()

width = 50
height = 50

x = displayFrame
y = displayHeight - height - displayFrame
speed = 5

left, right = False, False
animCount = 0

isJump = False
jumpCount = 10

def drawWindow():
	global animCount 

	win.fill((0, 0, 0))

	if animCount + 1 >= 30:
		animCount = 0

	if right:
		win.blit(walkRight[animCount // 3], (x, y))	
		animCount +=1
	elif left:
		win.blit(walkRight[animCount // 5], (x, y))	
		animCount +=1	
	else:
		win.blit(playerStand, (x, y))	

		
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