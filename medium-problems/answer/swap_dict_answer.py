"""Create a function that takes:

1. A list of keys.
2. A list of values (same size).
3. True, if key and value should be swapped, else False.

The function returns the constructed dict. Empty lists return an empty dict.

To make it simple, use only hashable (= immutable) keys.
To make it simple, use only unique keys.

It validates python:
1. The use of zip
2. Swap variables using tuple syntax.
3. Comprehensions (swap_dict4) or dict function on tuples (swap_dict5)
4. iteration without indexing
5. good naming variables (Avoid using i, j, s, etc)

Source: https://edabit.com/challenge/cEzT2e8tLpwYnrstP
"""


def swap_dict1(list1, list2, swap_flag):
    pass  # I don't know.


def swap_dict2(list1, list2, swap_flag):
    new_dict = {}
    for element1, element2 in zip(list1, list2):
        new_dict[element1] = element2

    if swap_flag:
        new_dict = {value: key for key, value in new_dict.items()}
    return new_dict


def swap_dict3(list1, list2, swap_flag):
    if swap_flag:
        list1, list2 = list2, list1

    new_dict = {}
    for element1, element2 in zip(list1, list2):
        new_dict[element1] = element2
    return new_dict


def swap_dict4(list1, list2, swap_flag):
    if swap_flag:
        list1, list2 = list2, list1

    return {element1: element2 for element1, element2 in zip(list1, list2)}


def swap_dict5(list1, list2, swap_flag):
    if swap_flag:
        list1, list2 = list2, list1
    return dict(zip(list1, list2))


def swap_dict6(list1, list2, swap_flag):
    return dict(zip(list2, list1)) if swap_flag else dict(zip(list1, list2))


def test_swap_dict(swap_function):
    list1 = [1, 2, 3, 4, 5]
    list2 = ['a', 'b', 'c', 'd', 'e']
    check_dict = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}
    assert swap_function(list1, list2, False) == check_dict

    check_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
    assert swap_function(list1, list2, True) == check_dict

    assert swap_function([], [], True) == {}


def test_main():
    for swap_function in [swap_dict2, swap_dict3, swap_dict4, swap_dict5, swap_dict6]:
        test_swap_dict(swap_function)


if __name__ == '__main__':
    test_main()

