import sys
input = sys.stdin.readline
n = int(input())
n_stack = []
for i in range(n):
    command = list(map(int, input().split()))
    if 1 == command[0]:
        n_stack.append(command[1])
    elif 2 == command[0]:
        if n_stack:
            print(n_stack.pop())
        else:
            print(-1)
    elif 3 == command[0]:
        print(len(n_stack))
    elif 4 == command[0]:
        if len(n_stack) == 0:
            print(1)
        else:
            print(0)            
    elif 5 == command[0]:
        if n_stack:
            print(n_stack[-1])
        else:
            print(-1)