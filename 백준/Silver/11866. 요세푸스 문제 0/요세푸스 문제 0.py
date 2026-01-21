from collections import deque
import sys
def input(): return sys.stdin.readline().rstrip()

n, k = map(int, input().split())
deq = deque()
result = []
for i in range(1, n+1):
    deq.append(i)
while deq:
    deq.rotate(-(k-1))
    result.append(deq.popleft())
print('<' + ', '.join(map(str, result)) + '>')