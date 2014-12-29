# imagine folding the word over itself and comparing the letters that need to match for palindromicity
# the minimum operations needed to make each pair match is the difference between them
# because you can reduce the larger letter until it is the same as the other one.
import itertools

chardiff = lambda x, y: abs(ord(x)-ord(y))

for _ in itertools.repeat(None, int(input())):
    word = input()
    L = len(word)
    # split in two with floor/ceiling(reverse floor) division and reverse second half
    pairs = zip(word[:L//2], word[-(-L//2):][::-1])
    print(sum(itertools.starmap(chardiff, pairs)))