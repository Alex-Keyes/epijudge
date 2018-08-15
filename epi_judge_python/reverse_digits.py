from test_framework import generic_test

# write a function that reversed the digit of an integer passed to it
"""
Q: why don't we convert the integer to a string and then return the reversed string?
A: no dice, that doesn't work for negative test cases...
Q: hah no shit that worked. 
A: that being said, it's probably a bit faster to do something a bit faster than how this works

maybe we can see if the string input thing works

interesting that the 'faster' algorithm isn't actually much faster
"""


def reverse(x):
    str_x = str(x)
    if str_x[0] == '-':
        rev_str = str_x[:0:-1]
        rev_str = '-' + rev_str
    else:
        rev_str = str_x[::-1]
    return int(rev_str)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("reverse_digits.py",
                                       'reverse_digits.tsv', reverse))
