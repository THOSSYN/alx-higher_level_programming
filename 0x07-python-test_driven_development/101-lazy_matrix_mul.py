#!/usr/bin/python3
"""It uses Numpy module"""

import numpy as np
"""The numpy is aliased as np"""


def lazy_matrix_mul(m_a, m_b):
    """Multiplies 2 matrices by using Numpy

       Args:
        m_a: is the first matrix argument
        m_b: is the second matrix argument
    """
    a_res = np.array(m_a)
    b_res = np.array(m_b)
    return a_res.dot(b_res)
