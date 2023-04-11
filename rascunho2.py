while True:
    moedas=[]
    m=int(input())
    primo=True
    soma=0
    for i in range(m):
        moedas+=[int(input())]
    n=int(input())
    for i in range(0,len(moedas),n):
        soma+=i
    for i in range(2,soma):
        if soma % i ==0:
            primo=False

    if primo == True:
        print('You’re a coastal aircraft, Robbie, a large silver aircraft.')
        break
    else:print('Bad boy! I’ll hit you.')
