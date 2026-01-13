n = int(input())
ls = [1,2,3,4,5,6,7,8,9]
num = 0
for i in range(1, 10):
    for j in range(1, 10):
        num = i * j
        ls.append(num)
if n in ls:
    print(1)
else:
    print(0)