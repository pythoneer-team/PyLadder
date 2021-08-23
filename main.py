
import pygame

# Initializing pygame
pygame.init()
window = pygame.display.set_mode((1366, 768))
clock = pygame.time.Clock()
window_height = window.get_height()
window_width = window.get_width()
main_bg_file = pygame.image.load("pg.jpg")
main_bg = pygame.transform.smoothscale(main_bg_file, (1366, 768))


ic = pygame.image.load("icon.jpg")
game_layout_display = pygame.display.set_mode((50,50))
pygame.display.set_caption("Snakes and Ladders Game ")
pygame.display.set_icon(ic)
pygame.display.update()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    window.blit(main_bg, (0, 0))

    pygame.display.update()


