import bisect
import random
import sys

import numpy as np

HAYSTACK = np.arange(1, 30, 2)
NEEDLES = np.arange(1, 30, 3)
ROW_FMT = '{0:2d} @ {1:2d}     {2}{0:<2d}'


def demo(bisect_fn):
    for needle in reversed(NEEDLES):
        position = bisect_fn(HAYSTACK, needle)
        # graphical offset showing where the item is to be inserted
        offset = position * '  |'
        print(ROW_FMT.format(needle, position, offset))


def grade(score, bisect_fn, breakpoints=None, grades='FDCBA'):
    """
    Use case of bisect: table lookups by numeric values, such as converting scores to grades.
    """
    if breakpoints is None:
        breakpoints = [60, 70, 80, 90]
    i = bisect_fn(breakpoints, score)
    return grades[i]


def demo_insort(list_size):
    random.seed(1917)
    my_list = []
    for i in range(list_size):
        new_item = random.randrange(list_size * 2)
        bisect.insort(my_list, new_item)
        print('%2d ->' % new_item, my_list)

if __name__ == "__main__":
    # When the items are equal in comparison, bisect_right returns an insertion point after the existing item,
    # and bisect_left returns the position of the existing item
    if sys.argv[-1] == 'left':
        bisect_fn = bisect.bisect_left
    else:
        bisect_fn = bisect.bisect_right

    print('DEMO:', bisect_fn.__name__)
    print('haystack ->', ' '.join('%2d' % n for n in HAYSTACK))
    demo(bisect_fn)

    # Faster than using the index method for very large lists.
    print('GRADES:')
    [print(f'{round(score)} -> {grade(round(score), bisect_fn)}') for score in np.linspace(30, 100, 7)]

    # Inserting an item into an ordered list
    demo_insort(list_size=7)
