from pyladder import __version__
from pyladder.score import *


def test_version():
    assert __version__ == '0.1.0'

####################################################################


def test_moving_zero():
    actual_x, actual_y = moving(0)
    expected_x, expected_y = 381, 581
    assert actual_x == expected_x and actual_y == expected_y

####################################################################


def test_moving_ten():
    actual_x, actual_y = moving(10)
    expected_x, expected_y = 881, 581
    assert actual_x == expected_x and actual_y == expected_y

####################################################################


def test_ladders():
    actual = ladders(9, 1, '86')
    expected = 31
    assert actual == expected

####################################################################


def test_snakes():
    actual = snakes(62, 1, '32')
    expected = 62
    assert not actual == expected

####################################################################


def test_dice():
    actual = dice(6, 1)
    expected = "../assets/dice_image6.png"
    assert actual == expected

####################################################################


def test_turn_ladders():
    actual = turn(4, True, False, 1)
    expected = 31
    assert actual == expected

####################################################################


def test_turn_snakes():
    actual = turn(57, False, True, 1)
    expected = 19
    assert actual == expected

####################################################################


def test_playing_player_win():
    actual = playing(10, 1)
    expected = "Congratulations You WON !"
    assert actual == expected

####################################################################


def test_playing_computer_win():
    actual = playing(10, 2)
    expected = "Computer Won !"
    assert actual == expected

####################################################################


def test_math_computer_fail_answer():
    actual = math(2, 50)
    expected = False
    assert actual == expected

####################################################################


def test_math_computer_correct_answer():
    actual = math(2, 23)
    expected = True
    assert actual == expected

####################################################################
