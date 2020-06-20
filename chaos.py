import matplotlib as plt
import numpy as np
from collections import namedtuple

Point = namedtuple('Point', 'x y')


def mid_point(A, B, portion=2):
    C = Point()
    C.x = A.x+B.x/portion
    C.y = A.y+B.y/portion
    return C


def build_visual(anchors=[], moving_point=None,):
    #TODO: Build anchor points
    #TODO: build plt
    pass


if __name__ == "__main__":
    build_visual()
