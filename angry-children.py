# let's avoid sorting the entire list of packets, in hopes of keeping the algorithm less than n*log(n).
# in fact let's even avoid holding all the packets in memory at the same time by using a stream-based algorithm

# the first K packets are necessarily the best packets.
# the values of the packets must all be stored, and then the next N-K packets processed
#   because if a new packet comes in and it should be included in the best packets,
#   either the min or max packet gets bumped off to be replaced by the next smallest/largest packet
#       whichever one decreases unfairness the most. (so any packet may be required)
#   most efficient implementation would use min-max heap or sorted array for constant insertion and O(logn) removal,
# so this approach would be O(K+(N-K)log(K)) runtime and O(K) in memory

# however I'll be lazy and just "brute-force" with a full sort for the implementation in O(NlogN)
import itertools

N, K = int(input()), int(input())
packets = sorted([int(input()) for _ in itertools.repeat(None, N)])

#find the minimum difference between a pair that includes K elements between them, (0,K-1) to (N-K+1,N)
print(min(map(lambda a,b: b-a, packets[:N-K+1], packets[K-1:])))
