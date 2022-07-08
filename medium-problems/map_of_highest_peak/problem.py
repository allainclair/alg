# https://leetcode.com/problems/map-of-highest-peak/
UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)

MAP_DIRECTION = {UP}

def get_water_coords(is_water):
    water_points = []
    for i, line in enumerate(is_water):
        js = [j for j, cel in enumerate(line) if cel == 1]
        water_points += [(i, j) for j in js]
    return water_points


def get_coord(visit, x, y):
    direction_x, direction_y = visit
    return x + direction_x, y + direction_y


def create_peaks(n, m, coord):
    def peaks_rec(peaks, prev_value, to_visit):
        min_ = prev_value
        for visit in to_visit:
            visit_x, visit_y = get_coord(visit, x, y)


    def peaks_rec(peaks, visited, x, y):
        up_value = down_value = left_value = right_value = float('inf')
        arg_calls = []
        if x-1 >= 0:  # Up
            if visited[x-1][y]:
                up_value = peaks[x-1][y]
            else:
                arg_calls.append((x-1, y))
        if x+1 < n:  # Down
            if visited[x+1][y]:
                down_value = peaks[x+1][y]
            else:
                arg_calls.append((x+1, y))
        if y-1 >= 0:  # Left
            if visited[x][y-1]:
                left_value = peaks[x][y-1]
            else:
                arg_calls.append((x, y-1))
        if y+1 < m:  # Right
            if visited[x][y+1]:
                right_value = peaks[x][y+1]
            else:
                arg_calls.append((x, y+1))
        min_ = min(up_value, down_value, left_value, right_value)
        peaks[x][y] = min_ + 1

        for args in arg_calls:
            peaks_rec(peaks, visited, *args)

    peaks = [[0] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]
    x, y = coord
    peaks[x][y] = 0  # Water
    visited[x][y] = True

    peaks_rec(peaks, visited, x, y)


def get_adjacency(matrix, coord):
    n, m = len(matrix), len(matrix[0])
    x, y = coord
    coords = []
    if x-1 >= 0:  # Up
        coords.append((x-1, y))
    if x+1 < n:  # Down
        coords.append((x+1, y))
    if y-1 >= 0:  # Left
        coords.append((x, y-1))
    if y+1 < m:  # Right
        coords.append((x, y+1))
    return coords


def bfs(matrix, start_coord):
    start_x, start_y = start_coord
    adjacencies = get_adjacency(matrix, start_coord)


def highest_peak(is_water):
    water_coords = get_water_coords(is_water)
    n = len(water_coords)
    m = len(water_coords[0])
    all_peaks = []
    for coord in water_coords:
        peaks = create_peaks(n, m, coord)
        all_peaks.append(peaks)


def main():
    is_water = [[0, 1], [0, 0]]
    assert get_water_coords(is_water) == [(0, 1)]
    # assert highest_peak(is_water)  == [[1, 0], [2, 1]]

    is_water = [[0, 0, 1], [1, 0, 0], [0, 0, 0]]
    assert get_water_coords(is_water) == [(0, 2), (1, 0)]
    # assert highest_peak(is_water) == [[1, 1, 0], [0, 1, 1], [1, 2, 2]]


if __name__ == '__main__':
    main()
