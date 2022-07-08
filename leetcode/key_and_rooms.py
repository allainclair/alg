# https://leetcode.com/problems/keys-and-rooms/

def main():
    rooms = [[1], [2], [3], []]
    assert check_rooms(rooms)
    rooms = [[1, 3], [3, 0, 1], [2], [0]]
    assert not check_rooms(rooms)
    print()
    rooms = [[2, 3], [], [2], [1, 3, 1]]
    assert check_rooms(rooms)


def check_room(rooms, room_index, open_rooms):
    print('room_index', room_index)
    for key in rooms[room_index]:
        print('key', key)
        if not open_rooms[key]:
            open_rooms[key] = True
            if all(open_rooms):
                return True
            else:
                check_room(rooms, key, open_rooms)


def check_rooms(rooms):
    open_rooms = [True] + [False]*(len(rooms) - 1)
    if all(open_rooms):
        return True
    check_room(rooms, 0, open_rooms)
    return all(open_rooms)


if __name__ == '__main__':
    main()
