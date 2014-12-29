#!/usr/bin/python3
import itertools

# check every possible pair
def maxXor(l, r):
    return max(
        itertools.starmap(
            lambda a,b: a ^ b,
            itertools.product(range(l,r+1), repeat=2)
        )
    )
if __name__ == '__main__':
    l = int(input())
    r = int(input())
    print(maxXor(l, r))
