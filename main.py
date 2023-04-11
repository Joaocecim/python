l=[]
v=[]
c=[]
n=int(input())
for i in range(n):
    l.append(int(input()))
for i in range(len(l)):
    if l[i] not in v:
        c.append(1)
        v.append(l[i])
    else:
        c[l.index(l[i])]+=1
for i in range(len(c)):
     print(f'{v[i]} aparece {c[i]} vez(es)')

print(l)
print(v)




