n = int(input())
title = {}

for i in range(n):
    b = input()
    if b in title:
        title[b] += 1
    else:
        title[b] = 1
max_count = max(title.values())

book = []
for name, count in title.items():
    if count == max_count:
        book.append(name)
        
book.sort()
print(book[0])