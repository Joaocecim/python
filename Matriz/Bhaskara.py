#matriz m x n
#contar pares
import random
pares=0
matrix=[]
m=int(input())
n=int(input())
for i in range(m):
    matriz=[]
    for j in range(n):
        matriz+=[random.randint(0,100)]
    matrix+=[matriz]
print(matrix)
for i in range(len(matrix)):
    for j in range(len(matrix)):
        if matrix[i][j]%2==0:
            pares+=1
print(pares)