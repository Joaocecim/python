import random
n=int(input())
cartelas=[]
num_sort=random.randint(0,99)
for i in range(n):
    linhas=[]
    for j in range(20):
        linhas+=[random.randint(0,99)]
    cartelas+=[linhas]
ini_cartela=(i-1)*20
fim_cartela=ini_cartela+19
while True:
    for i in range(len(cartelas)):
        for j in range(len(cartelas)):
            num_sort=random.randint(0,99)
            print(num_sort)
            if cartelas[i][j] == num_sort:



