#COMO CRIAR E MODIFICAR ARQUIVOS:

'''

'r' -> Usado somente para ler algo
'w' -> Usado somente para escrever algo
'r+'-> Usado para ler e escrever algo
'a' -> Usado para acrescentar algo 

'''
arq=open('arq.txt','w')
arq.write('gol do Brasil')
arq.close()
arq=open('arq.txt','a')
arq.write('\n2 x 0')
arq.close()