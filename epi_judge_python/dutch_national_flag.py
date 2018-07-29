import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

RED, WHITE, BLUE = range(3)


def dutch_flag_partition(pivot_index, A):
    """Write a program that takes an array A and an index i into A,
    and rearranges the elements such that all elements less than A[i] (the “pivot”) appear first,
    followed by elements equal to the pivot, followed by elements greater than the pivot."""
    pivot_val = A[pivot_index]
    low = 0
    iterator = 0
    high = len(A) - 1

    while iterator <= high:
        if A[iterator] < pivot_val:
            # if A iter is less than pivot swap A low and A iterator, increment both
            A[low], A[iterator] = A[iterator], A[low]
            low += 1
            iterator += 1
        elif A[iterator] > pivot_val:
            # if greater than, swap A iter and A high
            A[iterator], A[high] = A[high], A[iterator]
            high -= 1
        else:
            iterator += 1
    return A


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
    # print(i)
    # print(len(A))
    if i != len(A):
        raise TestFailure('Not partitioned after {}th element'.format(i))
    elif any(count):
        raise TestFailure("Some elements are missing from original array")


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("dutch_national_flag.py",
                                       'dutch_national_flag.tsv',
                                       dutch_flag_partition_wrapper))
