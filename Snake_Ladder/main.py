import pygame

# Initializing pygame
pygame.init()

# Display Window
width_screen = 1366
height_screen = 768
window = pygame.display.set_mode((width_screen, height_screen))

# Caption Title
pygame.display.set_caption('Pythoneer')

# clock = pygame.time.Clock()

# window_height = window.get_height()
# window_width = window.get_width()

# Background
background = pygame.image.load("assets/background.jpg")
main_background = pygame.transform.smoothscale(background, (1366, 768))

# Board
board = pygame.image.load("assets/board.png")

# All Point
red_point = pygame.image.load("assets/red.png")
red_point = pygame.transform.smoothscale(red_point, (36, 51))

blue_point = pygame.image.load("assets/blue.png")
blue_point = pygame.transform.smoothscale(blue_point, (36, 51))

# Font and Size
font = pygame.font.Font('freesansbold.ttf', 32)

# Start Text
text_start = font.render('Start >>', True, (0, 0, 0), (255, 255, 255))


# Cells Sites Function
def cells_sites(cell):
    cells = [[391, 581], [441, 581], [491, 581], [541, 581], [591, 581], [641, 581], [691, 581], [741, 581], [791, 581],
             [841, 581], [891, 581], [891, 535], [841, 535], [791, 535], [741, 535], [691, 535], [641, 535], [591, 535],
             [541, 535], [491, 535], [441, 535], [441, 481], [491, 481], [541, 481], [591, 481], [641, 481], [691, 481],
             [741, 481], [791, 481], [841, 481], [891, 481], [891, 435], [841, 435], [791, 435], [741, 435], [691, 435],
             [641, 435], [591, 435], [541, 435], [491, 435], [441, 435], [441, 381], [491, 381], [541, 381], [591, 381],
             [641, 381], [691, 381], [741, 381], [791, 381], [841, 381], [891, 381], [891, 335], [841, 335], [791, 335],
             [741, 335], [691, 335], [641, 335], [591, 335], [541, 335], [491, 335], [441, 335], [441, 281], [491, 281],
             [541, 281], [591, 281], [641, 281], [691, 281], [741, 281], [791, 281], [841, 281], [891, 281], [891, 235],
             [841, 235], [791, 235], [741, 235], [691, 235], [641, 235], [591, 235], [541, 235], [491, 235], [441, 235],
             [441, 181], [491, 181], [541, 181], [591, 181], [641, 181], [691, 181], [741, 181], [791, 181], [841, 181],
             [891, 181], [891, 135], [841, 135], [791, 135], [741, 135], [691, 135], [641, 135], [591, 135], [541, 135],
             [491, 135], [441, 135]]
    return cells[cell][0], cells[cell][1]


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.blit(main_background, (0, 0))
    window.blit(board, (433, 134))

    window.blit(text_start, (260, 592))

    x_red, y_red = cells_sites(0)
    window.blit(red_point, (x_red, y_red))

    x_blue, y_blue = cells_sites(2)
    window.blit(blue_point, (x_blue, y_blue))

    pygame.display.update()
