matrix=[]
pares=0
for i in range(3):
    linhas=[]
    for j in range(3):
        linhas.append(int(input('['+str(i)+','+str(j)+']')))
    matrix.append(linhas)
for i in range(len(matrix)):
    for j in range(3):
        if matrix[i][j]% 2 == 0:
            pares+=1
print(matrix)
print(pares)