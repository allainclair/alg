# https://leetcode.com/problems/rectangle-area/


def intersection_rec(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
    max_min_x = max(ax1, bx1)
    min_max_x = min(ax2, bx2)

    max_min_y = max(ay1, by1)
    min_max_y = min(ay2, by2)

    if max_min_x >= min_max_x or max_min_y >= min_max_y:
        max_min_x = min_max_x = max_min_y = min_max_y = 0

    return max_min_x, min_max_x, max_min_y, min_max_y


def intersection(max_point, min_point):
    diff = max_point - min_point
    return diff if diff > 0 else 0


def area(x1, x2, y1, y2):
    return (x2-x1) * (y2-y1)


def compute_area(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
    area_1 = area(ax1, ax2, ay1, ay2)
    area_2 = area(bx1, bx2, by1, by2)

    x1, x2, y1, y2 = intersection_rec(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2)
    intersec_area = area(x1, x2, y1, y2)

    return area_1 + area_2 - intersec_area


def test1():
    ax1, ay1 = -3, 0
    ax2, ay2 = 3, 4
    bx1, by1 = 0, -1
    bx2, by2 = 9, 2
    assert compute_area(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2) == 45


def test2():
    ax1, ay1 = -2, -2
    ax2, ay2 = 2, 2
    bx1, by1 = -2, -2
    bx2, by2 = 2, 2
    assert compute_area(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2) == 45