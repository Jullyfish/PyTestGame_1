import pygame

displayWidth, displayHeight, displayFrame = 1280, 720, 0

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

bg = pygame.image.load('backgrounds/bg1.jpg')
playerStandRight = pygame.image.load('sprites/R0.png')
playerStandLeft = pygame.image.load('sprites/L0.png')

clock = pygame.time.Clock()

class player(object):
	def __init__(self, x, y, width, height):
		self.x = displayFrame
		self.y = displayHeight - height - displayFrame
		self.width = width
		self.height = height
		self.speed = 8
		self.isJump = False
		self.jumpCount = 10
		self.animCount = 0
		self.left = False
		self.right = False
		self.standRight = True
		self.standLeft = False

	def draw(self, win):
		if sharpshooter.animCount + 1 >= len(walkRight) * 3:
			sharpshooter.animCount = 0

		if sharpshooter.right:
			win.blit(walkRight[sharpshooter.animCount // 3], (sharpshooter.x, sharpshooter.y))	
			sharpshooter.animCount +=1
			sharpshooter.standRight, sharpshooter.standLeft = True, False
		elif sharpshooter.left:
			win.blit(walkLeft[sharpshooter.animCount // 3], (sharpshooter.x, sharpshooter.y))	
			sharpshooter.animCount +=1	
			sharpshooter.standRight, sharpshooter.standLeft = False, True	
		else:
			if sharpshooter.standRight:
				win.blit(playerStandRight, (sharpshooter.x, sharpshooter.y))
			elif sharpshooter.standLeft:
				win.blit(playerStandLeft, (sharpshooter.x, sharpshooter.y))	


def drawWindow():
	win.blit(bg, (0, 0))	
	sharpshooter.draw(win)
	pygame.display.update()	


sharpshooter = player(1000, 1000, 48, 96)
run = True
while run:
	clock.tick(30)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	keys = pygame.key.get_pressed()
	if keys[pygame.K_ESCAPE]:
		run = False		

	if keys[pygame.K_LEFT] and sharpshooter.x > displayFrame:
		sharpshooter.x -= sharpshooter.speed		
		sharpshooter.left = True
		sharpshooter.right = False
	elif keys[pygame.K_RIGHT] and sharpshooter.x < displayWidth - displayFrame - sharpshooter.width:
		sharpshooter.x += sharpshooter.speed
		sharpshooter.left = False
		sharpshooter.right = True
	else:
		sharpshooter.left = False
		sharpshooter.right = False
		sharpshooter.animCount = 0 	

	if not(sharpshooter.isJump):	
		if keys[pygame.K_SPACE]:
			sharpshooter.isJump = True		
	else:
		if sharpshooter.jumpCount >= -10:
			if sharpshooter.jumpCount < 0:
				sharpshooter.y += (sharpshooter.jumpCount ** 2) / 2
			else:	
				sharpshooter.y -= (sharpshooter.jumpCount ** 2) / 2
			sharpshooter.jumpCount -= 1
		else:
			sharpshooter.isJump = False
			sharpshooter.jumpCount = 10	

	drawWindow()		

pygame.quit()			