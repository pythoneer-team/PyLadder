from pyladder import __version__
from pyladder.pyladder import *


def test_version():
    assert __version__ == '0.1.0'

#######################################################################


def test_score():
    playing(10)

