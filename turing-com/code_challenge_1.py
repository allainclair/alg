

def call_points(ops):
    def sum_(scores):
        return scores + [int(scores[-1]) + int(scores[-2])]

    def double(scores):
        return scores + [int(scores[-1])*2]

    def invalidate(scores):
        return scores[:-1]

    map_ = {
        '+': sum_,
        'D': double,
        'C': invalidate,
    }

    scores = []
    for i, op in enumerate(ops):
        func = map_.get(op)
        if func is not None:
            scores = func(scores)
        else:  # It is a score.
            scores.append(int(op))

    return sum(scores)


def test1():
    ops = ['5', '2', 'C', 'D', '+']
    result = 30
    assert call_points(ops) == result
