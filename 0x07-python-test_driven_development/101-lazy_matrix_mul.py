#!/usr/bin/python3

"""This module contains a function that multiplies two matrices"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Return the multiplication of two matrices.
    """

    return (np.matmul(m_a, m_b))
