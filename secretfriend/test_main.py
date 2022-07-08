from main import secretfriend


def test_1_consistence():
    friends = {1}
    assert secretfriend(friends) is None


def test_2_consistence():
    friends = {1, 2}
    output = {(1, 2), (2, 1)}
    assert secretfriend(friends) == output


def test_3_consistence():
    # We want a "circle form" secret friend. This way for 3 friends, there are
    # only 2 possible circular outputs.
    friends = {1, 2, 3}
    output1 = {(1, 2), (2, 3), (3, 1)}
    output2 = {(2, 1), (1, 3), (3, 2)}
    result = secretfriend(friends)
    assert result == output1 or result == output2


def test_n_consistence():
    size = 5
    friends = set(range(size))

    # Create adjacency to check if there is a circular form
    result = secretfriend(friends)
    adjacency = {}
    for friend1, friend2 in result:
        adjacency[friend1] = friend2

    # Add 'size' friends walking through the adjacencies.
    list_ = [friend1]
    for _ in range(len(friends) -1):
        friend = adjacency[friend1]
        list_.append(friend)
        friend1 = friend

    # At the end we need all the friend in the 'list_'.
    assert len(list_) == len(friends)
    assert set(list_) == friends


if __name__ == '__main__':
    test_1_consistence()
    test_2_consistence()
    test_3_consistence()
    test_n_consistence()
