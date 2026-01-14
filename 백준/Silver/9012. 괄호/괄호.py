import sys
def input(): return sys.stdin.readline().rstrip()


t = int(input())
ls = []
for i in range(t):
    n = input()
    ls.append(n)
    
for k in range(t):
    cnt = 0
    for x in ls[k]:
        if x =='(':
            cnt += 1
        else:
            cnt -= 1
        if cnt <0:
            break
                  
    if cnt == 0:
        print('YES')
    else:
        print('NO')