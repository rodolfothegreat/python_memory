import pygame, sys
from pygame.locals import *
import random
List1 = []
List2 = []
Exposed = []
state = 0
turns = 0
chosen = [-1, -1]
WHITE = (255, 255, 255)
GREEN = ( 0, 155, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 100)

def new_game():
    global turns
    global List1
    global List2
    global Exposed
    global state
    turns = 0
    state = 0
    List1 = []
    List2 = []
    Exposed = []
    for i in range(0, 8):
        List1.append(i)
        List2.append(i)
    List1.extend(List2)
    random.shuffle(List1)
    
    for i in range(0, 16):
        Exposed.append(0)
    #label.set_text("Turns = 0")
    
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global List1
    global Exposed
    global turns
    global chosen
    global state
    if (sum(Exposed) == 16):
        return
    card = pos[0] / 50
    if Exposed[card] == 1:
        return
    else:
        Exposed[card] = 1
    if state == 0:
        state = 1
        chosen[0] = card
    elif state == 1:
        state = 2
        turns = turns + 1
        #label.set_text("Turns = " + str(turns))
        chosen[1] = card
                                     
    else:
        if (List1[chosen[0]] !=List1[chosen[1]]):
            Exposed[chosen[0]] = 0
            Exposed[chosen[1]] = 0                         
        state = 1
        chosen[0] = card
    
    
def drawing(amode):
    global List1
    global Exposed
    amode.fill(BLUE)
    myfont = pygame.font.SysFont("monospace", 75)
    myfontsmall = pygame.font.SysFont("monospace", 25)
    labelturns = myfontsmall.render("Turns = " + str(turns),  2, (255,255,255))
    amode.blit(labelturns, (10, 100))
    for i in range(0, 16):
        if (Exposed[i] == 0):
		
	    pygame.draw.polygon(amode, GREEN, [[i * 50, 0], [i * 50 + 48, 0], [i * 50 + 48, 100], [i * 50, 100]])
        else:
	    pygame.draw.polygon(amode, GREEN, [[i * 50, 0], [i * 50 + 48, 0], [i * 50 + 48, 100], [i * 50, 100]])
	    label = myfont.render(str(List1[i]),  1, (255,255,0))
	    amode.blit(label, (i * 50, 10))
		

	
	

pygame.init()
new_game()
DISPLAYSURF = pygame.display.set_mode((800, 135))
pygame.display.set_caption('Memory! ')
DISPLAYSURF.fill(WHITE)
drawing(DISPLAYSURF)
while True: # main game loop
	for event in pygame.event.get():

		# handle MOUSEBUTTONUP
		if event.type == pygame.MOUSEBUTTONUP:
			pos = pygame.mouse.get_pos()
			pygame.display.set_caption('Memory! ' + str(pos))
			mouseclick(pos)
			drawing(DISPLAYSURF)
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	pygame.display.update()