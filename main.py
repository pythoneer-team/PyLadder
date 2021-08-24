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


def button(text, xmouse, ymouse, x, y, width, height, int, new, size, btn_1):
    if x + width > xmouse > x and y + height > ymouse > y:
        pygame.draw.rect(game_layout, new, [
                         x - 2.5, y - 2.5, width + 5, height + 5])
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
        button("Rules", mouse[0], mouse[1], (width / 2 - 100), (height /
               2) + 220, 200, 100, (113, 207, 41, 1), (0, 230, 0), 60, 15)
        mouse = pygame.mouse.get_pos()

        if btn_player("Our Team", mouse[0], mouse[1], 1166, 0, 200, 50, (226, 135, 67), (245, 223, 173, 255), 30):
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
        btn_1 = button("Against Computer", mouse[0], mouse[1], (width / 2 - 150), 350, 350, 100, (113, 207, 41, 1),
                       (0, 230, 0), 40, "single")
        btn_2 = button("Back to Main", mouse[0], mouse[1], 0, 850,
                       300, 50, (27, 143, 190, 255), (255, 181, 114, 255), 30, 5)
        if btn_2 == 5:
            menu()
        if btn_1 == "single":
            playing(1)
        pygame.display.update()


starter()
menu()
