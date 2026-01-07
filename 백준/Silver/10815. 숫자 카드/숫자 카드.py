n = int(input())
ncard_number = set(map(int, input().split()))
m = int(input())
mcard_number = list(map(int, input().split()))
ls = []
for k in mcard_number:
    if k in ncard_number:
        ls.append('1')
    else:
        ls.append('0')
print(' '.join(ls))