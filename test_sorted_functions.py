from sorted_functions import *


def test_sorted_order():
    x = ['e', 'a', 'c', 'd', 'b']
    y = sorted_order(x)
    assert y == sorted(x) == ['a', 'b', 'c', 'd', 'e']
