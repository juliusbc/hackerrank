import collections
# check that at most one character doesn't have an even number of occurances
print("YES" if (sum([count % 2 for count in collections.Counter(input()).values()]) < 2) else "NO")