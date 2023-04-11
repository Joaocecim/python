n=int(input())
pares=[]
impares=[]
resultado=[]
for i in range(n):
    k=int(input())
    if k % 2 == 0:
        pares.append(k)
    else:
        impares.append(k)
pares.sort()
impares.sort(reverse=True)
for i in range(len(pares)):
    resultado.append(pares[i])
for i in range(len(impares)):
    resultado.append(impares[i])
for i in range(len(resultado)):
    print(resultado[i])