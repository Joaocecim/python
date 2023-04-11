x1,y1,x2,y2=map(int,input().split())
teste=0
while x1 !=0 and x2!=0 and y1!=0 and y2 !=0:
    teste+=1
    c=0
    auxy=y1
    auxx=x1
    if y1<y2:
        y1=y2
        y2=auxy
    if x1<x2:
        x1=x2
        x2=auxx
    n=int(input())
    for i in range(n):

        xm,ym=map(int,input().split())
        if x2<=xm<=x1 and y2<=ym<=y1:
            c+=1
    print(f'Teste {teste}')
    print(c)
    x1, y1, x2, y2 = map(int, input().split())