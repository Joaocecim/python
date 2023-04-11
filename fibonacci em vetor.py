''''
l=[1,1]
for i in range(2,10):
    l.append(l[i-1]+l[i-2])
print(l)

k=int(input())
x=1
a=0
b=1
for i in range(k):
    x=a+b
    b=a
    a=x
print(x)
'''''
k=int(input())
fib=0
c=0
x=1
a=1
b=1
while c<k:
    x=a+b
    b=a
    a=x
    if a-b>1:
        for i in range(b+1,a):
            fib=i
            c+=1
            if c==k:
                break
print(fib)