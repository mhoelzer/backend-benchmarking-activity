"""
Various sorting algorithms adapted from
python3.codes/popular-sorting-algorithms
"""
from copy import deepcopy
from heapq import merge
import random

random_seq = range(5000)
random.shuffle(random_seq)

def bubble_sort(seq):
    d_seq = deepcopy(seq)
    changed = True

    while changed:
        changed = False
        for i in range(len(d_seq) - 1):
            if d_seq[i] > d_seq[i+1]:
                d_seq[i], d_seq[i+1] = d_seq[i+1], d_seq[i]
                changed = True

    return d_seq


def insertion_sort(seq):
    d_seq = deepcopy(seq)

    for i in range(1, len(d_seq)):
        j = i - 1
        key = d_seq[i]

        while (d_seq[j] > key) and (j >= 0):
            d_seq[j+1] = d_seq[j]
            j -= 1

        d_seq[j+1] = key

    return d_seq


def insertion_sort_bin(seq):
    d_seq = deepcopy(seq)

    for i in range(1, len(d_seq)):
        key = seq[i]
        # invariant: ``seq[:i]`` is sorted
        # find the least `low' such that ``seq[low]`` is not less then `key'.
        # Binary search in sorted sequence ``seq[low:up]``:
        low, up = 0, i
        while up > low:
            middle = (low + up) // 2
            if d_seq[middle] < key:
                low = middle + 1
            else:
                up = middle
        # insert key at position ``low``
        d_seq[:] = d_seq[:low] + [key] + d_seq[low:i] + d_seq[i + 1:]

    return d_seq


def selection_sort(seq):
    d_seq = deepcopy(seq)

    for i, item in enumerate(d_seq):
        mn = min(range(i, len(d_seq)), key=d_seq.__getitem__)
        d_seq[i], d_seq[mn] = d_seq[mn], item

    return d_seq


def merge_sort(seq):
    d_seq = deepcopy(seq)

    if len(d_seq) <= 1:
        return d_seq

    middle = len(d_seq) // 2
    left = merge_sort(d_seq[:middle])
    right = merge_sort(d_seq[middle:])

    return list(merge(left, right))


def heapify(seq, end, i):
    left = 2 * i + 1
    right = 2 * (i + 1)
    high = i

    if left < end and seq[i] < seq[left]:
        high = left

    if right < end and seq[high] < seq[right]:
        high = right

    if high != i:
        seq[i], seq[high] = seq[high], seq[i]
        seq = heapify(seq, end, high)

    return seq


def heap_sort(seq):
    d_seq = deepcopy(seq)
    end = len(d_seq)
    start = end // 2 - 1

    for i in range(start, -1, -1):
        heapify(d_seq, end, i)

    for i in range(end-1, 0, -1):
        d_seq[i], d_seq[0] = d_seq[0], d_seq[i]
        d_seq = heapify(d_seq, i, 0)

    return d_seq


def quick_sort(seq):
    d_seq = deepcopy(seq)

    less = []
    pivotList = []
    more = []

    if len(d_seq) <= 1:
        return d_seq

    else:
        pivot = d_seq[0]
        for i in d_seq:
            if i < pivot:
                less.append(i)
            elif i > pivot:
                more.append(i)
            else:
                pivotList.append(i)
        less = quick_sort(less)
        more = quick_sort(more)
        return less + pivotList + more


if __name__ == "__main__":

    print "random_seq before: {}\n".format(random_seq)

    algorithms = [
        bubble_sort, insertion_sort, insertion_sort_bin, selection_sort,
        merge_sort, heap_sort, quick_sort]

    for algorithm in algorithms:
        print "{}: {}".format(algorithm.__name__, algorithm(random_seq))

    print "\nrandom_seq after: {}".format(random_seq)
