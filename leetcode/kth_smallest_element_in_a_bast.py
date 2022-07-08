class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def change_list(list_):
    list_ = [1, 2, 3, 4]
    return list_


def main():
    list_ = [1]
    changed_list_returned = change_list(list_)
    print(changed_list_returned)
    print(list_)


if __name__ == '__main__':
    main()
