l,c,m,n=map(int,input().split())
notas = []
for i in range(3):
#cria linha vazia
    linha = []
    for j in range(5):
#vai adicionando as notas na linha
        linha.append(eval(input('Digite a nota [' + str(i) + ',' + str(j) + ']:')))
#adiciona a linha na matriz turma
notas.append(linha)
print()