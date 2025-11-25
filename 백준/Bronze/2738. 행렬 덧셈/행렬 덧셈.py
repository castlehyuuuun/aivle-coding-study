n, m = map(int, input().split())
a, b = [], []
for i in range(n):
    line = list(map(int, input().split()))
    a.append(line)
for i in range(n):
    line = list(map(int, input().split()))
    b.append(line)
    
for t in range(n):
    for k in range(m):
        print(a[t][k] + b[t][k])