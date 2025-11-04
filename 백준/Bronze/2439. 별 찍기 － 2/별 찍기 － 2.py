N = int(input())
for i in range(1, N + 1):
    temp = ('*' * i)
    print(temp.rjust(N))