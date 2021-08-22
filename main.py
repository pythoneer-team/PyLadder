import pygame
time_clocks = pygame.time.Clock()

game_icon = pygame.image.load("assets/icon.jpg")
game_layout_display = pygame.display.set_mode((1366, 768))
pygame.display.set_caption("Welcome to PyLadder game")
pygame.display.set_icon(game_icon)
pygame.display.update()

# Loading images
board = pygame.image.load("assets/board.png")
background1= pygame.image.load("assets/snake2.jpg")
background2= pygame.image.load("assets/snake3.jpg")
background3= pygame.image.load("assets/snake2.jpg")
background4= pygame.image.load("assets/welcome.jpg")
background5= pygame.image.load("assets/welcome1.jpg")
clock = pygame.time.get_ticks()
# welcoming message

def welcoming_msg():
    while pygame.time.get_ticks() - clock < 5000:
            # game_layout_display.blit(background1, (100, 100))
            game_layout_display.blit(background4, (100, 100))
            game_layout_display.blit(background5, (500, 100))
            # game_layout_display.blit(background4, (500, 100))
            pygame.display.update()
clock = pygame.time.get_ticks()
print(clock)

welcoming_msg()



# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
