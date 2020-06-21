import matplotlib.pyplot as plt
import numpy as np
from collections import namedtuple
import random

"""
    2D Chaos Game
"""

Point = namedtuple('Point', 'x y')


def mid_point(A, B, portion=2):
    C = Point()
    C.x = A.x+B.x/portion
    C.y = A.y+B.y/portion
    return C


def build_visual(anchors, moving_point=None,):
    print('anchors:', anchors)
    print('moving_point:', moving_point)

    plt.scatter(*anchors.T)
    plt.show()


def random_point():
    # return Point(x=random.randrange(0, 20), y=random.randrange(0, 20))

    return [random.randrange(0, 20), random.randrange(0, 20)]


def generate_anchor_points(n=2):
    anchor_points = []

    for i in range(n):
        anchor_points.append(random_point())

    print(anchor_points)

    return np.array(anchor_points)


def generate_starting_point():
    starting_point = random_point()
    return starting_point


if __name__ == "__main__":
    random.seed(100)
    num_anchor_points = 3
    anchor_points = generate_anchor_points(n=num_anchor_points)
    starting_position = generate_starting_point()
    build_visual(anchors=anchor_points, moving_point=starting_position)
