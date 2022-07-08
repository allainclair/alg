# https://leetcode.com/problems/range-frequency-queries/

class RangeFreqQuery:

    def __init__(self, arr):
        self.arr = arr

    def query(self, left, right, value):
        sub_array = self.arr[left:right+1]
        return sub_array.count(value)


def test_1():
    arr = [12, 33, 4, 56, 22, 2, 34, 33, 22, 12, 34, 56]
    left, right, value = 1, 2, 4
    obj = RangeFreqQuery(arr)
    assert obj.query(left, right, value) == 1

    left, right, value = 0, 11, 33
    obj = RangeFreqQuery(arr)
    assert obj.query(left, right, value) == 2
