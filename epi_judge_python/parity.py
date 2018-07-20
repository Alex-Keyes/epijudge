from test_framework import generic_test


def parity(x):
    """ Compute the parity of a word, returning 1 if it's bits are odd, 0 if it's even """
    # okay we need to count the number of bits and then return 1 if the count is odd, otherwise return false
    bit_count = 0
    while x:
        bit_count += x & 1
        x >>= 1

    if bit_count % 2 == 0:
        return 0
    else:
        return 1


# This version of parity is _much_ faster than the brute force party Such is the power of divide and conquer!
def parity_fast(x):
    x ^= x >> 32
    x ^= x >> 16
    x ^= x >> 8
    x ^= x >> 4
    x ^= x >> 2
    x ^= x >> 1
    return x & 0x1


if __name__ == '__main__':
    exit(generic_test.generic_test_main("parity_fast.py", 'parity.tsv', parity_fast))
