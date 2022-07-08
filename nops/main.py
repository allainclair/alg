from icecream import ic
from collections import defaultdict


def main():
    file_path = input('Please specify the input file location: ')
    number_of_longest_words = int(input(
        'Please specify the number of longest words to output (default 2): ')) or 2

    words = set()
    with open(file_path) as file:
        for line in file:
            words.add(line.strip())

    comprised_word = set()
    for word in words:
        working_set = words - {word}
        if is_comprised_other_words(word, working_set):
            comprised_word.add(word)
    ic(len(comprised_word))



def is_not_comprised_word(word, words):
    return not any(True for w in words if word in w)


def get_removing_intervals(word, words):
    removing_words = defaultdict(list)
    for w in words:
        index = word.find(w)
        while index > -1:
            start_index = index
            end_index = index + len(w)
            removing_words[w].append((start_index, end_index))
            index = word.find(w, end_index)
    return removing_words


def is_comprised_other_words(word, words):
    removing_intervals = get_removing_intervals(word, words)
    # Let's mark the word's interval.
    # To be a 'comprised_other_words' we need all(marks).
    # It means we have words from 'words' to match all chars in the 'word' arg.
    marks = [False]*len(word)
    for w, intervals in removing_intervals.items():
        for interval in intervals:
            start, end = interval
            marks[start:end] = [True]*(end - start)

    removing_words = sorted(removing_intervals, reverse=True)
    return all(marks)


ALL_WORDS = {
        'boar',
        'cat',
        'cats',
        'catsdogcats',
        'catxdogcatsrat',
        'dog',
        'dogs',
        'dogcatsdogsboar',
        'hippopotamuses',
        'rat',
        'ratcatdogcat',
}

def test_get_removing_intervals():
    word = 'dogcatsdogsboar'
    result = {
        'boar': [(11, 15)],
        'cat': [(3, 6)],
        'cats': [(3, 7)],
        'dog': [(0, 3), (7, 10)],
        'dogs': [(7, 11)],
    }
    words = ALL_WORDS - {word}
    removing_intervals = get_removing_intervals(word, words)
    assert result == removing_intervals

    word = 'aaaabaaabaa'
    words = {'a', 'aa', 'aaa', 'aaaa'}
    removing_intervals = get_removing_intervals(word, words)
    ic(removing_intervals)


def test_is_not_comprised_word():
    assert is_not_comprised_word('cats', {'cat', 'dog', 'rat'})
    assert not is_not_comprised_word('cat', {'cat', 'dog', 'rat'})
    assert is_not_comprised_word('dogs', {'cat', 'dog', 'rat'})
    assert not is_not_comprised_word('dog', {'cat', 'dogs', 'rat'})


def test_1():
    word = 'cats'
    words = ALL_WORDS - {word}
    assert not is_comprised_other_words(word, words)

    word = 'catsdogcats'
    words = ALL_WORDS - {word}
    assert is_comprised_other_words(word, words)

    word = 'ratcatdogcat'
    words = ALL_WORDS - {word}
    assert is_comprised_other_words(word, words)

    word = 'dogs'
    words = ALL_WORDS - {word}
    assert not is_comprised_other_words(word, words)

    word = 'dogcatsdogsboar'
    words = ALL_WORDS - {word}
    assert is_comprised_other_words(word, words)

    assert not is_comprised_other_words("abasers", {"baser", "as"})
    assert is_comprised_other_words("blurbed", {"blurb", "bed", "blur"})
    assert is_comprised_other_words("carboxymethyl", {"car", "carbo", "methyl", "xy"})
    assert is_comprised_other_words("alkaloidal", {"al", "alkaloid", "kaloidal"})
    assert not is_comprised_other_words("carboxymethyl", {"car", "carbo", "methyl", "bo"})
    assert is_comprised_other_words('aaababa', {"a", "b", "aa"})


if __name__ == '__main__':
    # test_get_removing_intervals()
    # test_is_not_comprised_word()
    test_1()
    # main()
