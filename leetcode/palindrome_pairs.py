# https://leetcode.com/problems/palindrome-pairs/

def palindrome(word):
    control_index = len(word)//2
    segment1 = word[:control_index]
    segment2 = word[::-1][:control_index]
    return segment1 == segment2


def palindrome_pairs(words):
    index_pairs = []
    for i, w1 in enumerate(words):
        for j, w2 in enumerate(words):
            if i != j and palindrome(w1 + w2):
                index_pairs.append([i, j])
    # print(index_pairs)
    return index_pairs


def main():
    assert palindrome('abcdcba')
    assert not palindrome('abcdcbd')
    assert palindrome('abcddcba')
    assert not palindrome('abcddcbz')

    words = ["abcd", "dcba", "lls", "s", "sssll"]
    assert palindrome_pairs(words) == [[0, 1], [1, 0], [3, 2], [2, 4]]


if __name__ == '__main__':
    main()
