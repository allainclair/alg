def empty_racks(list_):
    empty_spots = []
    empty_stop_number = 0
    for position in list_:
        if not position:
            empty_stop_number += 1
        else:
            empty_spots.append(empty_stop_number)
            empty_stop_number = 0
    empty_spots.append(empty_stop_number)
    return empty_spots


def max_distance(racks):
    empty_racks_ = empty_racks(racks)
    first = empty_racks_[0]
    last = empty_racks_[-1]
    max_ = max(first, last)

    remaining_racks = empty_racks_[1:-1]
    for remaining_rack_distance in remaining_racks:
        distance = remaining_rack_distance // 2
        if remaining_rack_distance % 2 == 1:
            distance += 1
        if distance > max_:
            max_ = distance
    return max_


def get_racks(bikes):
    min_ = min(bikes)
    max_ = max(bikes)
    number_of_racks = (max_ - min_) + 1

    rack_bins = [0]*number_of_racks
    shift = min_
    for bike_pos in bikes:
        pos = bike_pos - shift
        rack_bins[pos] = 1
    return rack_bins


def solution(A):
    racks = get_racks(A)
    return max_distance(racks)


def main():
    A = [10, 0, 8, 2, -1, 12, 11, 3]
    r = [1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1]
    assert solution(A) == 2

    A = [5, 5]
    assert solution(A) == 0

    A = [-3, 13, 0, 2, 6, 9]
    assert solution(A) == 2

    A = [-3, 13, 0, 2, 0, 9]
    assert solution(A) == 3

    racks = [1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1]
    assert max_distance(racks) == 2

    racks = [1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1]
    assert max_distance(racks) == 3
    # #
    racks = [0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0]
    assert max_distance(racks) == 4


    racks = [0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0]
    assert max_distance(racks) == 5

if __name__ == '__main__':
    main()
