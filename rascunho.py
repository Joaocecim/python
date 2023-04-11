import random
palavras=['banana','carro','planta','janela']
random.shuffle(palavras)
escolhida = palavras[0]
saida='_'*len(escolhida)

print(saida)
print(escolhida)
nova_saida=''
letra=input()
tentativa=0
while escolhida != saida and tentativa<5:
    acertou=False

    for i in range(len(escolhida)):

        if letra == escolhida[i]:

            acertou=True
            nova_saida+=letra
            print(nova_saida)
        else: nova_saida += saida
    saida = nova_saida
    if not acertou:
        print('A letra',letra,'não pertence à palavra')
    tentativa+=1
    letra=input()


