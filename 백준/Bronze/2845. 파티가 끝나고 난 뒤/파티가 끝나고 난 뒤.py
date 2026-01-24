import sys
def input(): return sys.stdin.readline().rstrip()

n, m = map(int, input().split())
participant = list(map(int, input().split()))
num = n * m
result = []
for k in range(5):
    temp = participant[k] - num
    result.append(temp)
print(' '.join(map(str, result)))