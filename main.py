import pygame
from random import randint

time_clocks = pygame.time.Clock()
pygame.init()
width = 1366
height = 768

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

mouse = pygame.mouse.get_pos()
click = pygame.mouse.get_pressed()


def movement(a):
    l1 = [[406, 606], [456, 606], [506, 606], [556, 606], [606, 606], [656, 606], [706, 606], [756, 606], [806, 606],
          [856, 606], [906, 606], [906, 560], [856, 560], [806, 560], [
              756, 560], [706, 560], [656, 560], [606, 560],
          [556, 560], [506, 560], [456, 560], [456, 506], [506, 506], [
              556, 506], [606, 506], [656, 506], [706, 506],
          [756, 506], [806, 506], [856, 506], [906, 506], [906, 460], [
              856, 460], [806, 460], [756, 460], [706, 460],
          [656, 460], [606, 460], [556, 460], [506, 460], [456, 460], [
              456, 406], [506, 406], [556, 406], [606, 406],
          [656, 406], [706, 406], [756, 406], [806, 406], [856, 406], [
              906, 406], [906, 360], [856, 360], [806, 360],
          [756, 360], [706, 360], [656, 360], [606, 360], [556, 360], [
              506, 360], [456, 360], [456, 306], [506, 306],
          [556, 306], [606, 306], [656, 306], [706, 306], [756, 306], [
              806, 306], [856, 306], [906, 306], [906, 260],
          [856, 260], [806, 260], [756, 260], [706, 260], [656, 260], [
              606, 260], [556, 260], [506, 260], [456, 260],
          [456, 206], [506, 206], [556, 206], [606, 206], [656, 206], [
              706, 206], [756, 206], [806, 206], [856, 206],
          [906, 206], [906, 160], [856, 160], [806, 160], [756, 160], [
              706, 160], [656, 160], [606, 160], [556, 160],
          [506, 160], [456, 160]]
    l2 = l1[a]
    x = l2[0] - 25
    y = l2[1] - 25
    return x, y


def message_display_screen(text, x, y, fs):
    largeText = pygame.font.Font('freesansbold.ttf', fs)
    TextSurf, TextRect = text_objects_screen(text, largeText)
    TextRect.center = (x, y)
    game_layout_display.blit(TextSurf, TextRect)


def text_objects_screen(text, font):
    textSurface = font.render(text, True, black_color)
    return textSurface, textSurface.get_rect()


def message_display1_screen(text, x, y, fs, c):
    largeText = pygame.font.Font('freesansbold.ttf', fs)
    TextSurf, TextRect = text_objects1(text, largeText)
    TextRect.center = (x, y)
    game_layout_display.blit(TextSurf, TextRect)


def text_objects1(text, font):
    textSurface = font.render(text, True, blue_color)
    return textSurface, textSurface.get_rect()


def text_objects1_screen(text, font, c):
    textSurface = font.render(text, True, c)
    return textSurface, textSurface.get_rect()


def Quit():
    pygame.quit()
    quit()


def button(t, xm, ym, x, y, wid, hei, int, after, fast, best):
    if x + wid > xm > x and y + hei > ym > y:
        pygame.draw.rect(game_layout_display, after, [
                         x - 2.5, y - 2.5, wid + 5, hei + 5])
        if pygame.mouse.get_pressed() == (1, 0, 0):
            if best == 1:
                choice()
            elif best == 5:
                return 5
            elif best == 15:
                rules()
            elif best == 0:
                Quit()
            elif best == "s" or best == 2 or best == 3 or best == 4:
                return best
            elif best == 7:
                choice()
            else:
                return True
    else:
        pygame.draw.rect(game_layout_display, int, [x, y, wid, hei])
    message_display_screen(t, (x + wid + x) / 2, (y + hei + y) / 2, fast)


def introduction():
    time_clock = pygame.time.get_ticks()
    while pygame.time.get_ticks() - time_clock < 2500:
        game_layout_display.blit(initial_background, (0, 0))
        pygame.display.update()
    while True:
        time_clock = pygame.time.get_ticks()
        while pygame.time.get_ticks() - time_clock < 500:
            game_layout_display.blit(initial_background2, (0, 0))
            pygame.display.update()
        time_clock = pygame.time.get_ticks()
        while pygame.time.get_ticks() - time_clock < 500:
            game_layout_display.blit(initial_background3, (0, 0))
            pygame.display.update()
        time_clock = pygame.time.get_ticks()
        while pygame.time.get_ticks() - time_clock < 500:
            game_layout_display.blit(initial_background4, (0, 0))
            pygame.display.update()
        time_clock = pygame.time.get_ticks()
        while pygame.time.get_ticks() - time_clock < 500:
            game_layout_display.blit(initial_background5, (0, 0))
            pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                return
        pygame.display.update()


def creditation():
    while True:
        game_layout_display.blit(creditations1, (200, 100))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    Quit()
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if button("Back", mouse[0], mouse[1], width_screen / 2 - 100, 700, 200, 50, red_color, blue_red_color, 25, 20):
            pygame.display.update()


def rules():
    while True:
        game_layout_display.blit(ruless, (200, 100))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    Quit()
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if button("Back", mouse[0], mouse[1], width_screen / 2 - 100, 700, 200, 50, red_color, blue_green_color, 25, 20):
            pygame.display.update()


def button2(t, xm, ym, x, y, wid, hei, int, after, fast):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + wid > xm > x and y + hei > ym > y:
        pygame.draw.rect(game_layout_display, after, [
                         x - 2.5, y - 2.5, wid + 5, hei + 5])
        if pygame.mouse.get_pressed() == (1, 0, 0):
            return True

    else:
        pygame.draw.rect(game_layout_display, int, [x, y, wid, hei])
    message_display_screen(t, (x + wid + x) / 2, (y + hei + y) / 2, fast)

    m = True
    while m:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    Quit()

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        game_layout_display.blit(menu_background, (0, 0))
        button("Play", mouse[0], mouse[1], (width_screen / 2 - 100), height_screen / 2, 200, 100, green_color,
               blue_green_color, 60, 1)

        button("Quit", mouse[0], mouse[1], (width_screen / 2 - 100), (height_screen / 2) + 110, 200, 100, green_color,
               blue_green_color, 60, 0)

        button("Rules", mouse[0], mouse[1], (width_screen / 2 - 100), (height_screen / 2) + 220, 200, 100, green_color,
               blue_green_color, 60, 15)

        mouse = pygame.mouse.get_pos()

        if button2("Our Team", mouse[0], mouse[1], 1166, 700, 200, 50, purple_color, blue_purple_color, 25):
            creditation()

        pygame.display.update()


def choice():
    f = True
    while f == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    Quit()
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        best1 = best2 = best3 = best4 = best5 = -1
        game_layout_display.blit(menu_background, (0, 0))

        pygame.display.update()


introduction()
