# used wolframalpha
# recurrence on floor(N/2), a(n)=2*a(n-1)+1, a(0)=1, a(1)=3 -> -1+2^(1+n)
# use factor of N % 2 + 1 for odd N

a = lambda n: 2**(1 + n) - 1

for _ in range(int(input())):
    N = int(input())
    print(a(N // 2) * (N % 2 + 1))
        