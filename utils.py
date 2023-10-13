import numpy as np
from manim import *
import constant as C

def get_indices(max_index:int, step:float) :
    if (max_index % 2 == 1) : # odd
        return np.arange(np.ceil(-max_index/2), np.floor(max_index/2) + 1, step = 1) * step
    return np.arange(np.ceil(-max_index/2) + 0.5, np.floor(max_index/2) + 0.5, step = 1) * step

def mobject_ndarray(array:np.array, step:float, color:str, font_size:int) -> VGroup :
    if (array.ndim == 1) :
        array = np.expand_dims(array, 0)

    matrix = Rectangle(height=array.shape[0]*step, width=array.shape[1]*step, grid_xstep=step, grid_ystep=step)
    mobject = VGroup(matrix)
    for i, row in enumerate(get_indices(array.shape[0], step)) :
        for j, col in enumerate(get_indices(array.shape[1], step)) :
            text = Text(f"{array[i][j]}", font_size=font_size).move_to(matrix).shift([col, row, 0])
            mobject.add(text)
    return mobject