#!/bin/python3
'''

It's really easy to have off-by-1 errors in these problems.
Pay very close attention to your list indexes and your < vs <= operators.
'''


def find_smallest_positive(xs):
    left = 0
    right = len(xs) - 1

    def go(left, right):
        mid = (left + right)//2
        if xs[mid] == 0:
            return mid + 1
        if left == right:
            if xs[mid] > 0:
                return mid
            else:
                return None

        if xs[mid] > 0:
            return go(left, mid - 1)
        if xs[mid] < 0:
            return go(mid + 1, right)

    if len(xs) == 0:
        return None

    if xs[0] > 0:
        return 0
    else:
        return go(left, right)


def count_repeats(xs, x):
    left = 0
    right = len(xs) - 1

    def first(left, right):
        mid = (left + right) // 2
        if xs[mid] == x:
            if mid == 0 or xs[mid - 1] > x:
                return mid
            else:
                return first(left, mid - 1)

        if left == right:
            return None
        if x > xs[mid]:
            return first(left, mid - 1)
        if x < xs[mid]:
            return first(mid + 1, right)

    def second(left, right):
        mid = (left + right) // 2
        if xs[mid] == x:
            if mid == (len(xs) - 1) or x > xs[mid + 1]:
                return mid
            else:
                return second(mid + 1, right)
        if left == right:
            return None
        if xs[mid] > x:
            return second(mid + 1, right)
        if x > xs[mid]:
            return second(left, mid - 1)

    if len(xs) == 0:
        return 0
    more = first(left, right)
    less = second(left, right)

    if more is None or less is None:
        return 0

    else:
        return less - more + 1


def argmin(f, lo, hi, epsilon=1e-3):
    def go(lo, hi):
        m1 = lo + (hi - lo) / 4
        m2 = lo + (hi - lo) / (1.3333)
        if (hi - lo) < epsilon:
            return hi
        if f(m1) > f(m2):
            return go(m1, hi)
        if f(m1) < f(m2):
            return go(lo, m2)
    return go(lo, hi)

############################################################################
# the functions below are extra credit
############################################################################


def find_boundaries(f):
    '''
    Returns a tuple (lo,hi).
    If f is a convex function, then the
    minimum is guaranteed to be between lo and hi.
    This function is useful for initializing argmin.

    HINT:
    Begin with initial values lo=-1, hi=1.
    Let mid = (lo+hi)/2
    if f(lo) > f(mid):
        recurse with lo*=2
    elif f(hi) < f(mid):
        recurse with hi*=2
    else:
        you're done; return lo,hi
    '''


def argmin_simple(f, epsilon=1e-3):
    '''
    This function is like argmin, but it internally
    uses the find_boundaries function so that
    you do not need to specify lo and hi.

    NOTE:
    There is nothing to implement for this function.
    If you implement the find_boundaries function correctly,
    then this function will work correctly too.
    '''
    lo, hi = find_boundaries(f)
    return argmin(f, lo, hi, epsilon)
