# for every input
for _ in range(int(input())):
    number = input();
    # count the number of times a digit that isn't zero divides the number
    print(sum([(int(digit) != 0 and int(number) % int(digit) == 0) for digit in number]))