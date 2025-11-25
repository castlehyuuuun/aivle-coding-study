lis = input()

alph = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

num = 0
for i in range(len(lis)):
    for j in alph:
        if lis[i] in j:
            num += alph.index(j) +3
print(num)