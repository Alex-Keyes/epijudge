import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

RED, WHITE, BLUE = range(3)

"""
I know that this is a solved djikstra problem I just don't remember what it was....
I think it has something to do with the pivot val, and then we use the pivot value to keep track of when we are done
we need need 3 vars 
i, j and n

why won't my array pass? 
It wouldn't pass because I was working off of the pivot index, not the value at that specific index.
Since I wasn't working on the value of the array at the pivot index, I wasn't searching anything.

"""


def dutch_flag_partition(pivot_index, A):
    pivot = A[pivot_index]
    i = 0
    j = 0
    n = len(A) - 1
    while j <= n:
        if A[j] < pivot:
            A[i], A[j] = A[j], A[i]
            i += 1
            j += 1
        elif A[j] > pivot:
            A[j], A[n] = A[n], A[j]
            n -= 1
        else:
            j += 1


@enable_executor_hook
def dutch_flag_partition_wrapper(executor, A, pivot_idx):
    count = [0, 0, 0]
    for x in A:
        count[x] += 1
    pivot = A[pivot_idx]

    executor.run(functools.partial(dutch_flag_partition, pivot_idx, A))

    i = 0
    while i < len(A) and A[i] < pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] == pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] > pivot:
        count[A[i]] -= 1
        i += 1

    if i != len(A):
        raise TestFailure('Not partitioned after {}th element'.format(i))
    elif any(count):
        raise TestFailure("Some elements are missing from original array")


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("dutch_national_flag.py",
                                       'dutch_national_flag.tsv',
                                       dutch_flag_partition_wrapper))
