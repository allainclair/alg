"""https://leetcode.com/problems/two-sum-iv-input-is-a-bst/"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def add_leaf(root, element):
    if element:
        if element < root.val:
            if root.left is not None:
                add_leaf(root.left, element)
            else:
                root.left = TreeNode(element)
        else:
            if root.right is not None:
                add_leaf(root.right, element)
            else:
                root.right = TreeNode(element)


def buildtree(list_):
    root = TreeNode(list_[0])
    for element in list_[1:]:
        add_leaf(root, element)
    return root


def tree_to_list(root, k):
    def tree_to_list_recursion(root, list_):
        ret = False
        if root.left:
            ret = tree_to_list_recursion(root.left, list_)
        print(root.val)
        print(list_)
        if not ret:
            for element in list_:
                print('element + root.val', element + root.val)
                if element + root.val == k:
                    return True
            list_.append(root.val)
            if root.right:
                return tree_to_list_recursion(root.right, list_)
        else:
            return True

    list_ = []
    return tree_to_list_recursion(root, list_) is not None


def find_target(root, k):
    list_ = tree_to_list(root)
    for i, element1 in enumerate(list_[:-1]):
        for element2 in list_[i+1:]:
            if element1 + element2 == k:
                return True
    return False


def main():
    # list_, k = [5, 3, 6, 2, 4, None, 7], 9
    # root = buildtree(list_)
    # assert tree_to_list(root, k)

    list_, k = [2, 1, 3], 4
    root = buildtree(list_)
    assert tree_to_list(root, k)


if __name__ == '__main__':
    main()
