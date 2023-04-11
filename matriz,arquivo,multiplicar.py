def criar_matriz(arquivo):
    matriz=open(arquivo,'r')
    m1,n1,m2,n2=map(int,matriz.readline().split())
    matriz1=[]
    for i in range(m1):
        matriz1+=[list(map(int,matriz.readline().split()))]
    matriz2=[]
    for i in range(m2):
        matriz2+=[list(map(int,matriz.readline().split()))]
    matriz.close()
    return matriz1,matriz2

matriz1,matriz2=criar_matriz('matriz.txt')
print(matriz1)
print(matriz2)

def multiplica(m1,m2):
    res=[]
    if len(m1[0])==len(m2):
        for i in range(len(m1)):
            res+=[[]]
            for j in range(len(m2[0])):
                res[i]+=[0]
                for k in range(len(m1[0])):
                    res[i][j]+=m1[i][k]*m2[k][j]
    else:
        print('Dimensões invalidas')
    return res
print(multiplica(matriz1,matriz2))