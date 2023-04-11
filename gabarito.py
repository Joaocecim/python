def cria_matrizes(arquivo):
    matrizes=open(arquivo,'r')
    m1,n1,m2,n2=map(int,matrizes.readline().split())
    matriz1=[]
    for i in range(m1):
        matriz1+=[list(map(int,matrizes.readline().split()))]
    matriz2=[]
    for i in range(m2):
        matriz2+=[list(map(int,matrizes.readline().split()))]
    matrizes.close()
    return matriz1,matriz2

m1,m2=cria_matrizes('matriz.txt')
print(m1)
print(m2)
arq='matriz.txt'
def multiplica(m1,m2):

    mult_m = []

    if len(m1[0]) == len(m2):
        for i in range(len(m1)):
            mult_m+=[[]]
            for j in range(len(m2[0])):
                mult_m[i] += [0]
                for k in range(len(m1[0])):
                    mult_m[i][j] += m1[i][k] * m2[k][j]
        print(mult_m)

    else:
        print(''' Dimensões inválidas! Verifique se o número
       de colunas de m_1 é igual ao número de linhas de m_2''')
print(multiplica(m1,m2))
