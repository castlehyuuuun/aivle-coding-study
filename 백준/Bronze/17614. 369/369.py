n = int(input())
count = 0
for i in range(1, n+1):
    numFor3 = str(i)
    count += numFor3.count('3') + numFor3.count('6') + numFor3.count('9')
print(count)