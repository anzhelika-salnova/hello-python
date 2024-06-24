
#Print all integer powers of two, less or equal N.

N = int(input())
k = 0
while 2 ** k <= N:
        print(2 ** k)
        k += 1