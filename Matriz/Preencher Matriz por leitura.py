# notas = []
# for i in range(3):
# # cria linha vazia
#     linha = []
#     for j in range(5):
# #vai adicionando as notas na linha
#         linha.append(eval(input('Digite a nota [' + str(i) + ',' + str(j) + ']:')))
# #adiciona a linha na matriz turma
#     notas.append(linha)
# print(notas)
# PREENCHER COM 0
# ● Programa que cria uma matriz n x m preenchida com zeros
#
# n = eval(input('Digite a dimensão n da matriz: '))
# m = eval(input('Digite a dimensão m da matriz: '))
# matriz = []
# for i in range(n):
#   linha = []
#   for j in range(m):
#       linha.append(0)
#       matriz.append(linha)
#   print(matriz)
#
n = eval(input('Digite a dimensão n da matriz: '))
m = eval(input('Digite a dimensão m da matriz: '))
matriz = []
for i in range(n):
    matriz.append([0]*m)
for i in range(n):
        print(matriz[i])