t = int(input())

for i in range(t):
    n = int(input())
    food = list(map(int, input().split()))
    
    tot = sum(food)
    
    day = 1
    while tot <= n:
        tot *= 4
        day += 1
    print(day)