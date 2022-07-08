# https://leetcode.com/problems/trapping-rain-water/

def correct_water(water, higher_left_index, higher_left, current_index, current_water):
    water_tank = water[higher_left_index+1 : current_index+1]
    tank_level_dropped = max(higher_left - current_water, 0)
    water_tank = [water - tank_level_dropped for water in water_tank]
    water[higher_left_index+1 : current_index+1] = water_tank


def trap(height):
    higher_left = height[0]
    higher_left_index = 0
    water_system = [0]*len(height)
    previous_wall = float('inf')
    increasing_or_stopped = False
    for i, h in enumerate(height):
        if previous_wall <= h:
            increasing_or_stopped = True
        elif increasing_or_stopped:  # and decreasing
            correct_water(water_system, higher_left_index, higher_left, i-1, previous_wall)
            higher_left = previous_wall
            higher_left_index = i-1
            increasing_or_stopped = False
            print('higher_left_index', higher_left_index)
        else:  # Only decreasing.
            pass

        water_system[i] = max(higher_left - h, 0)
        previous_wall = h

    # Last position
    print('higher_left_index', higher_left_index)
    len_dropped = len(water_system[higher_left_index+1:])
    drooped = [0]*len_dropped
    water_system[higher_left_index+1:] = drooped
    print(water_system)
    return sum(water_system)


def main():
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    result = trap(height)
    print(result)
    assert trap(height) == 6
    print()

    height = [4, 2, 0, 3, 2, 5]
    result = trap(height)
    print(result)
    assert trap(height) == 9


if __name__ == '__main__':
    main()
