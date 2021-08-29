import re
from random import randint

# All Dice
dice1 = "../assets/dice_image1.png"
dice2 = "../assets/dice_image2.png"
dice3 = "../assets/dice_image3.png"
dice4 = "../assets/dice_image4.png"
dice5 = "../assets/dice_image5.png"
dice6 = "../assets/dice_image6.png"

#############################################################################################

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

#############################################################################################

def ladders(x, rounds, answer):
    if x == 1:
        if math(rounds, answer):
            return 38
        else:
            return 1
    elif x == 4:
        if math(rounds, answer):
            return 14
        else:
            return 4
    elif x == 9:
        if math(rounds, answer):
            return 31
        else:
            return 9
    elif x == 28:
        if math(rounds, answer):
            return 84
        else:
            return 28
    elif x == 21:
        if math(rounds, answer):
            return 42
        else:
            return 21
    elif x == 51:
        if math(rounds, answer):
            return 67
        else:
            return 51
    elif x == 80:
        if math(rounds, answer):
            return 99
        else:
            return 80
    elif x == 72:
        if math(rounds, answer):
            return 91
        else:
            return 72
    else:
        return x

#############################################################################################

def snakes(x, rounds, answer):
    if x == 17:
        if math(rounds, answer):
            return 17
        else:
            return 7
    elif x == 54:
        if math(rounds, answer):
            return 54
        else:
            return 34
    elif x == 62:
        if math(rounds, answer):
            return 62
        else:
            return 19
    elif x == 64:
        if math(rounds, answer):
            return 64
        else:
            return 60
    elif x == 87:
        if math(rounds, answer):
            return 87
        else:
            return 36
    elif x == 93:
        if math(rounds, answer):
            return 93
        else:
            return 73
    elif x == 95:
        if math(rounds, answer):
            return 95
        else:
            return 75
    elif x == 98:
        if math(rounds, answer):
            return 98
        else:
            return 79
    else:
        return x

#############################################################################################

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
    return d

#############################################################################################

def turn(score, go_up, swallowed, rounds):
    d = 5
    score += d
    if score <= 100:
        ladd_score = ladders(score, rounds ,'86')
        if ladd_score != score:
            if go_up:
                score = ladd_score
                return score
        snake_score = snakes(score, rounds, '32')
        if snake_score != score:
            score = snake_score
            return score

#############################################################################################

def playing(btn1, rounds):
    player1_x_c = 406 - 25
    player1_y_c = 606 - 25
    comp_x_c = 1006 - 25 - 40
    comp_y_c = 606 - 25
    player1_score = 0
    computer_score = 0
    while True:
        up = False
        down = False

        if btn1:
            if rounds == 1:
                player1_score, up, down, six = 100, False, False ,False
                if not six:
                    rounds += 1
                if player1_score == 100:
                    text = "Congratulations You WON !"
                    return text

            if rounds == 2:
                computer_score, up, down, six = 100, False, False ,False
                if not six:
                    rounds += 1
                    if btn1 == 10:
                        rounds = 1
                if computer_score == 100:
                    text = "Computer Won !"
                    return text

#############################################################################################

def math(rounds ,ans):
    if rounds == 1:

        questions = [["../assets/question/q1.jpg", '96'],
                    ["../assets/question/q2.jpg", '111'],
                    ["../assets/question/q3.jpg", '72'],
                    ["../assets/question/q4.png", '225'],
                    ["../assets/question/q5.jpg", '9'],
                    ["../assets/question/q6.png", '86'],
                    ["../assets/question/q7.png", '23'],
                    ["../assets/question/q8.jpg", '6'],
                    ["../assets/question/q9.jpg", '12'],
                    ["../assets/question/q10.jpg", '5'],
                    ["../assets/question/q11.jpg", '25'],
                    ["../assets/question/q12.jpg", '16'],
                    ["../assets/question/q13.jpg", '16'],
                    ["../assets/question/q14.jpg", '45'],
                    ["../assets/question/q15.jpg", '51'],
                    ["../assets/question/q16.jpg", '9'],
                    ["../assets/question/q17.jpg", '7']]

        question = questions[5][0]
        answer = questions[5][1]

        if answer == ans:
            return True
        else:
            return False
    else:
        computer_answer = 23
        if  computer_answer != ans:
            return False
        else:
            return True
