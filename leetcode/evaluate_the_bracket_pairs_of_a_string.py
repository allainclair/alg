# https://leetcode.com/problems/evaluate-the-bracket-pairs-of-a-string/

def main():
    pass


def evaluate(string, knowledge):
    knowledge = dict(knowledge)
    new_string = ''
    while string:
        string_and_new_segment = process(string, knowledge)
        if string_and_new_segment is not None:
            string, new_segment = string_and_new_segment
            new_string += new_segment
        else:
            break
    new_string += string
    return new_string


def process(string, knowledge):
    start_end = find_brackets(string)
    if start_end is not None:
        start, end = start_end
        token = string[start + 1:end - 1]
        token_value = knowledge[token]
        new_segment = string[:start] + token_value
        return string[end:], new_segment
    else:
        return None


def find_brackets(s):
    start = end = None
    for i, char in enumerate(s):
        if char == '(':
            start = i
        elif char == ')':
            end = i + 1
            break
    return (start, end) if start != end else None


def test_1():
    s = '(name)is(age)yearsold'
    knowledge = [['name', 'bob'], ['age', 'two']]
    assert evaluate(s, knowledge) == 'bobistwoyearsold'


def test_2():
    s = '(a)(a)(a)aaa'
    knowledge = [['a', 'yes']]
    assert evaluate(s, knowledge) == 'yesyesyesaaa'


def test_4():
    s = '(a)(b)'
    knowledge = [['a', 'b'], ['b', 'a']]
    assert evaluate(s, knowledge) == 'ba'


def test_find_bracket():
    s = '(abcd)abcd'
    assert find_brackets(s) == (0, 6)

    s = 'alovc(abcd)abcd'
    assert find_brackets(s) == (5, 11)

    s = 'alovcabcdabcd'
    assert find_brackets(s) == None


if __name__ == '__main__':
    main()
