import itertools

ascii_value_generator = (ord(char) for char in itertools.cycle('Close'))  # Get integer ASCII values
integers = [67, 175, 286, 401, 502, 569, 677, 788, 903, 1004]
print([integer - next(ascii_value_generator) for integer in integers])
