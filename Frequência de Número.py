l=[]
k=[]
c=[]
n=int(input())
for i in range(n):
    l.append(int(input()))
l.sort()
for i in range(len(l)):
    if l[i] not in k:
        k.append(l[i])
        c.append(1)
    else:
        c[k.index(l[i])]+=1
for i in range(len(k)):
    print(f'{k[i]} aparece {c[i]} vez(es)')


