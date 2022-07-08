# Write a function checking that the given string is valid. We consider a string
# to be valid if all the characters of the string have exactly the same frequency.

# Examples:
# "aabbcc" is a valid string     => [a = 2, b = 2, c = 2]
# "aabbccc" is an invalid string => [a = 2, b = 2, c = 3]


# Check if the string is valid as it is (same condition as before) or if one character
# at one position can be removed from the string so it will become valid.
# "aabbccc" is an valid string => [a = 2, b = 2, c = 3] => 3 - 1 => [a = 2, b = 2, c = 2]

# "aabbcccddd"

import collections


def check_letters(string):
    counter = collections.Counter(string)  # c = {'a': 2, 'b': 2. 'c': 3, 'd': 3}
    set_ = set(counter.values())
    values_counter = collections.Counter(counter.values())

    values = list(values_counter.values())
    keys = list(values_counter.keys())

    if len(values) == 2:
        first = values[0] > 1 and values[1] == 1
        second = values[1] > 1 and values[0] == 1
        third = abs(keys[1] - keys[0]) == 1
        return (first or second) and third
    elif len(set_) == 1:
        return True
    else:
        return False


def main():
    input1 = "aabbcc"
    assert check_letters(input1) == True

    input2 = "aabbccc"
    assert check_letters(input2) == True

    input2 = "aabbbbaaacccc"
    assert check_letters(input2) == True

    input2 = "aabbbbaacccccc"
    assert check_letters(input2) == False

    input2 = "aabbbbaaccccc"
    assert check_letters(input2) == True

    input2 = "aabbcccddd"
    assert check_letters(input2) == False

    input2 = "aabbccccdddd"
    assert check_letters(input2) == False

    input2 = "aabbccdddd"
    assert check_letters(input2) == False


if __name__ == '__main__':
    main()
