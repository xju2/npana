#!/usr/bin/env python

import numpy as np
from numba import vectorize

target = 'cpu'
@vectorize(['float32(float32, float32)'], target=target)
def Add(a, b):
    return a+b

if __name__ == "__main__":
    # Initialize arrays
    N = 1000000
    A = np.ones(N, dtype=np.float32)
    B = np.ones(A.shape, dtype=A.dtype)
    C = np.empty_like(A, dtype=A.dtype)

    # Add arrays on GPU
    C = Add(A, B)
