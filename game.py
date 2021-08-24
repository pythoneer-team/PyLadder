# Importing
import pygame
import re
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
Background = pygame.image.load("assets/bg_menu.jpg")
ourrules = pygame.image.load("assets/rules.png")
ourrules = pygame.transform.smoothscale(ourrules, (width, height))
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

# Sounds
pygame.mixer.music.load("sound/song1.wav") # And menu first line
snake_sound = pygame.mixer.Sound("sound/snake2.wav")
ladder_sound = pygame.mixer.Sound("sound/ladder2.wav")
win_sound = pygame.mixer.Sound("sound/win1.wav")
lose_sound = pygame.mixer.Sound("sound/loss3.wav")
dice_sound = pygame.mixer.Sound("sound/dice1.wav")

# img Win & loss
wins_player = pygame.image.load("assets/wins_player.png")
loss_player = pygame.image.load("assets/loss_player.png")
wins_computer = pygame.image.load("assets/wins_computer.png")
loss_computer = pygame.image.load("assets/loss_computer.png")

# Position of mouse
mouse = pygame.mouse.get_pos()

# Last Question
last_question = []

# prompt text when player/computer wins the game , or when a player cant move due to movments being higher than 100  
def display_text(text, x, y, fontsize):
    Textsize = pygame.font.SysFont("ravie", fontsize)
    Texts, TextBox = text_reshape(text, Textsize)
    TextBox.center = (x, y)
    game_layout.blit(Texts, TextBox)
# text reshape
def text_reshape(text, font):
    Texts = font.render(text, True, (250, 250, 250))
    return Texts, Texts.get_rect()
# prompt Messagewhen there is a ladder or a snake 
def display_text2(text, x, y, fontsize,c):
    Textsize = pygame.font.SysFont("courier new", fontsize)
    texts, TextBox = text_reshape2(text, Textsize,c)
    TextBox.center = (x, y)
    game_layout.blit(texts, TextBox)

def text_reshape2(text, font, c):
    Texts = font.render(text, True, c)
    return Texts, Texts.get_rect()

# Goti movement function Yousef (returning x and y cooridinates)
def moving(a):
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
            return 4
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
        if math():
            return 17
        else:
            return 7
    elif x == 54:
        if math():
            return 54
        else:
            return 34
    elif x == 62:
        if math():
            return 62
        else:
            return 19
    elif x == 64:
        if math():
            return 64
        else:
            return 60
    elif x == 87:
        if math():
            return 87
        else:    
            return 36
    elif x == 93:
        if math():
            return 93
        else:   
            return 73
    elif x == 95:
        if math():
            return 95
        else:  
            return 75
    elif x == 98:
        if math():
            return 98
        else: 
            return 79
    else:
        return x
#  dices and thier images Yousef (to do: change time)
def dice(d,rounds):
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
    if rounds==1:
        clock = pygame.time.get_ticks()
        while pygame.time.get_ticks() - clock < 800:
            game_layout.blit(d, (160, 300))
            pygame.display.update()
    else:
        clock = pygame.time.get_ticks()
        while pygame.time.get_ticks() - clock < 800:
            game_layout.blit(d, (1140, 300))
            pygame.display.update()

    # for mute and unmute
# Quitting:
def Quit():
    pygame.quit()
    quit()
# Button:
def button(text, xmouse, ymouse, x, y, width, height, int, new, size,btn_1):
    if x + width > xmouse > x and y + height > ymouse > y:
        pygame.draw.rect(game_layout, new, [x - 2.5, y - 2.5, width + 5, height + 5])
        if pygame.mouse.get_pressed() == (1, 0, 0):
            if btn_1 == 1:
                chosen()
            elif btn_1 == 0:
                Quit()
            elif btn_1 == 15:
                rules()
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
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    Quit()
        clock = pygame.time.get_ticks()
        while True:
            while pygame.time.get_ticks() - clock < 500:
                game_layout.blit(ourrules, (0, 0))
                pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    return
            pygame.display.update()
#  Game lunching
def starter():
    # time_clock = pygame.time.get_ticks()
    # while pygame.time.get_ticks() - time_clock < 2500:
    #     game_layout.blit(back1, (0, 0))
    #     pygame.display.update()
        # note we may reomve this one
    # while True:
    #     time_clock = pygame.time.get_ticks()
    #     while pygame.time.get_ticks() - time_clock < 500:
    #         game_layout.blit(back2, (0, 0))
    #         pygame.display.update()
    #     time_clock = pygame.time.get_ticks()
    #     while pygame.time.get_ticks() - time_clock < 500:
    #         game_layout.blit(back3, (0, 0))
    #         pygame.display.update()
    #     time_clock = pygame.time.get_ticks()
    #     while pygame.time.get_ticks() - time_clock < 500:
    #         game_layout.blit(back4, (0, 0))
    #         pygame.display.update()
    #     time_clock = pygame.time.get_ticks()
    #     while pygame.time.get_ticks() - time_clock < 500:
    #         game_layout.blit(back5, (0, 0))
    #         pygame.display.update()
    #
    #     for event in pygame.event.get():
    #         if event.type == pygame.KEYDOWN:
    #             return
        pygame.display.update()
