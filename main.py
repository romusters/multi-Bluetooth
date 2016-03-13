import receiver
import sender

import module
import pygame

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)

rectA = [50, 300, 100, 50]
rectB = [350, 300, 100, 50]
rectC = [650, 300, 100, 50]

disableA = False
disableB = False
disableC = False

lineWidth = 5

def main():
	pygame.init()
	gameDisplay = pygame.display.set_mode((800,600))
	pygame.display.set_caption('TCP communication in multiple bluetooth modules.')
	pygame.display.update()

	font = pygame.font.SysFont(None, 30)

	gameExit = False

	while not gameExit:
		pos = None
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				gameExit = True
				pygame.quit()
				quit()
			if event.type == pygame.MOUSEBUTTONUP:
				pos = pygame.mouse.get_pos()
		gameDisplay.fill(white)

		drawA = pygame.draw.rect(gameDisplay, black, rectA)
		if(pos):
			if(drawA.collidepoint(pos)):
				global disableA
				disableA = not disableA
				pygame.draw.rect(gameDisplay, red, [rectA[0]+lineWidth, rectA[1]+lineWidth, rectA[2]-2*lineWidth, rectA[3]-2*lineWidth])#[410, 310, 80, 30])
		elif(disableA):
			pygame.draw.rect(gameDisplay, red, [rectA[0]+lineWidth, rectA[1]+lineWidth, rectA[2]-2*lineWidth, rectA[3]-2*lineWidth])#[410, 310, 80, 30])
		else:
			pygame.draw.rect(gameDisplay, white, [rectA[0]+lineWidth, rectA[1]+lineWidth, rectA[2]-2*lineWidth, rectA[3]-2*lineWidth])#[410, 310, 80, 30])
		screen_text = font.render("A", True, black)
		gameDisplay.blit(screen_text, [rectA[0]+45, rectA[1] +15])#[445, 315])



		drawB = pygame.draw.rect(gameDisplay, black, rectB)
		if(pos):
			if(drawB.collidepoint(pos)):
				global disableB
				disableB = not disableB
				pygame.draw.rect(gameDisplay, red, [rectB[0]+lineWidth, rectB[1]+lineWidth, rectB[2]-2*lineWidth, rectB[3]-2*lineWidth])#[410, 310, 80, 30])
		elif(disableB):
			pygame.draw.rect(gameDisplay, red, [rectB[0]+lineWidth, rectB[1]+lineWidth, rectB[2]-2*lineWidth, rectB[3]-2*lineWidth])#[410, 310, 80, 30])
		else:
			pygame.draw.rect(gameDisplay, white, [rectB[0]+lineWidth, rectB[1]+lineWidth, rectB[2]-2*lineWidth, rectB[3]-2*lineWidth])#[410, 310, 80, 30])
		screen_text = font.render("B", True, black)
		gameDisplay.blit(screen_text, [rectB[0]+45, rectB[1] +15])



		drawC = pygame.draw.rect(gameDisplay, black, rectC)
		if(pos):
			if(drawC.collidepoint(pos)):
				global disableC
				disableC = not disableC
				pygame.draw.rect(gameDisplay, red, [rectC[0]+lineWidth, rectC[1]+lineWidth, rectC[2]-2*lineWidth, rectC[3]-2*lineWidth])#[410, 310, 80, 30])
		elif(disableC):
			pygame.draw.rect(gameDisplay, red, [rectC[0]+lineWidth, rectC[1]+lineWidth, rectC[2]-2*lineWidth, rectC[3]-2*lineWidth])#[410, 310, 80, 30])
		else:
			pygame.draw.rect(gameDisplay, white, [rectC[0]+lineWidth, rectC[1]+lineWidth, rectC[2]-2*lineWidth, rectC[3]-2*lineWidth])#[410, 310, 80, 30])
		screen_text = font.render("C", True, black)
		gameDisplay.blit(screen_text, [rectC[0]+45, rectC[1] +15])

		pygame.display.update()

if __name__ == "__main__":
	#main()

	import time
	import module

	A = module.bluetoothModule(id = "A")
	B = module.bluetoothModule(id = "B")
	
	idx = 0
	while True:
		var = "ball"
		A.Ks = var
		if idx%4 == 0:
			B.Kr = 1
		if
		idx += 1
		time.sleep(1)
		if idx%4 == 0:

			print "B knows A knows vault"


			#B knows if there is a vault, then you need a code
			#C knows code
