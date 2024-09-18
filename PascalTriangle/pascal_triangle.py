import math

def pascal(c, r):
    if c > r or c < 0 or r < 0:
        raise ValueError("Invalid column or row indices.")
    return math.comb(r, c)