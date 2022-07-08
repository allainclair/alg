def check_coordinates(max_x, max_y, coordinates):
    """Candidate needs to check all Xs Ys to be less than max_x and max_y"""
    for x, y in coordinates:
        if x >= max_x or y >= max_y:
            pass


def coordinates(coord_string):
    parsed = []
    new_coord = ''
    for char in coord_string:
        if char != ')':
            new_coord += char
        else:
            x, y = _get_coord(f'{new_coord})')
            parsed.append((x, y))
            new_coord = ''
    return parsed


def grid_dimension(string):
    """Candidate needs to check X and Y types"""
    x, y = string.split('x')
    return int(x), int(y)


def _get_coord(string):
    """Candidate needs to check X and Y types"""
    x, y = string.strip().lstrip('(').rstrip(')').split(',')
    return int(x.strip()), int(y.strip())
