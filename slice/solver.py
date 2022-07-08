from const import (
    MOVE_NORTH,
    MOVE_EAST,
    MOVE_WEST,
    MOVE_SOUTH,
    DROP_PIZZA,
)


def deliver(target_x, target_y, current_x, current_y):
    movements = []
    delivered = False
    while not delivered:
        moved = False
        if current_x < target_x:
            current_x += 1
            movements.append(MOVE_EAST)
            moved = True
        elif current_x > target_x:
            current_x -= 1
            movements.append(MOVE_WEST)
            moved = True

        if current_y < target_y:
            current_y += 1
            movements.append(MOVE_NORTH)
            moved = True
        elif current_y > target_y:
            current_y -= 1
            movements.append(MOVE_SOUTH)
            moved = True

        if not moved:
            movements.append(DROP_PIZZA)
            delivered = True

    return movements, current_x, current_y


def solver_1(pizza_locations):
    current_x = current_y = 0
    movements = []
    for location in pizza_locations:
        x, y = location
        new_movements, current_x, current_y = deliver(x, y, current_x, current_y)
        movements += new_movements
    return ''.join(movements)
