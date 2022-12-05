# importing stuff
 
import pygame
import time
import random
import threading
 
# initializing pygame
 
pygame.init()
 
# defining variables
 
clock = pygame.time.Clock()
autoATK = 0
coins = 0
display_width = 300
display_height = 450
black = (0, 0, 0)
light_blue = (173, 216, 230)
blue = (0, 100, 250)
green = (0, 255, 0)
red = (255, 0, 0)

# creating display and caption
 
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Dungeon Koala")
fsize = 20
font = pygame.font.Font('freesansbold.ttf', fsize)
 
# defining functions
 
def circle(display, color, x, y, radius):
    pygame.draw.circle(display, color, [x, y], radius)
    
def rectangle(display, color, x, y, w, h):
    pygame.draw.rect(display, color, (x, y, w, h))
    
def drawLifeBar(color, y_coord, level):

    pygame.draw.circle(gameDisplay, color, (40, y_coord), 20, 5)
    pygame.draw.rect(gameDisplay, color, [70, y_coord - 15, 200, 30])
    pygame.draw.rect(gameDisplay, color, [75, y_coord - 10, 190, 20])
    level_text = font.render(str(level), True, black)
    gameDisplay.blit(level_text, (30, y_coord - 10))

#def drawDamage(red, y_coord, draw, length):
  
def DrawText(text, Textcolor, Rectcolor, x, y, fsize):
    text = font.render(text, True, Textcolor, Rectcolor)
    textRect = text.get_rect()
    textRect.center = (x, y)
    gameDisplay.blit(text, textRect)

def drone():
    global autoATK
    global HP
    autoATK = 0
    HP = 10
    while True:
        HP = HP - autoATK
        time.sleep(0.1)

#loads background image
background = pygame.image.load("dungeon.png")
# Loads and loops background music
#pygame.mixer.music.load('synth_dungeon.wav')
#pygame.mixer.music.play(-1)


def main():
    global clock
    global autoATK
    global coins
    global HP
    global color
    global attack
    color = blue
    slime_count = 0
    autoATK = 0
    attack = 1
    cost = 10
    cost2 = 10
    HP = 10
    game_running = True
    while game_running:  
        
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mopos = pygame.mouse.get_pos()
                # attack slime
                if mopos >= (90, 0) and mopos <= (210, 0):
                    HP -= attack
                # select sword upgrade
                if mopos <= (300, 0) and mopos >= (280, 0) and coins >= cost:                    
                        coins = coins - cost
                        cost = cost * 1.5
                        attack = attack * 1.2
                        cost = round(cost, 0)
                # select drone upgrade
                if mopos >= (0, 0) and mopos <= (15, 0) and coins >= cost2:
                        coins = coins - cost2
                        cost2 = cost2 * 1.5
                        autoATK = autoATK + 0.5
                        cost2 = round(cost2, 0)
        if HP <= 0:
            color = (r,g,b)
            HP = 10
            coins += 1
            slime_count += 1
        
        # drawing graphics 
        gameDisplay.fill(light_blue)
        gameDisplay.blit(background, (-200,-125))
        DrawText("Dungeon Koala", black, light_blue, 150, 50, fsize)
        DrawText("wallet = " + str(f'{coins:.2f}') + " coins", black, light_blue, 110, 100, fsize)
        DrawText("slimes = " + str(slime_count), black, light_blue, 65, 120, fsize)
                
        # draw slime
        circle(gameDisplay, color, 150, 250, 60)
        circle(gameDisplay, black, 120, 250, 10)
        circle(gameDisplay, black, 180, 250, 10)
        rectangle(gameDisplay, black, 140, 280, 10, 10)
        # draw life bar
        # drawLifeBar(green, 330, 1)
        # draw damage
        DrawText("Slime HP = " + str(f'{HP:.2f}'), black, light_blue, 150, 330, fsize)
        # upgrade button (drone)
        DrawText("buy/upgrade ATK drone " + str(cost2), black, light_blue, 160, 370, fsize)
        circle(gameDisplay, blue, 11, 370, 10)
        # upgrade button (sword)
        DrawText("upgrade bamboo sword " + str(cost), black, light_blue, 150, 400, fsize)
        circle(gameDisplay, blue, 290, 400, 10)

        pygame.display.flip()
        clock.tick(60)
 
# ending the program
if __name__ == "__main__":
    x = threading.Thread(target = drone, daemon = True)
    x.start()
    main()
    pygame.quit()
    quit()
