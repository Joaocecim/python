import random
matrix=[]
pares=0
for i in range(5):
    matriz=[]
    for j in range(5):
        matriz+=[random.randint(0,1000)]
    matrix+=[matriz]
for i in range(len(matrix)):
    for j in range(len(matrix)):
        if matrix[i][j] % 2 ==0:
            pares+=1
print(pares)
print(matrix)
