"""
This module uses numpy but is otherwise very easy to understand and test.
"""

import numpy as np


def dot_multiply(a, b):
    return np.dot(a, b)


def two_norm(array):
    return np.linalg.norm(array, ord=2)
