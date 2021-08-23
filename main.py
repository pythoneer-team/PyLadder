

import pygame


# Initializing pygame
pygame.init()
width_screen = 1366
height_screen = 768

#title and icon
pygame.display.set_caption("PyLadder")
icon = pygame.image.load("img/game.png")
pygame.display.set_icon(icon)

window = pygame.display.set_mode((width_screen, height_screen ))
clock = pygame.time.Clock()
window_height = window.get_height()
window_width = window.get_width()
main_bg_file = pygame.image.load("img/back.jpg")
main_bg = pygame.transform.smoothscale(main_bg_file, (width_screen, height_screen ))



# green, blue colour .
white=(255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)

X = 1350
Y = 1050


font = pygame.font.Font('freesansbold.ttf', 50)
text = font.render('Quit', True,  white, blue)
textRect = text.get_rect()
textRect.center = (X//2, Y//2)

X1 = 1150
Y1 = 870
font1 = pygame.font.Font('freesansbold.ttf', 50)
text1 = font1.render('Instractions', True, white, blue)
textRect1 = text.get_rect()
textRect1.center = (X1//2, Y1//2)

X2 = 1350
Y2 = 680
font2 = pygame.font.Font('freesansbold.ttf', 50)
text2 = font2.render('Play', True, white, blue)
textRect2 = text.get_rect()
textRect2.center = (X2//2, Y2//2)

# def button(t, xm, ym, x, y, wid, hei, int, after, fast, best):
#   mouse = pygame.mouse.get_pos()
#   click = pygame.mouse.get_pressed()
#
# window.blit(main_bg_file, (0, 0))
# button(text2, mouse[0], mouse[1], (width_screen/ 2 - 100), height_screen / 2, 200, 100, white,
#        blue, 60, 1)
#


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    window.blit(main_bg, (0, 0))
    window.blit(text2, textRect2)
    window.blit(text, textRect)
    window.blit(text1, textRect1)


    pygame.display.update()
