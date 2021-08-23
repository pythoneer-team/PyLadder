import pygame
from random import randint

time_clocks = pygame.time.Clock()
pygame.init()
width_screen = 1366
height_screen = 768

ic = pygame.image.load("resources/icon.png")
game_layout_display = pygame.display.set_mode((width_screen, height_screen))
pygame.display.set_caption("Snakes and Ladders Game ")
pygame.display.set_icon(ic)
pygame.display.update()
black_color = (10, 10, 10)
white_color = (250, 250, 250)
red_color = (200, 0, 0)
blue_red_color = (240, 0, 0)
green_color = (0, 200, 0)
blue_green_color = (0, 230, 0)
blue_color = (0, 0, 200)
grey_color = (50, 50, 50)
yellow_color = (150, 150, 0)
purple_color = '#BFA2DB'
blue_purple_color = (60, 0, 190)

menu_background = pygame.image.load("resources/menu.jpg")
post = pygame.image.load("resources/game_background.jpg")
initial_background = pygame.image.load("resources/introduction_image.png")
initial_background2 = pygame.image.load("resources/introduction_image2.png")
initial_background3 = pygame.image.load("resources/introduction_image3.png")
initial_background4 = pygame.image.load("resources/introduction_image4.png")
initial_background5 = pygame.image.load("resources/introduction_image5.png")
creditations1 = pygame.image.load("resources/owner.png")
ruless = pygame.image.load("resources/rules.png")


mouse = pygame.mouse.get_pos()
click = pygame.mouse.get_pressed()


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
