"""
Create a function that determines whether each seat can "see"
the front-stage. A number can "see" the front-stage if it is
strictly greater than the number before it.

Everyone can see the front-stage in the example below:

# FRONT STAGE
[[1, 2, 3, 2, 1, 1],
[2, 4, 4, 3, 2, 2],
[5, 5, 5, 5, 4, 4],
[6, 6, 7, 6, 5, 5]]

# Starting from the left, the 6 > 5 > 2 > 1, so all numbers can see.
# 6 > 5 > 4 > 2 - so all numbers can see, etc.

Not everyone can see the front-stage in the example below:

# FRONT STAGE
[[1, 2, 3, 2, 1, 1],
[2, 4, 4, 3, 2, 2],
[5, 5, 5, 10, 4, 4],
[6, 6, 7, 6, 5, 5]]

# The 10 is directly in front of the 6 and blocking its view.
The function should return True if every number can see the front-stage, and False
if even a single number cannot.

Examples
can_see_stage([
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]) ➞ True

can_see_stage([
  [0, 0, 0],
  [1, 1, 1],
  [2, 2, 2]
]) ➞ True

can_see_stage([
  [2, 0, 0],
  [1, 1, 1],
  [2, 2, 2]
]) ➞ False

can_see_stage([
  [1, 0, 0],
  [1, 1, 1],
  [2, 2, 2]
]) ➞ False

Number must be strictly smaller than
the number directly behind it.

1. Create some test cases to check your code.

2. Create a "Person Entity" with its height based on the first test case.
   You can use only a height property for the person entity. We want to access
   the "person.height" for example.
3. This way, create a function that returns a list of people based

It validates python:
1. len and zip function
2. iteration without indexing

Source: https://edabit.com/challenge/xbjDMxzpFcsAWKp97
"""


def check_seats1(seats):
    line_len = len(seats[0])
    front_seats = [-1]*line_len
    for line_seats in seats:
        for seat, front_seat in zip(line_seats, front_seats):
            if seat <= front_seat:
                return False
        front_seats = line_seats
    return True


def check_seats2(seats):
    """Still trying"""
    line_len = len(seats[0])
    front_seats = [-1]*line_len

    # return (for front_seats, back_seats in zip(seats[1:], seats[:-1]))


def strictly_increasing(arr):
    return all(x < y for x, y in zip(arr, arr[1:]))


def check_seats3(seats):
    transpose = list(zip(*seats))
    return all(strictly_increasing(x) for x in transpose)


def check_seats4(seats):
    return all(sorted(set(row)) == list(row) for row in zip(*seats))


def check_seats5(seats):
    seats = np.array(seats)
    return np.all(seats[1:] - seats[:-1] > 0)


def check_seats6(seats):
    """Indexed for. Bottom up"""
    line_len, column_len = len(seats), len(seats[0])
    for j in range(column_len):
        for i in range(line_len - 1, 0, -1):
            if seats[i][j] < seats[i-1][j]:
                return False
    return True


def test_seats(seats_function):
    seats = [[1, 2, 3, 2, 1, 1],
            [ 2, 4, 4, 3, 2, 2],
            [ 5, 5, 5, 5, 4, 4],
            [ 6, 6, 7, 6, 5, 5]]
    assert seats_function(seats)

    seats = [[1, 2, 3, 2,  1, 1],
            [ 2, 4, 4, 3,  2, 2],
            [ 5, 5, 5, 10, 4, 4],
            [ 6, 6, 7, 6,  5, 5]]
    assert not seats_function(seats)


def test_main():
    for seats_function in [check_seats1, check_seats6]:
        test_seats(seats_function)


if __name__ == '__main__':
    test_main()
