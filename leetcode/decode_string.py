# https://leetcode.com/problems/decode-string/
# There is recursive inputs

# INCOMPLETE
# First idea: Stack approach
# 1. Stack number and something (normal text and repeated text inside)

def decodeString(s):
    result = ''
    encoded = False
    encoded_string = ''
    for char in s:
        if char.isdigit():
            multiplier = int(char)
            encoded = True
        elif encoded:
            if char == '[':
                pass
            elif char == ']':
                encoded_string *= multiplier
                result += encoded_string
                encoded_string = ''
                encoded = False
            else:
                encoded_string += char
        else:
            result += char
    return result


def test_decode_0():
    s = ''
    result = ''
    assert decodeString(s) == result


def test_decode_1():
    s = 'aabb'
    result = 'aabb'
    assert decodeString(s) == result


def test_decode_2():
    s = 'aabb1[c]'
    result = 'aabbc'
    assert decodeString(s) == result


def test_decode_3():
    s = "3[a]2[bc]"
    result = "aaabcbc"
    assert decodeString(s) == result


def test_decode_4():
    s = "3[a2[c]]"
    result = "accaccacc"

#
# if __name__ == '__main__':
#     test_decode0()

