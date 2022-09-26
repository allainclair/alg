from longest_word.longest_word_main import is_comprised_word


def test_comprised_word_simple_true():
    assert is_comprised_word(word="catdog", wordbook={"cat", "dog", "rat"}) is True


def test_comprised_word_simple_false():
    assert is_comprised_word(word="bear", wordbook={"cat", "dog", "rat"}) is False


def test_comprised_word_simple_two_truths():
    assert (
        is_comprised_word(word="catsdogcat", wordbook={"cat", "dog", "rat", "cats"})
        is True
    )


def test_comprised_word_simple_missing_one():
    assert is_comprised_word(word="catsdogcat", wordbook={"cat", "dog", "rat"}) is False


def test_comprised_word_small_true():
    assert is_comprised_word("abcd", {"ab", "cd", "ef"}) is True


def test_comprised_word_small_false():
    assert is_comprised_word("acbd", {"ab", "cd", "ef"}) is False


def test_comprised_word_exact_same():
    assert is_comprised_word(word="cat", wordbook={"cat", "dog"}) is False


def test_comprised_word_replaces_error():
    assert is_comprised_word(word="abasers", wordbook={"baser", "as"}) is False


def test_comprised_word_skip_larger_first_wordbook():
    assert is_comprised_word("blurbed", {"blurb", "bed", "blur"}) is True


def test_comprised_word_carboxymethyl_true():
    assert is_comprised_word("carboxymethyl", {"car", "carbo", "methyl", "xy"}) is True


def test_comprised_word_carboxymethyl_false():
    assert is_comprised_word("carboxymethyl", {"car", "carbo", "methyl", "bo"}) is False


def test_comprised_word_alkaloidal_true():
    assert is_comprised_word("alkaloidal", {"al", "alkaloid", "kaloidal"}) is True


def test_comprised_word_1():
    assert is_comprised_word('aaababa', {"a", "b", "aa"}) is True
