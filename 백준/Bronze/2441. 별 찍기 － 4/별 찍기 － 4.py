N = int(input())

for i in range(N, 0, -1):
    temp = '*' * i
    print(temp.rjust(N))