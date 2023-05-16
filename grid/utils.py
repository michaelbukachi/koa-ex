import itertools
import math


def find_closest(data):
    points = data.split(";")
    if len(points) == 1:
        return ""
    dist = float("inf")
    result = None

    for comb in itertools.combinations(points, 2):
        p = [int(val) for val in comb[0].split(",")]
        q = [int(val) for val in comb[1].split(",")]
        cur_dist = math.dist(p, q)
        if cur_dist < dist:
            dist = cur_dist
            result = comb

    if not result:
        return ""

    return ";".join(result)
