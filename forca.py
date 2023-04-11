import random
l=['pato','cadeira','mesa','carta']
sorteado=l[random.randint(0,len(l)-1)]
palavra='_'*len(sorteado)
letra=input()
nova_saida='_'
for i in range(len(palavra)):
    if letra in sorteado:
        nova_saida+=letra
    else:print('errou')
print(palavra)


