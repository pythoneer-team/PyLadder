
import pygame


pygame.init()
 # screen resolution
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


BLACK = (100,100,100)
WHITE = (255,255,255)
HOVER_COLOR = (170,170,170)




FONT = pygame.font.SysFont ("Times New Norman", 60)

text1 = FONT.render("Computer", True, WHITE)
text2 = FONT.render("2 Players", True, WHITE)
text3 = FONT.render("QUIT", True, WHITE)
rect1 = pygame.Rect(550,340,230,50)
rect2 = pygame.Rect(550,430,230,50)
rect3 = pygame.Rect(550,530,230,50)

buttons = [
    [text1, rect1, BLACK],
    [text2, rect2, BLACK],
    [text3, rect3, BLACK],
    ]

def game_intro():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.MOUSEMOTION:
                for button in buttons:
                   
                    if button[1].collidepoint(event.pos):
                     
                        button[2] = HOVER_COLOR
                    else:
               
                        button[2] = BLACK

        window.blit(main_bg, (0, 0))

       
        for text, rect, color in buttons:
            pygame.draw.rect(window, color, rect)
            window.blit(text, rect)

        pygame.display.flip()
        clock.tick(15)


game_intro()
pygame.quit()