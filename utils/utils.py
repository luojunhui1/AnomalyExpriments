import math
import numpy as np

def rgb2hex(rgbcolor):
    r, g, b, a = rgbcolor
    r = math.floor(r * 255)
    g = math.floor(g * 255)
    b = math.floor(b * 255)
    result = np.left_shift(r, 16) + np.left_shift(g, 8) + b
    return '#' + hex(result)[2:]

def norm_by_row(data):
    # m = np.mean(data, axis = 1)
    res = (data.copy()).astype(np.float64)
    for index in range(0, len(data)):
        mx = np.max(data, axis=1)
        mn = np.min(data, axis=1)
        res[index] = (res[index] - mn[index]) / (mx[index] - mn[index])
    return res