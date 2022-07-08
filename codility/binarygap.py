# https://app.codility.com/programmers/lessons/1-iterations/binary_gap/

def binarygap(n):
    binstr = bin(n)[2:]
    print(binstr)
    zeros_splitted = binstr.split('1')
    print(zeros_splitted)
    max_zeros = max(zeros_splitted)
    # Incomplete, need another condition below.
    return len(max_zeros) if len(zeros_splitted) > 2 else 0



def main():
    n = 1041
    assert binarygap(n) == 5

    n = 32
    assert binarygap(n) == 0


if __name__ == '__main__':
    main()
