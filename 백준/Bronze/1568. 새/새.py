N = int(input())
K = 1
time = 0

while N > 0:
    N -= K
    K += 1
    if K > N:
        K = 1
    time += 1
    
print(time)