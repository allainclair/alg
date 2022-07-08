# https://leetcode.com/problems/find-k-closest-elements/

def closest_index(arr, x):
    start, end = 0, len(arr) - 1
    mid = int((end - start) / 2)
    while start <= end:
        mid = int((end + start) / 2)
        if arr[mid] < x:
            start = mid + 1
        elif arr[mid] > x:
            end = mid - 1
        else:
            return mid

    print('mid', mid)
    # print('mid-1', mid-1)
    # print('arr[mid-1]', arr[mid-1])
    if mid-1 < 0:
        return 0
    # elif mid+1 > len(arr) -1:
    #     return len(arr) - 1

    # print()
    # print(abs(arr[mid-1] - x))
    # print(abs(arr[mid] - x))
    # print(abs(arr[mid+1] - x))

    if abs(arr[mid-1] - x) <= abs(arr[mid] - x):
        return mid-1
    else:
        return mid
    # print()


def k_closest(arr, k, x):
    index = closest_index(arr, x)
    ret = []
    prev = index - 1
    post = index + 1
    for i in range(k):
        print(prev, index, post)
        ret.append(arr[index])
        if prev > -1:
            dist_prev = abs(arr[prev] - x)
            print('dist_prev', dist_prev)
        else:
            dist_prev = float('inf')
        if post < len(arr):
            dist_post = abs(arr[post] - x)
            print('dist_post', dist_post)
        else:
            dist_post = float('inf')
        if dist_prev <= dist_post:
            index = prev
            prev -= 1
        else:
            index = post
            post += 1
    print(ret)
    return ret


def main():
    # test_closest_index()

    arr = [1, 2, 3, 4, 5]
    k, x = 4, 3
    assert sorted(k_closest(arr, k, x)) == [1, 2, 3, 4]

    arr = [1, 2, 3, 4, 5]
    k, x = 4, -1
    assert sorted(k_closest(arr, k, x)) == [1, 2, 3, 4]



def test_closest_index():
    arr = list(range(100))
    for i, element in enumerate(arr):
        assert closest_index(arr, element) == i

    # arr = [1, 2, 3, 4]
    # ret = closest_index(arr, 10)
    # assert ret == 3
    # ret = closest_index(arr, -10)
    # assert ret == 0

    arr = [1, 10, 20, 30]

    ret = closest_index(arr, 10)
    assert ret == 1

    ret = closest_index(arr, 2)
    assert ret == 0

    ret = closest_index(arr, 12)
    assert ret == 1

    ret = closest_index(arr, 18)
    assert ret == 2

    ret = closest_index(arr, 20)
    assert ret == 2

    ret = closest_index(arr, 21)
    assert ret == 2

    ret = closest_index(arr, 29)
    assert ret == 3

    ret = closest_index(arr, 31)
    assert ret == 3

    ret = closest_index(arr, 40)
    assert ret == 3


if __name__ == '__main__':
    main()
