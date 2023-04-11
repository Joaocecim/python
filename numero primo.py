while n 
n=int(input('Digite um número inteiro:'))
c=2
primo=True
for val in range(c,n):
    if n % val==0:
        primo=False
print(primo)
