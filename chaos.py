import matplotlib as plt
import numpy as np
from collections import namedtuple
import random

Point = namedtuple('Point', 'x y')


def mid_point(A, B, portion=2):
    C = Point()
    C.x = A.x+B.x/portion
    C.y = A.y+B.y/portion
    return C


def build_visual(anchors=[], moving_point=None,):
    #TODO: Build anchor points
    #TODO: build plt

    print('anchors:', anchors)
    print('moving_point:', moving_point)
    pass


def generate_anchor_points(n=2):
    anchor_points = []

    for i in range(n):
        anchor = Point(x=random.randrange(-10, 10), y=random.randrange(-10, 10))
        anchor_points.append(anchor)

    return anchor_points


if __name__ == "__main__":
    num_anchor_points = 3
    anchor_points = generate_anchor_points(n=num_anchor_points)
    starting_position = Point() # at random
    build_visual(anchors=anchor_points, moving_point=starting_position)
