# Importing
import pygame
from random import randint

clock = pygame.time.Clock()

# Initialization
pygame.init()
width = 1366
height = 768


# Icon layout and caption
icon = pygame.image.load("assets/icon.jpg")
game_layout = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pyladder Game")
pygame.display.set_icon(icon)
pygame.display.update()


Board = pygame.image.load("assets/Snakes_ladders_big_image.png")
Menu = pygame.image.load("assets/menu.jpg")
Background = pygame.image.load("assets/game_background.jpg")
ourrules = pygame.image.load("assets/rules.png")

back1 = pygame.image.load("assets/introduction_image.png")
back2 = pygame.image.load("assets/introduction_image2.png")
back3 = pygame.image.load("assets/introduction_image3.png")
back4 = pygame.image.load("assets/introduction_image4.png")
back5 = pygame.image.load("assets/introduction_image5.png")

asac_project = pygame.image.load("assets/ASAC.png")
asac_project = pygame.transform.smoothscale(asac_project, (width, height))

# All Point
red_token = pygame.image.load("assets/red.png")
red_token = pygame.transform.smoothscale(red_token, (36, 51))

blue_token = pygame.image.load("assets/blue.png")
blue_token = pygame.transform.smoothscale(blue_token, (36, 51))

# All Dice
dice1 = pygame.image.load("assets/dice_image1.png")
dice2 = pygame.image.load("assets/dice_image2.png")
dice3 = pygame.image.load("assets/dice_image3.png")
dice4 = pygame.image.load("assets/dice_image4.png")
dice5 = pygame.image.load("assets/dice_image5.png")
dice6 = pygame.image.load("assets/dice_image6.png")



# Position of mouse
mouse = pygame.mouse.get_pos()
click = pygame.mouse.get_pressed()

# Texts 
def display_text(text, x, y, fontsize):
    Textsize = pygame.font.SysFont("courier new", fontsize)
    text, TextBox = text_reshape(text, Textsize)
    TextBox.center = (x, y)
    game_layout.blit(text, TextBox)
# text reshape
def text_reshape(text, font):
    TextBox = font.render(text, True, (250, 250, 250))
    return TextBox, TextBox.get_rect()
# Message displaying for field
def display_text2(text, x, y, fontsize):
    Textsize = pygame.font.SysFont("courier new", fontsize)
    text, TextBox = text_reshape2(text, Textsize)
    TextBox.center = (x, y)
    game_layout.blit(text, TextBox)

def text_reshape2(text, font, c):
    TextBox = font.render(text, True, c)
    return TextBox, TextBox.get_rect()

# Goti movement function Yousef
def movement(a):
    l1 = [[406, 606], [456, 606], [506, 606], [556, 606], [606, 606], [656, 606], [706, 606], [756, 606], [806, 606],
          [856, 606], [906, 606], [906, 560], [856, 560], [806, 560], [756, 560], [706, 560], [656, 560], [606, 560],
          [556, 560], [506, 560], [456, 560], [456, 506], [506, 506], [556, 506], [606, 506], [656, 506], [706, 506],
          [756, 506], [806, 506], [856, 506], [906, 506], [906, 460], [856, 460], [806, 460], [756, 460], [706, 460],
          [656, 460], [606, 460], [556, 460], [506, 460], [456, 460], [456, 406], [506, 406], [556, 406], [606, 406],
          [656, 406], [706, 406], [756, 406], [806, 406], [856, 406], [906, 406], [906, 360], [856, 360], [806, 360],
          [756, 360], [706, 360], [656, 360], [606, 360], [556, 360], [506, 360], [456, 360], [456, 306], [506, 306],
          [556, 306], [606, 306], [656, 306], [706, 306], [756, 306], [806, 306], [856, 306], [906, 306], [906, 260],
          [856, 260], [806, 260], [756, 260], [706, 260], [656, 260], [606, 260], [556, 260], [506, 260], [456, 260],
          [456, 206], [506, 206], [556, 206], [606, 206], [656, 206], [706, 206], [756, 206], [806, 206], [856, 206],
          [906, 206], [906, 160], [856, 160], [806, 160], [756, 160], [706, 160], [656, 160], [606, 160], [556, 160],
          [506, 160], [456, 160]]
    l2 = l1[a]
    x = l2[0] - 25
    y = l2[1] - 25
    return x, y

def math():
    return True    

# Ladder check maram
def ladders(x):
    if x == 1:
        if math():
         return 38
        else:
         return 1
    elif x == 4:
        if math():
         return 14
        else:
         return 14
    elif x == 9:
        if math():
          return 31
        else:
         return 9
    elif x == 28:
        if math():
         return 84
        else:
         return 28
    elif x == 21:
        if math():
         return 42
        else:
         return 21
    elif x == 51:
        if math():
         return 67
        else:
         return 51
    elif x == 80:
        if math():
         return 99
        else:
         return 80 
    elif x == 72:
        if math():
         return 91
        else:
         return 72
    else:
        return x

# Snake Check Omar
def snakes(x):
    if x == 17:
        return 7
    elif x == 54:
        return 34
    elif x == 62:
        return 19
    elif x == 64:
        return 60
    elif x == 87:
        return 36
    elif x == 93:
        return 73
    elif x == 95:
        return 75
    elif x == 98:
        return 79
    else:
        return x
