TOP_LEFT = 0
TOP_RIGHT = 1
BOTTOM_LEFT = 2
BOTTOM_RIGHT = 3


class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


def get_quadrants(matrix):
    n = len(matrix)
    if n > 1:
        mid = n // 2

        top_left = []
        for line in matrix[:mid]:
            top_left.append(line[:mid])

        top_right = []
        for line in matrix[:mid]:
            top_right.append(line[mid:])

        bottom_left = []
        for line in matrix[mid:]:
            bottom_left.append(line[:mid])

        bottom_right = []
        for line in matrix[mid:]:
            bottom_right.append(line[mid:])

        return top_left, top_right, bottom_left, bottom_right
    else:
        return None


def check_matrix(matrix):
    value = matrix[0][0]
    for line in matrix:
        for element in line:
            if value != element:
                return False
    return value


def build_quad_tree(matrix):
    def build_quad_tree_recursion(grid, node):
        quadrants = get_quadrants(grid)
        if quadrants is not None:
            for i, quadrant in enumerate(quadrants):
                if i == TOP_LEFT:
                    top_left_value = check_matrix(quadrant)
                    if top_left_value in {0, 1}:
                        new_node = None
                    else:
                        new_node = Node(None, False, None, None, None, None)
                        build_quad_tree_recursion(quadrant, new_node)
                    node.topLeft = new_node
                elif i == TOP_RIGHT:
                    top_right_value = check_matrix(quadrant)
                    if top_right_value in {0, 1}:
                        new_node = None
                    else:
                        new_node = Node(None, False, None, None, None, None)
                        build_quad_tree_recursion(quadrant, new_node)
                    node.topRight = new_node
                elif i == BOTTOM_LEFT:
                    bottom_left_value = check_matrix(quadrant)
                    if bottom_left_value in {0, 1}:
                        new_node = None
                    else:
                        new_node = Node(None, False, None, None, None, None)
                        build_quad_tree_recursion(quadrant, new_node)
                    node.bottomLeft = new_node
                elif i == BOTTOM_RIGHT:
                    bottom_right_value = check_matrix(quadrant)
                    if bottom_right_value in {0, 1}:
                        new_node = None
                    else:
                        new_node = Node(None, False, None, None, None, None)
                        build_quad_tree_recursion(quadrant, new_node)
                    node.bottomRight = new_node

            if top_left_value == top_right_value == bottom_left_value == bottom_right_value != False:
                node.val = top_left_value
                node.isLeaf = True
        else:
            node = Node(grid[0][0], True, None, None, None, None)

    root = Node(None, False, None, None, None, None)
    build_quad_tree_recursion(matrix, root)
    return root


def main():
    grid = [[0, 1], [1, 0]]
    quadrants = get_quadrants(grid)
    # print(quadrants)

    grid = [[1,1,0,0],[1,1,0,0],[0,0,1,1],[0,0,1,1]]
    quadrants = get_quadrants(grid)
    # print(quadrants)

    grid = [[1]]
    quadrants = get_quadrants(grid)
    # print(quadrants)


if __name__ == '__main__':
    main()