from some_functions import *


def test_dot_multiply():
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])
    assert dot_multiply(a, b) == 32


def test_two_norm():
    array = np.array([3, 4])
    assert two_norm(array) == 5