#  dices and thier images Yousef (to do: change time)
def dice(d):
    if d == 1:
        d = dice1
    elif d == 2:
        d = dice2
    elif d == 3:
        d = dice3
    elif d == 4:
        d = dice4
    elif d == 5:
        d = dice5
    elif d == 6:
        d = dice6
    time_clock = pygame.time.get_ticks()
    while pygame.time.get_ticks() - time_clock < 1000:
        game_layout.blit(d, (300, 500))
        pygame.display.update()

    # for mute and unmute


def btn_player(text, xmouse, ymouse, x, y, width, height, int, new, size):
    # mouse position
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + width > xmouse > x and y + height > ymouse > y:
        pygame.draw.rect(game_layout, new, [x - 2.5, y - 2.5, width + 5, height + 5])
        if pygame.mouse.get_pressed() == (1, 0, 0):
            return True
    else:
        pygame.draw.rect(game_layout, int, [x, y, width, height])
    display_text(text, (x + width + x) / 2, (y + height + y) / 2, size)

# Turn
def turn(sc, lefted, section):
   pass


# Quitting:
def Quit():
    pygame.quit()
    quit()


# Buttons:

def button(text, xmouse, ymouse, x, y, width, height, int, new, size,btn_1):
    if x + width > xmouse > x and y + height > ymouse > y:
        pygame.draw.rect(game_layout, new, [x - 2.5, y - 2.5, width + 5, height + 5])
        if pygame.mouse.get_pressed() == (1, 0, 0):
            if btn_1 == 1:
                chosen()
            # elif btn_1 == 15:
            #     rules()
            elif btn_1 == 0:
                Quit()
            elif btn_1 == "single":
                return btn_1
            else:
                return True
    else:
        pygame.draw.rect(game_layout, int, [x, y, width, height])
    display_text(text, (x + width + x) / 2, (y + height + y) / 2, size)
# game rules
def rules():
    while True:
        game_layout.blit(ourrules, (200, 100))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    Quit()
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if button("Back", mouse[0], mouse[1], width / 2 - 100, 700, 200, 50, (0, 230, 0), (0, 230, 0), 25, 20):
            pygame.display.update()

#  Game lunching
def starter():
    time_clock = pygame.time.get_ticks()
    while pygame.time.get_ticks() - time_clock < 2500:
        game_layout.blit(back1, (0, 0))
        pygame.display.update()
    while True:
        time_clock = pygame.time.get_ticks()
        while pygame.time.get_ticks() - time_clock < 500:
            game_layout.blit(back2, (0, 0))
            pygame.display.update()
        time_clock = pygame.time.get_ticks()
        while pygame.time.get_ticks() - time_clock < 500:
            game_layout.blit(back3, (0, 0))
            pygame.display.update()
        time_clock = pygame.time.get_ticks()
        while pygame.time.get_ticks() - time_clock < 500:
            game_layout.blit(back4, (0, 0))
            pygame.display.update()
        time_clock = pygame.time.get_ticks()
        while pygame.time.get_ticks() - time_clock < 500:
            game_layout.blit(back5, (0, 0))
            pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                return
        pygame.display.update()

# about our project and team members
def ASAC():
    while True:
        game_layout.blit(asac_project, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    Quit()
        # mouse position
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if button("Back", mouse[0], mouse[1], width / 2 - 120, 680, 200, 70, (113, 207, 41, 1), (0, 230, 0), 60, 15):
            menu()
        pygame.display.update()

# Main Menu of our game
def menu():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    Quit()
        # mouse position
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        game_layout.blit(Menu, (0, 0))
        button("Play", mouse[0], mouse[1], (width / 2 - 100), height / 2, 200, 100, (113, 207, 41, 1),
               (0, 230, 0), 60, 1)
        button("Quit", mouse[0], mouse[1], (width / 2 - 100), (height / 2) + 110, 200, 100, (113, 207, 41, 1),
               (0, 230, 0), 60, 0)
        button("Rules", mouse[0], mouse[1], (width / 2 - 100), (height / 2) + 220, 200, 100, (113, 207, 41, 1),(0, 230, 0), 60, 15)                                                                           
        mouse = pygame.mouse.get_pos()

        if btn_player("Our Team", mouse[0], mouse[1], 1166, 0, 200, 50, (226,135,67), (245,223,173,255), 30):
            ASAC()
        pygame.display.update()

# Options Menu:
def chosen():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    Quit()
        # mouse position
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        btn_1 = btn_2 = 1
        game_layout.blit(Menu, (0, 0))
        # Single player button
        btn_1 = button("Against Computer", mouse[0], mouse[1], (width / 2 - 150), 350, 350, 100,(113, 207, 41, 1),
               (0, 230, 0), 40,"single")
        btn_2 = button("Back to Main", mouse[0], mouse[1], 0, 850, 300, 50,(27,143,190,255), (255,181,114,255), 30, 5)
        if btn_2 == 5:
            menu()
        if btn_1 == "single":
            playing(1)
        pygame.display.update()


def playing(btn1):
    time = 3000
    while time<10000:
        game_layout.blit(Background, (0, 0))
        game_layout.blit(Board, (width / 2 - 250, height / 2 - 250))
        break

    
starter()
menu()
