"""https://leetcode.com/problems/n-ary-tree-level-order-traversal/"""


def level_order(root):
    def level_order_rec(node, list_):
        if node is not None:
            list_.append(node.children)
        else:
            pass

    l = []
    l.append([root.val])
    level_order_rec(root, l)
    return l


def main():
    root = [1, None, 3, 2, 4, None, 5, 6]


if __name__ == '__main__':
    main()
