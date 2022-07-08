"""
HOURS            00 01 02 03 04 05 06 07 08 09 10 11 12 13 14 15 16 17
8-12 14-16                               |------------|    |------|
9-10 11-12 13-15                            |---| |---| |------|

+1 instance for times_windows2: 09-16       |--------------------|
Send to sanjay@landing.ai
"""

DAILY_HOURS = 24


def is_overlap(hour, time_window):
    start, end = time_window
    return start <= hour <= end


def n_students1(times_windows):
    """Count how many overlaps there is in every hour.
    And we return the max_overlap.

    Efficiency:
    O(k*n). k = number of hours, n = number of time_windows.
    If k is constant -> O(n).
    """
    max_overlap = 0
    for hour in range(DAILY_HOURS):
        overlap = 0
        for time_window in times_windows:
            if is_overlap(hour, time_window):
                overlap += 1
                if overlap > max_overlap:
                    max_overlap = overlap
    return max_overlap


def main():
    # 2 test cases

    times_windows1 = [[14, 16], [9, 10], [13, 15], [8, 12], [11, 12]]
    return_ = n_students1(times_windows1)
    assert return_ == 2

    times_windows2 = [[14, 16], [9, 16], [9, 10], [13, 15], [8, 12], [11, 12]]
    return_ = n_students1(times_windows2)
    assert return_ == 3


if __name__ == '__main__':
    main()
