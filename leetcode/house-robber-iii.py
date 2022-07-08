# https://leetcode.com/problems/house-robber-iii/solution/

def main():
    input = [3, 2, 3, None, 3, None, 1]
    root = build_tree(input)
    print_tree(root)
    print()

    input = [3, 4, 5, 1, 3, None, 1]
    root = build_tree(input)
    print_tree(root)


def print_tree(root):
    if root.left is not None:
        print_tree(root.left)
    print(f'{root.val} ')
    if root.right is not None:
        print_tree(root.right)


def build_tree(list_):
    """Build binary tree given a list of nodes"""
    root = TreeNode(list_[0])
    x = [root]
    nextchildren = 'left'
    for value in list_[1:]:
        if nextchildren == 'left':
            node = x.pop(0)
            if value is not None:
                newnode = TreeNode(value)
                node.left = newnode
                x.append(newnode)
            nextchildren = 'right'
        elif nextchildren == 'right':
            if value is not None:
                newnode = TreeNode(value)
                node.right = newnode
                x.append(newnode)
            nextchildren = 'left'
    return root


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


if __name__ == '__main__':
    main()
