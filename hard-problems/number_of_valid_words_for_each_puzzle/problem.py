# https://leetcode.com/problems/number-of-valid-words-for-each-puzzle/

def find_num_valid(words, puzzles):
    answers = [0]*len(puzzles)
    # print(words)
    # print(puzzles)
    for i, puzzle in enumerate(puzzles):
        first_letter = puzzle[0]
        # print('first_letter:', first_letter)
        # print('puzzle:', puzzle)
        puzzleset = set(puzzle)
        for word in words:
            # print(word)
            if first_letter in word:
                # print('len(word)', len(word))
                answers[i] += sum(1 for char in word if char in puzzleset) == len(word)
        # print()
    # print(answers)
    return answers



def main():
    words = ["aaaa", "asas", "able", "ability", "actt", "actor", "access"]
    puzzles = ["aboveyz", "abrodyz", "abslute", "absoryz", "actresz", "gaswxyz"]
    assert find_num_valid(words, puzzles) == [1, 1, 3, 2, 4, 0]


if __name__ == '__main__':
    main()
