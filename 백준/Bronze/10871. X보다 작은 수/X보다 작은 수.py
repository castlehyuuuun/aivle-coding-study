N, X = map(int, input().split())
A = list(map(int, input().split()))[:N]

for i in range(len(A)):
    if A[i] < X:
        print(A[i], end=' ')