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


def max_distance(rack_bins):
    empty_racks_ = empty_racks(rack_bins)
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
    position_shift = min_
    for bike_position in bikes:
        shift_position = bike_position - position_shift
        rack_bins[shift_position] = 1
    return rack_bins


def solution(A):
    racks = get_racks(A)
    return max_distance(racks)


def test_1():
    A = [10, 0, 8, 2, -1, 12, 11, 3]
    assert solution(A) == 2


def test_2():
    A = [5, 5]
    assert solution(A) == 0


def test_3():
    A = [-3, 13, 0, 2, 6, 9]
    assert solution(A) == 2



def main():
    pass


if __name__ == '__main__':
    main()
