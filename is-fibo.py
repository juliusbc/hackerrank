import math

# implementing https://en.wikipedia.org/wiki/Square_number#Properties
def is_square(num):
    x = str(num)
    # A square number can end only with digits 1, 4,6, 9, 00, or 25
    if (x[-1:] not in ['1', '4', '6', '9'] and
        x[-2:] not in ['00', '25']):
        return False
    # could be improved using newton's method and stopping when it's clear it isn't an integer
    return math.sqrt(num).is_integer()
    
# implementing https://en.wikipedia.org/wiki/Fibonacci_number#Recognizing_Fibonacci_numbers
for _ in range(int(input())):
    x = int(input())
    # if and only if one or both of 5x^2+4 or 5x^2-4 is a perfect square
    print("IsFibo" if is_square(5*x*x+4) or is_square(5*x*x-4) else "IsNotFibo")