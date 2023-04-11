l=[4.00,4.50,5.00,2.00,1.50]
n,p=map(int,input().split())
c=0
for i in range(p):
    c+=l[n-1]
print(f'Total: R$ {c:.2f}')