# about our project and team members
def ASAC():
    while True:
        game_layout.blit(asac_project, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    Quit()
        mouse = pygame.mouse.get_pos()
        if button("Back", mouse[0], mouse[1], width / 2 - 120, 680, 200, 70, (113, 207, 41, 1), (0, 230, 0), 60, 2):
            menu()
        pygame.display.update()
# Main Menu of our game
def menu():
    pygame.mixer.music.play(-1)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    Quit()
        mouse = pygame.mouse.get_pos()
        game_layout.blit(Menu, (0, 0))
        button("Play", mouse[0], mouse[1], (width / 2 - 100), height / 2, 200, 100, (113, 207, 41, 1),(0, 230, 0), 60, 1)
        button("Rules", mouse[0], mouse[1], (width / 2 - 100), (height / 2) + 110, 200, 100, (113, 207, 41, 1),(0, 230, 0), 60, 15)                                                                          
        button("Quit", mouse[0], mouse[1], (width / 2 - 100), (height / 2) + 220, 200, 100, (113, 207, 41, 1),(0, 230, 0), 60, 0)
        mouse = pygame.mouse.get_pos()
        if button("PyLadder", mouse[0], mouse[1], 1166, 0, 200, 50, (113, 207, 41, 1),(0, 230, 0), 30,2):
            ASAC()
        pygame.display.update()
# Options Menu after chosing Play:
def chosen():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    Quit()
        mouse = pygame.mouse.get_pos()
        game_layout.blit(Menu, (0, 0))
        # Single player button
        btn_1 = button("Single Player Against Computer", mouse[0], mouse[1], (330),400,750,100,(113, 207, 41, 1),
               (0, 230, 0), 40,"single")
        mouse = pygame.mouse.get_pos()
        btn_2 = button("Back to Main", mouse[0], mouse[1], 10, 700, 300, 50,(113, 207, 41, 1),(0, 230, 0), 30, 5)
        if btn_2 == 5:
            menu()
        if btn_1 == "single":
            playing(21)
        pygame.display.update()
# Turn
def turn(score, go_up, swallowed,rounds):
    # roll a dice using random number between 1 and 6
    d = randint(1, 6) 
    # print(type(d))
    pygame.mixer.Sound.play(dice_sound)
    if d != 6:
        dice(d,rounds)
        six = False
    else:
        dice(d,rounds)
        clock = pygame.time.get_ticks()
        while pygame.time.get_ticks() - clock < 1500:
            display_text(" HOT DICE", 130, 60, 55)
            pygame.display.update()
        six = True
    score += d
    # if score is 100 or less
    if score <= 100:
        ladd_score = ladders(score)  # checking for ladders for player
        if ladd_score != score:
            go_up = True
            pygame.mixer.Sound.play(ladder_sound)
            clock = pygame.time.get_ticks()
            score = ladd_score
        snake_score = snakes(score)
        if snake_score != score:  
            swallowed = True
            pygame.mixer.Sound.play(snake_sound)
            score = snake_score
    # if score is not grater than 100
    else:  
        score -= d
        clock = pygame.time.get_ticks()
        while pygame.time.get_ticks() - clock < 1500:
            display_text("Oops, YOU CANT MOVE!", 130, 60, 55)
            pygame.display.update()
    return score, go_up, swallowed, six

def playing(btn1):
    game_layout.blit(Background, (0, 0))
    game_layout.blit(Board, (width / 2 - 250, height / 2 - 250))
    player1_x_c = 406 - 25
    player1_y_c = 606 - 25
    comp_x_c = 406 - 25-40
    comp_y_c = 606 - 25
    game_layout.blit(red_token, (comp_x_c, comp_y_c))
    game_layout.blit(blue_token, (player1_x_c, player1_y_c))
    gamer1score = 0
    gamer2score = 0
    rounds = 1
    while True:
        up = False
        down = False
        time=2500
        game_layout.blit(Background, (0, 0))
        game_layout.blit(Board, (width / 2 - 250, height / 2 - 250))
        mouse = pygame.mouse.get_pos()
        # whenever escape is pressed quit the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    Quit()
        green_color = (113, 207, 41, 1)
        light_green_color = (0, 230, 0)
        # print(btn1)
        if btn1:
            if button("Click to Roll", mouse[0], mouse[1], 70, 138, 300, 50, green_color, light_green_color, 30, btn1):
                if rounds == 1:
                    gamer1score, up, down, six = turn(gamer1score, up, down,rounds)
                    player1_x_c, player1_y_c = moving(gamer1score)
                    if not six:
                        rounds += 1
                    if gamer1score == 100:
                        time = pygame.time.get_ticks()
                        while pygame.time.get_ticks() - time < 2500:
                            display_text("Congratulations You WON !", 1000, 50, 50)
                            pygame.mixer.music.pause()
                            while pygame.time.get_ticks() - time < 2500:
                                game_layout.blit(wins_player, (-5, height / 2 - 100))
                                game_layout.blit(loss_computer, (width - 120, height / 2))
                                pygame.display.update()
                                pygame.mixer.Sound.play(win_sound)
                            pygame.mixer.music.unpause()
                            pygame.display.update()
                        break
            game_layout.blit(red_token, (comp_x_c ,comp_y_c ))
            if btn1 == 21:
                game_layout.blit(blue_token, (player1_x_c + 2, player1_y_c))
            button("Computer", mouse[0], mouse[1], 1100, 138, 200, 50, green_color, light_green_color, 30,btn1)
            if rounds == 2:
                gamer2score, up, down, six = turn(gamer2score, up, down,rounds)
                comp_x_c, comp_y_c = moving(gamer2score)
                if not six:
                    rounds += 1
                    if btn1 == 21:
                        rounds = 1
                if gamer2score == 100:
                    time_clock = pygame.time.get_ticks()
                    while pygame.time.get_ticks() - time_clock < 2000:
                        display_text("Computer Wins !", 1066, 50, 50)
                        pygame.mixer.music.pause()
                        while pygame.time.get_ticks() - time_clock < 2500:
                            game_layout.blit(wins_computer, (width - 250, height / 2 - 100))
                            game_layout.blit(loss_player, (-5, height / 2))
                            pygame.display.update()
                            pygame.mixer.Sound.play(lose_sound)
                        pygame.mixer.music.unpause()
                        pygame.display.update()
                    break
        if up:
            time_clock = pygame.time.get_ticks()
            while pygame.time.get_ticks() - time_clock < 1000:
                display_text2("To use the ladder:Please answer a simple question", 700, 50, 35, (250, 250, 250))
                pygame.display.update()
        if down:
            time_clock = pygame.time.get_ticks()
            while pygame.time.get_ticks() - time_clock < 1000:
                display_text2("To avoid a Snake:Please answer a simple question", 750, 50, 35, (250, 250, 250))
                pygame.display.update()
        clock.tick()
        pygame.display.update()

def math():
    font = pygame.font.Font(None, 32)
    input_box = pygame.Rect(585, 570, 140, 32)

    questions = [["assets/question/q1.jpg", '15'],
                 ["assets/question/q2.jpg", '15'],
                 ["assets/question/q3.jpg", '15'],
                 ["assets/question/q4.jpg", '15'],
                 ["assets/question/q5.jpg", '15'],
                 ["assets/question/q6.jpg", '15'],
                 ["assets/question/q7.jpg", '15'],
                 ["assets/question/q8.jpg", '15'],
                 ["assets/question/q9.jpg", '15'],
                 ["assets/question/q10.jpg", '15'],
                 ["assets/question/q11.jpg", '15'],
                 ["assets/question/q12.jpg", '15'],
                 ["assets/question/q13.jpg", '15'],
                 ["assets/question/q14.jpg", '15'],
                 ["assets/question/q15.jpg", '15'],
                 ["assets/question/q16.jpg", '15'],
                 ["assets/question/q17.jpg", '15'],
                 ["assets/question/q18.jpg", '15']]
    read_q = randint(0, 17)


    get_question = True

    while get_question:
        if questions[read_q][0] in last_question:
            read_q = randint(0, 17)
        else:
            last_question.append(questions[read_q][0])
            get_question = False
    print(last_question)
    question = pygame.image.load(questions[read_q][0])
    answer = questions[read_q][1]


    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive

    active = False
    text = ''
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
                if input_box.collidepoint(event.pos):
                    # Toggle the active variable.
                    active = not active
                else:
                    active = False
                # Change the current color of the input box.
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        # check if the player answer the question
                        if text:
                            if text == answer:
                                return True
                            else:
                                return False
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        # x = re.findall('\d', text)
                        # if x :
                            text += event.unicode
                        # print(x)

        pygame.draw.rect(game_layout, (30, 30, 30), pygame.Rect(433, 134, 500, 500))
        game_layout.blit(question, (433, 134))

        # Render the current text.
        txt_surface = font.render(text, True, color)

        # Resize the box if the text is too long.
        width_box = max(200, txt_surface.get_width()+10)

        input_box.w = width_box

        # Blit the text.
        game_layout.blit(txt_surface, (input_box.x+5, input_box.y+5))

        # Blit the input_box rect.
        pygame.draw.rect(game_layout, color, input_box, 2)

        pygame.display.update()

starter()
menu()
