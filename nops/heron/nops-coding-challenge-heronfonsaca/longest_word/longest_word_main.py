from collections import Counter
from itertools import combinations, permutations
from typing import Set, List


def is_comprised_two_words(word: str, wordbook: Set[str]) -> bool:
    """Checks if a word is comprised of exactly two words (most cases)
    of the wordbook. Works by splitting the word from end to middle.

    Args:
        word: word to be checked.
        wordbook: complete list of words (or dictionary).

    Returns:
        A boolean value if the word is or is not comprised of
        two wordbook words.
    """
    for i in range(2, len(word) // 2 + 1):
        if word[-i:] in wordbook and word[:-i] in wordbook:
            return True
    return False


def extract_intersected_fragments(word: str, wordbook: Set[str]) -> Set[str]:
    """Extract fragments of at least two letters from word and
    intersect them with wordbook to generate substrings of interest.

    Args:
        word: word to be checked.
        wordbook: complete list of words (or dictionary).

    Returns:
        List of intersected fragments of word with wordbook.
    """
    fragments = set(
        word[i:j] for i in range(len(word)) for j in range(i + 2, len(word) + 1)
    )
    intersections = fragments.intersection(wordbook)
    if word in intersections:
        intersections.remove(word)
    return intersections


def is_comprised_word(word: str, wordbook: Set[str]) -> bool:
    """Checks if a word is comprised of smaller words of the wordbook.
    Lists of mixes (combinations) of fragments are generated and them
    permutated to create sequences of fragments that can fully replace the
    original word.

    Args:
        word: word to be checked.
        wordbook: complete list of words (or dictionary).

    Returns:
        A boolean value if the word is or is not comprised of
        two wordbook words.
    """
    if is_comprised_two_words(word, wordbook):
        return True

    fragments = extract_intersected_fragments(word, wordbook)
    for combination_length in range(1, len(word) // 2 + 1):
        mixes = [
            list(Counter(comb).keys())
            for comb in list(combinations(fragments, combination_length))
        ]
        for mix in mixes:
            mix_joined = "".join(mix)
            if len(mix_joined) > len(word):
                continue
            if Counter(mix_joined).keys() != Counter(word).keys():
                continue
            for order in permutations(mix, len(mix)):
                word_temporary = word
                for word_checking in order:
                    word_temporary = word_temporary.replace(word_checking, ".")
                if not word_temporary.replace(".", ""):
                    return True
    return False


def extract_sorted_comprised_words(wordbook: Set[str]) -> List[str]:
    """
    Extracts comprised words from the wordbook and stores them in a
    List sorted by the length of each element in reverse order.

    Args:
        wordbook: complete list of words (or dictionary).

    Returns:
        List of comprised words sorted by the length
        of each element in reverse order.
    """
    return sorted(
        [word for word in wordbook if is_comprised_word(word, wordbook)],
        key=len,
        reverse=True,
    )


if __name__ == "__main__":
    words: Set[str] = set()
    while len(words) < 1:
        file_path = input("Please specify the input file location: ")
        try:
            with open(file_path, "r") as txt_file:
                words = set(txt_file.read().splitlines())
        except:
            print("Something went wrong. Try again.")

    words_count = 2
    try:
        words_count = int(input("Please specify the number of longest words to output (default 2): "))
        if words_count < 0:
            raise Exception
    except:
        print("Setting number of longest words to 2 words.")

    words_comprised = extract_sorted_comprised_words(words)
    for word_comprised in words_comprised[:words_count]:
        print(word_comprised)
    print(f"Number of words comprised of other words: {len(words_comprised)}")
