import pygame

displayWidth, displayHeight, displayFrame = 1280, 720, 5

pygame.init()
win = pygame.display.set_mode((displayWidth, displayHeight)) #, pygame.FULLSCREEN

pygame.display.set_caption('Test Game')


#<sprites>

walk = [
pygame.image.load('sprites/R2.png'), pygame.image.load('sprites/R3.png'), pygame.image.load('sprites/R4.png'),
pygame.image.load('sprites/R5.png'), pygame.image.load('sprites/R6.png'), pygame.image.load('sprites/R7.png'),
pygame.image.load('sprites/R8.png'), pygame.image.load('sprites/R9.png'),pygame.image.load('sprites/R10.png')]

playerJump = pygame.image.load('sprites/RJump.png')

bg = pygame.image.load('backgrounds/bg1.jpg')
playerStand = pygame.image.load('sprites/R0.png')

#</sprites>

clock = pygame.time.Clock()

class player(object):
	def __init__(self, x, y, width, height):
		self.x = x #displayFrame 
		self.y = y #displayHeight - height - 10 
		self.width = width #hitbox size
		self.height = height #hitbox size
		self.speed = 8
		self.isJump = False
		self.jumpCount = 10
		self.animCount = 0
		self.left = False
		self.right = False
		self.standRight = True
		self.standLeft = False		

	def draw(self, win):
		if sharpshooter.animCount + 1 >= len(walk) * 3:
			sharpshooter.animCount = 0

		if sharpshooter.isJump and sharpshooter.standRight:
			win.blit(playerJump, (sharpshooter.x, sharpshooter.y))	
		elif sharpshooter.isJump and sharpshooter.standLeft:
			win.blit(pygame.transform.flip(playerJump, True, False), (sharpshooter.x, sharpshooter.y))	
		elif sharpshooter.right:
			win.blit(walk[sharpshooter.animCount // 3], (sharpshooter.x, sharpshooter.y))	
			sharpshooter.animCount +=1
			sharpshooter.standRight, sharpshooter.standLeft = True, False
		elif sharpshooter.left:
			win.blit(pygame.transform.flip(walk[sharpshooter.animCount // 3], True, False), (sharpshooter.x, sharpshooter.y))	
			sharpshooter.animCount +=1	
			sharpshooter.standRight, sharpshooter.standLeft = False, True	
		elif sharpshooter.standRight:
			win.blit(playerStand, (sharpshooter.x, sharpshooter.y))
		elif sharpshooter.standLeft:
			win.blit(pygame.transform.flip(playerStand, True, False), (sharpshooter.x, sharpshooter.y))	


class projectile(object):
	def __init__(self, x, y, radius, color, facing):
		self.x = x
		self.y = y			
		self.radius = radius
		self.color = color
		self.facing = facing
		if sharpshooter.standRight:
			self.speed = 16
		elif sharpshooter.standLeft:
			self.speed = -16	

	def	draw(self, win):
		pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)


def drawWindow():
	win.blit(bg, (0, 0))
	#pygame.draw.rect(win, (255, 255, 255), 
	#(sharpshooter.x, sharpshooter.y, sharpshooter.width, sharpshooter.height), 2) #draw hitbox	
	sharpshooter.draw(win) 
	for bullet in bullets:
		bullet.draw(win)
	pygame.display.update()	


sharpshooter = player(0, displayHeight - 240, 40, 80)
bullets = []
run = True
while run:
	clock.tick(30)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	for bullet in bullets:
		if bullet.x < displayWidth and bullet.x > 0:
			bullet.x += bullet.speed
		else:
			bullets.pop(bullets.index(bullet))	

	keys = pygame.key.get_pressed()

	if keys[pygame.K_ESCAPE]:
		run = False		

	if keys[pygame.K_s]:
		bullets.append(projectile(round(sharpshooter.x + sharpshooter.width // 2), 
		round(sharpshooter.y + sharpshooter.height // 2), 6, (0,0,0), 1))	

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
		if keys[pygame.K_UP]:
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