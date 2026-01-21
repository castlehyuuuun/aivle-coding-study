from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
n_deque = deque()
for k in range(n):
    command = list(map(int, input().split()))
    if 1 == command[0]:
        n_deque.appendleft(command[1])
    elif 2 == command[0]:
        n_deque.append(command[1])
    elif 3 == command[0]:
        if n_deque:
            print(n_deque.popleft())
        else:
            print(-1)
    elif 4 == command[0]:
        if n_deque:
            print(n_deque.pop())
        else:
            print(-1)
    elif 5 == command[0]:
        print(len(n_deque))
    elif 6 == command[0]:
        if len(n_deque) == 0:
            print(1)
        else:
            print(0)
    elif 7 == command[0]:
        if n_deque:
            print(n_deque[0])
        else:
            print(-1)
    elif 8 == command[0]:
        if n_deque:
            print(n_deque[-1])
        else:
            print(-1)