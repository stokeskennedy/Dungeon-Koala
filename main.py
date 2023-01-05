# imports
import pygame, random, sys, time, threading
from pygame.locals import *
from button import *
from player import *
from enemy import *

# initializing pygame
pygame.init()
pygame.mixer.init()
 
# defining variables
droneATK = 0
coins = 0
sword_cost = 10
drone_cost = 10

# setting display parameters and clock
FPS = 60
clock = pygame.time.Clock()
display_width = 300
display_height = 450

# create colors
black = (0, 0, 0)
grey = (20,20,20)
blue = (0, 100, 250)
light_blue = (173, 216, 230)
green = (0, 255, 0)
red = (255, 0, 0)


# create game display, caption, and font
screen = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Dungeon Koala")
fsize = 18
font = pygame.font.Font('freesansbold.ttf', fsize)

# Class definitions
class Slime:
    def __init__(self, x_pos, y_pos, color, enabled):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.color = color
        self.draw_slime()
        self.enabled = enabled

    def draw_slime(self):
        self.enabled = True
        button_rect = pygame.rect.Rect((self.x_pos, self.y_pos), (150, 150))
        pygame.draw.rect(screen, color, button_rect, 0, 5)
        pygame.draw.rect(screen, black, button_rect, 2, 5)
        if self.enabled:
            if self.click_slime():
                pygame.draw.rect(screen, black, (140, 250, 25, 25))
                pygame.draw.rect(screen, red, button_rect, 2, 5)
            else:
                pygame.draw.rect(screen, color, button_rect, 0, 5)
                pygame.draw.rect(screen, black, button_rect, 2, 5)
        # draw features vvvv
        # left eye
        pygame.draw.circle(screen, black, (110, 200), 20, 20)
        # right eye
        pygame.draw.circle(screen, black, (190, 200), 20, 20)
        # mouth
        pygame.draw.rect(screen, black, (140, 250, 20, 15))

    def click_slime(self):
        mouse_pos = pygame.mouse.get_pos()
        left_click = pygame.mouse.get_pressed()[0]
        button_rect = pygame.rect.Rect((self.x_pos, self.y_pos), (150, 150))
        if left_click and button_rect.collidepoint(mouse_pos) and self.enabled:
            return True
        else:
            return False
    def __str__(self):
        return self.x_pos, self.y_pos, self.color, self.enabled
          
# function definitions
def circle(display, color, x, y, radius):
    pygame.draw.circle(display, color, [x, y], radius)
    
def rectangle(display, color, x, y, w, h):
    pygame.draw.rect(display, color, (x, y, w, h))
    
def drawLifeBar(color, y_coord, level):

    pygame.draw.circle(screen, color, (40, y_coord), 20, 5)
    pygame.draw.rect(screen, color, [70, y_coord - 15, 200, 30])
    pygame.draw.rect(screen, color, [75, y_coord - 10, 190, 20])
    level_text = font.render(str(level), True, black)
    screen.blit(level_text, (30, y_coord - 10))

def drawDamage(red, y_coord, draw, length):
    pass
  
def DrawText(text, Textcolor, Rectcolor, x, y, fsize):
    text = font.render(text, True, Textcolor, Rectcolor)
    textRect = text.get_rect()
    textRect.center = (x, y)
    screen.blit(text, textRect)

def drone():
    global droneATK
    global e
    e = Enemy(10, 1)
    droneATK = 0
    while True:
        e.hp = e.hp - droneATK
        time.sleep(0.1)

# load background image
background = pygame.image.load("dungeon.png").convert()
# Loads and loops background music
##### pygame.mixer.music.load('synth_dungeon.wav')
##### pygame.mixer.music.play(-1)

def main():
    global p, e
    global clock
    global droneATK
    global coins
    global color
    global sword_cost
    global drone_cost
    color = blue
    slime_count = 0
    droneATK = 0
    sword_cost = 10
    drone_cost = 10
    game_running = True
    
    p = Player(100, 1)
    e = Enemy(10, 1)
    
    while game_running:  
        
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                # attack slime
                if slime.click_slime():
                    e.hp -= p.atk
                # select sword upgrade
                if sword_button.check_click() and coins >= sword_cost:
                        coins = coins - sword_cost
                        sword_cost = sword_cost * 1.5
                        p.atk = p.atk * 1.2
                        sword_cost = round(sword_cost, 0)
                # select drone upgrade
                if drone_button.check_click() and coins >= drone_cost:
                        coins = coins - drone_cost
                        drone_cost = drone_cost * 1.5
                        droneATK = droneATK + 0.5
                        drone_cost = round(drone_cost, 0)
        # change color, reset HP, and increment coins & slime_count variables once HP is <= 0                
        if e.hp <= 0:
            color = (r,g,b)
            p.hp = 100
            e.hp = 10
            coins += 1
            slime_count += 1

        # draw background and text
        screen.fill(light_blue)
        screen.blit(background, (-200,-125))
        DrawText("Dungeon Koala", black, light_blue, 150, 50, fsize)
        DrawText("wallet = " + str(int(coins)) + " coins", black, light_blue, 110, 100, fsize)
        DrawText("slimes = " + str(slime_count), black, light_blue, 85, 120, fsize)
               
        # draw slime
        slime = Slime(75, 150, color, True)
        # draw life bar
        #### drawLifeBar(green, 330, 1)
        DrawText("Slime HP = " + str(int(e.hp)), black, light_blue, 150, 330, fsize)
        # upgrade button (drone)
        if coins >= drone_cost:
            drone_button = Button('Buy/Upgrade ATK Drone ' + str(int(drone_cost)), 5, 350, True)
        else:
            drone_button = Button('Buy/Upgrade ATK Drone ' + str(int(drone_cost)), 5, 350, False)
        # upgrade button (sword)
        if coins >= sword_cost:
            sword_button = Button("Upgrade Bamboo Sword " + str(int(sword_cost)), 5, 400, True)
        else:
            sword_button = Button("Upgrade Bamboo Sword "  + str(int(sword_cost)), 5, 400, False)
        
        print(p.__str__())
        print(e.__str__())
        pygame.display.flip()
        clock.tick(FPS)
 
# ending the program
if __name__ == "__main__":
    drone_thread = threading.Thread(target = drone, daemon = True)
    drone_thread.start()
    main()
    pygame.quit()
    quit()