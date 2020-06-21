import matplotlib.pyplot as plt
import numpy as np
from collections import namedtuple
import random

"""
    2D Chaos Game
"""

Point = namedtuple('Point', 'x y')


def mid_point(a, b, portion=2):
    c = []
    c[0] = (a[0] + b[0])/portion
    c[1] = (a[1] + b[1])/portion
    return c


def build_visual(anchors, moving_point=None,):
    print('anchors:', anchors)
    print('moving_point:', moving_point)

    plt.scatter(*anchors.T, color='r')
    plt.show()


def random_point():
    # return Point(x=random.randrange(0, 20), y=random.randrange(0, 20))

    return [random.randrange(0, 20), random.randrange(0, 20)]


def generate_anchor_points(n=3):
    anchor_points = []

    for i in range(n):
        anchor_points.append(random_point())

    return np.array(anchor_points)


def generate_starting_point():
    starting_point = random_point()
    return np.array(starting_point)


if __name__ == "__main__":
    random.seed(100)
    num_anchor_points = 3
    anchor_points = generate_anchor_points(n=num_anchor_points)
    starting_position = generate_starting_point()
    build_visual(anchors=anchor_points, moving_point=starting_position)
