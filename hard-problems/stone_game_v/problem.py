# https://leetcode.com/problems/stone-game-v/

def calc(stone_values):
    # Brute force

    def calc_rec(stone_values, previous_sum):
        if len(stone_values) < 2:
            return previous_sum

        n_slices = len(stone_values) - 1
        results = []
        for slice in range(n_slices):
            left, right = stone_values[:slice+1], stone_values[slice+1:]
            print('left', left)
            print('right', right)
            left_sum, right_sum = sum(left), sum(right)
            left_result = previous_sum + left_sum
            right_result = previous_sum + right_sum
            if left_result < right_result:
                result = calc_rec(left, left_result)
            elif left_result > right_result:
                result = calc_rec(right, right_result)
            else:
                result = max(calc_rec(left, left_result), calc_rec(right, right_result))
            results.append(result)

        return max(results)

    def lookup(pair, mapping):
        return mapping.get(pair, None)


    def calc_rec_2(stone_values, previous_sum, start, end):
        n_slices = end - start - 1
        if n_slices < 1:
            print('base case', previous_sum)
            return previous_sum
        results = []
        print('START, END', start, end)
        print('stone_values', stone_values)
        print('n_slices', n_slices)
        # print(mapping)
        for slice in range(n_slices):
            cut = start + slice + 1
            print('start, end', start, end)
            print('cut', cut)

            left, right = stone_values[start:cut], stone_values[cut:end]
            print('left', left, (start, cut))
            print('right', right, (cut, end))
            left_sum, right_sum = sum(left), sum(right)
            left_result = previous_sum + left_sum
            right_result = previous_sum + right_sum

            if left_result < right_result:
                result = lookup((start, cut), mapping)
                if result is None:
                    result = calc_rec_2(stone_values, left_result, start, cut)
                    mapping[(start, cut)] = result
                # print('LEFT LESSER')
                # print('left', left, left_sum, left_result)
                # print('result', result)
            elif left_result > right_result:
                result = lookup((cut, end), mapping)
                if result is None:
                    result = calc_rec_2(stone_values, right_result, cut, end)
                    mapping[(cut, end)] = result
                # print('RIGHT LESSER')
                # print('right', right, right_sum, right_result)
                # print('result', result)
            else:
                l_result = lookup((start, cut), mapping)
                if l_result is None:
                    l_result = calc_rec_2(stone_values, left_result, start, cut)
                    mapping[(start, cut)] = l_result

                # print('left', left, left_sum, left_result)
                r_result = lookup((cut, end), mapping)
                if r_result is None:
                    r_result = calc_rec_2(stone_values, right_result, cut, end)
                    mapping[(cut, end)] = r_result
                # print('right', right, right_sum, right_result)

                result = max(l_result, r_result)
                # print('result', result)

            results.append(result)

        return max(results)

    mapping = {}
    return calc_rec_2(stone_values, 0, 0, len(stone_values))


def main():
    stone_value = [6, 2, 3, 4, 5, 5]
    result = calc(stone_value)
    print(result)
    assert result == 18

    stone_value = [7, 7, 7, 7, 7, 7, 7]
    result = calc(stone_value)
    print(result)
    assert result == 28

    stone_value = [1, 1, 2]
    result = calc(stone_value)
    print(result)
    assert result == 3


if __name__ == '__main__':
    main()
